import json
import re
from typing import Dict, List
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

################################################################################################################################
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage
from pydantic import BaseModel, Field

model = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash-8b",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    google_api_key="" # .env
) 
system_prompt = "Your task is to extract the data from the user text. Donot make up anything any information.If any field is not available return empty string"
prompt = [SystemMessage(content=system_prompt)]

class JdData(BaseModel):
    years_of_experience: str = Field(description="Years of experience required for the job.")
    location: str = Field(description="The job location. If remote just say `remote`")
    skills: str = Field(description="The skills required for the job,exactly as mentioned in the text by user itself.This can be a larger text also depending upon user text.")
    company_name: str = Field(description="The name of the company as mentioned in the text.")
    visa_type: str =Field(description="The type of work visa , ex: l2, h4, C2C, w2, gc, H1, opt, cpt,etc ")
    job_role: str =Field(description="Job designation/job role/job title.")

def get_structured_data(text: str) -> JdData:
    structured_model= model.with_structured_output(JdData)
    list_of_text = [text[i:i+2000] for i in range(0, len(text), 2000)]
    for i,chunk in enumerate(list_of_text):
        struct_data=structured_model.invoke(prompt + [HumanMessage(content=chunk if i==0 else str(struct_data)+chunk)])
    return struct_data 

################################################################################################################################

def matches_career_pattern(url: str) -> bool:
        """Check if URL matches the careers/jobs pattern."""
        pattern = r"(careers?|jobs?|apply)(/|\?|.|-|_)"
        return bool(re.search(pattern, url, re.IGNORECASE))


def extract_iframe_urls(soup: BeautifulSoup, base_url: str = None) -> List[Dict[str, str]]:
    """
    Extract, validate and filter iframe URLs from HTML content.
    
    Args:
        html_content (str): HTML content to parse
        base_url (str, optional): Base URL to resolve relative URLs
        
    Returns:
        List[Dict[str, str]]: List of dictionaries containing iframe details
    """
    def is_valid_url(url: str) -> bool:
        """Check if the string is a valid URL."""
        try:
            result = urlparse(url)
            return all([result.scheme, result.netloc])
        except Exception:
            return False
    
    try:
        results = set()
        # Step 1 & 2: Find all iframes and extract src attributes
        iframes = soup.find_all('iframe')
        
        for iframe in iframes:
            src = iframe.get('src', '')
            
            # Skip empty src attributes
            if not src:
                continue
            
            if is_valid_url(src):
                # Step 4: Check if URL matches career/jobs pattern
                if matches_career_pattern(src):
                  results.add(src)
        
        return results
    
    except Exception as e:
        print(f"Error processing iframes: {str(e)}")
        return []


def job_post_links(career_page_url: str) -> list[str]:
  """
  Extract job-related links from a career page.

  Pattern explanation:
  r"(?!.*linkedin)*(careers?|jobs?|apply)(/|\?|.|-|_)*\d"
  - Excludes URLs containing 'linkedin'
  - Requires 'career', 'careers', 'job', 'jobs', or 'apply'
  - Followed by '/', '?', '.', '-', or '_'
  - Must contain at least one digit(job_id)

  Valid examples:
  - https://company.com/careers/software-engineer-123
  - https://company.com/jobs?id=456&location=nyc

  Invalid examples:
  - https://linkedin.com/jobs/view/software-engineer
  - https://company.com/about-us
  """
  try:
    headers = {
      "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
      "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
      "Accept-Language": "en-US,en;q=0.5",
      "Referer": "https://www.google.com/",
      "DNT": "1",
      "Connection": "keep-alive",
      "Upgrade-Insecure-Requests": "1"
    }
    
    response = requests.get(career_page_url, headers=headers)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")
    with open("job_post_links.html", "w") as f:
      f.write(soup.prettify())

    job_urls: set[str] = set()

    # Extract the <a> tag, which contains the job post url in href attribute
    for a_tag in soup.body.find_all("a", href=True):
      href: str = a_tag.get("href")
      if matches_career_pattern(href) and not re.search(r"(linkedin|locale=)", href, re.IGNORECASE):
        job_urls.add(urljoin(career_page_url, href))

    # Extract the <iframe> tag, which may contains the job post url in src attribute
    for iframe_url in extract_iframe_urls(soup, career_page_url):
       job_urls.update(job_post_links(iframe_url))

    return list(job_urls)

  except Exception as e:
    print(f"Error: {e}")
    return []
  

