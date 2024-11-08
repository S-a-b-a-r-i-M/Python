import re
import asyncio
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin
from httpx import AsyncClient, HTTPStatusError, RequestError


class WebsiteCareerPagePraser:
     
  def matches_career_pattern(self, url: str) -> bool:
      """Check if URL matches the careers/jobs pattern."""
      pattern = r"(careers?|jobs?|apply)(/|\?|.|-|_)"
      return bool(re.search(pattern, url, re.IGNORECASE))
  
  async def fetch_url(self, url: str) -> str:
     async with AsyncClient() as client:
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
          response = await client.get(url, headers=headers, timeout=5.0)
          response.raise_for_status()
          return response.text
        except (HTTPStatusError, RequestError) as e:
          print(f"Error fetching {url}: {str(e)}")
          return ""

  def extract_iframe_urls(self, soup: BeautifulSoup) -> list[dict[str, str]]:
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
                  if self.matches_career_pattern(src):
                    results.add(src)
          
          return results
      
      except Exception as e:
          print(f"Error processing iframes: {str(e)}")
          return []
     
  async def extract_job_post_links(self, career_page_url: str) -> list[str]:
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

    Returns:
    List[str]: List of job post URLs
    """
    try:
      content = await self.fetch_url(career_page_url)
      if not content:
        return []

      soup = BeautifulSoup(content, "html.parser")
      # with open("job_post_links.html", "w") as f:
      #   f.write(soup.prettify())

      job_urls: set[str] = set()
      # Extract the <a> tag, which contains the job post url in href attribute
      for a_tag in soup.body.find_all("a", href=True):
        href: str = a_tag.get("href")
        if self.matches_career_pattern(href) and not re.search(
           r"(linkedin|locale=)", href, re.IGNORECASE
        ):
          job_urls.add(urljoin(career_page_url, href))

      # Extract the <iframe> tag, which may contains the job post url in src attribute
      for iframe_url in self.extract_iframe_urls(soup):
        job_urls.update(self.extract_job_post_links(iframe_url))

      return list(job_urls)

    except Exception as e:
      print(f"Error: {e}")
      return []
    
  async def extract_jd_from_content(self, content: str) -> str:
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
          soup = BeautifulSoup(content, 'html.parser')
          
          # Search for specific elements
          potential_ids = ['job__description', 'job_description', 'job-description', 'job_details', 
                          'job-details', 'jobDisplay', 'overview', 'job', 'main-content', 'description', 
                          'content', 'careers']
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
                
          # search the available iframes
          
          # If nothing is found, return the whole body content
          return soup.body.get_text(strip=True, separator='\n') if soup.body and is_description_valid(text) else ""
      
      except Exception as e:
          print(f"An unexpected error occurred: {str(e)}")
          return ""
      
  async def extract_job_posts(self, career_page_url: str) -> list[dict[str, str]]:
    """
    """
    job_urls = await self.extract_job_post_links(career_page_url)
    if not job_urls:
        return []
    job_urls = job_urls[:5]

    page_contents = await asyncio.gather(
        *[self.fetch_url(url) for url in job_urls],
        return_exceptions=True,
    )

    valid_pages_with_url = [
        (url, content) 
        for url, content in zip(job_urls, page_contents) 
        if content and not isinstance(content, Exception)
    ]

    jds = await asyncio.gather(
        *[self.extract_jd_from_content(content) for _, content in valid_pages_with_url],
        return_exceptions=True
    )

    # Process results and create job data
    job_data = []
    for idx, jd in enumerate(jds):
        if jd:
            job_data.append({
                "apply_url": valid_pages_with_url[idx][0],
                "job_description": jd
            })

    print(f"for {career_page_url} found {len(job_data)} jobs")
    return job_data


paser = WebsiteCareerPagePraser()
asyncio.run(paser.extract_job_posts("https://job-boards.greenhouse.io/roofstock"))