def extract_job_description(jd_url: str) -> str:
    """
    Extract job description content from a given URL.
    
    Args:
    jd_url (str): URL of the job description page
    
    Returns:
    str: Extracted job description content
    """
    def is_description_valid(text: str) -> bool:
       if (len(text) > 1000 and 
            re.search(
              r"(job.?description|job.?summary|about.?the|responsibilities|responsibility|skills|qualifications)", 
              text,
              re.IGNORECASE
            )
        ):# otherwise it's not a valid job description
          return True
       
       return False

    try:
        response = requests.get(jd_url, timeout=20)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Search for specific elements
        potential_ids = ['job__description', 'job_description', 'job-description', 'job_details', 
                         'job-details', 'jobDisplay', 'overview', 'job', 'main-content', 'description', 
                         'content', 'careers'] # "job_summary"
        for tag in potential_ids:
            # Search for elements with id or class containing the potential id
            elements = soup.find_all(['div', 'section', 'main'], id=re.compile(tag, re.I))[:5] # take first five
            elements.extend(soup.find_all(['div', 'section', 'main'], class_=re.compile(tag, re.I))[:5])
            for element in elements:
                # Extract string content if found
                text = element.get_text(strip=True, separator='\n')
                if text and is_description_valid(text):
                    return text

        
        # Look for nested HTML
        nested_html = soup.body.find('html')
        if nested_html and nested_html.body:
              text = nested_html.body.get_text(strip=True, separator='\n')
              if is_description_valid(text):
                return text
        
        # If nothing is found, return the whole body content
        return soup.body.get_text(strip=True, separator='\n') if soup.body and is_description_valid(text) else ""
    
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")
        return ""

 # 1 - 10
roofstock = "https://job-boards.greenhouse.io/roofstock" # working fine
allganize = "https://www.allganize.ai/en/careers"
marqeta = "https://www.marqeta.com/company/careers/all-jobs" # fetch jd link is working  # fetch job description is not-working 
acuitybrands = "https://careers.acuitybrands.com/search/?createNewAlert=false&q=atrius&locationsearch=&optionsFacetsDD_department=&optionsFacetsDD_location=&optionsFacetsDD_title=&optionsFacetsDD_customfield5="
workable = "https://apply.workable.com/xqthesuperschoolproject/?lng=en" # jd link is not-working
freshworks = "https://careers.smartrecruiters.com/Freshworks" # working fine
zoho = "https://www.zoho.com/careers/#jobs" # fetch jd link is not-working # lazy loading
deloitte = "https://jobsindia.deloitte.com/search/?createNewAlert=false&q=&locationsearch=&optionsFeacetsDD_city=&optionsFacetsDD_customfield2=" # working fine
cisco = "https://jobs.cisco.com/jobs/SearchJobs/?3_19_3=%5B%22162%22%2C%22163%22%2C%22%22%5D&3_12_3=%5B%22194%22%2C%22187%22%2C%22191%22%2C%2255816092%22%2C%22197%22%5D&source=Cisco+Jobs+Career+Site&tags=CDC+Prof+engineering+software&projectOffset=0" # working fine
# hcl = "https://www.hcltech.com/engineering/job-opening" # having pagination # while fetching job description throwing HTTPSConnectionPool(host='www.hcltech.com', port=443): Read timed out
cts = "https://careers.cognizant.com/india-en/jobs/#results" # having pagination # working fine


# 11 - 20
"""
pandora = "https://retailcareers.pandoragroup.com/" # not working # french
renewfinancial = "https://renewfinancial.com/careers" # not working # 403 error
mosaic = "https://joinmosaic.com/about-us/careers/" # not working # dynamic loading
fivetran = "https://www.fivetran.com/careers#jobs" # not working # lazy loading
launchdarkly = "https://boards.greenhouse.io/launchdarkly" # working fine
zorrro = "https://zorrroservices.com/careers.html" # not working # different design (single page not two page)
boxbot = "https://www.boxbot.io/career" # not working # js Script
breezy = "https://breezy.band/careers/" # not working # js Script
appsmith = "https://www.appsmith.com/careers#open-roles" # working fine
automatic = "https://automattic.com/work-with-us/#open-positions" # not working # js Script
"""

for career_url in [roofstock]:
  links = job_post_links(career_url)
  with open("job_links.txt", "a", encoding="utf-8") as file:
    file.write(f"{career_url} ----------------------->\n{links}\n\n\n\n")

  for link in links:
    content = extract_job_description(link)
    print(content[:50], "\ntotal length:", len(content), "\nlink:", link, "\n\n")
    jd_data: JdData  = get_structured_data(content)

    with open("jd_data.jsonl", "a") as file:
      file.write(json.dumps(jd_data.model_dump()))



"""
Not Wokable Cases:
 1. loading from js script
 2. lazy loading
 3. requires authentication
"""