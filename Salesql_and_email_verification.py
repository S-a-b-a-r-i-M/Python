import asyncio
import json
import requests
from time import perf_counter

# domain documentation  - https://docs.abstractapi.com/email-validation
'''url = "https://emailvalidation.abstractapi.com/v1"

querystring = {"api_key":"31fdcf76a0ac473c82c78eb3b45e26f7","email":"vinoth@sugunaholdings.com"}

response = requests.request("GET", url, params=querystring)

print(response.text)'''

###################################
############ Salesql ##############
###################################

'''url = "https://api-public.salesql.com/v1/persons/enrich"

headers = {
    "accept": "application/json",
    "Authorization": "Bearer BCOSiI5nm75k1yS9jI8TNwgFTgJ3Igcu"
}

response = requests.get(url, headers=headers, params={"linkedin_url": "https://www.linkedin.com/in/iamsdt"})

print(response.text)'''
'''  
not_worked = ["https://www.linkedin.com/in/aswin-v-34322b261/", "https://www.linkedin.com/in/sabari-m-7b1112252/", 
              "https://www.linkedin.com/in/aswin-v-34322b261/", "https://www.linkedin.com/in/raj-karthi-7b2597215/",
              "https://www.linkedin.com/in/eubres-ureka-m-3320b41a5/", "https://www.linkedin.com/in/kiran-ravi-74baa12a3/"
              "https://www.linkedin.com/in/mutharasu-a-90638823b/", "https://www.linkedin.com/in/tamil-arasan-769b88247/"]  

worked_valid_emails = ["https://www.linkedin.com/in/therahulm/", "https://www.linkedin.com/in/charles-j-23b492129/", 
                       "https://www.linkedin.com/in/george-m-35aa65210/", "https://www.linkedin.com/in/vinoth-vinoth-2ba054256/" ,
                       "https://www.linkedin.com/in/praveen-saw-a5a09b27b/", "https://www.linkedin.com/in/iamsdt]

worked_invalid_emails = []
'''
# Response:
{
   "uuid":"e989973d-9de5-44df-bc9d-c9f456417318",
   "first_name":"George",
   "last_name":"M",
   "full_name":"George M",
   "linkedin_url":"https://www.linkedin.com/in/george-m-35aa65210",
   "title":"Frontend Web Developer",
   "headline":"Jr Frontend Developer",
   "industry":"IT Services and IT Consulting",
   "emails":[
      {
         "email":"nijenthen@gmail.com",
         "type":"Direct"
      }
   ],
   "location":"India IN",
   "organization":{
      "uuid":"8ddf71a9-619e-40da-8618-db3ed8613f21",
      "name":"ABShrms®",
      "website":"http://abshrms.com",
      "website_domain":"abshrms.com",
      "linkedin_url":"https://www.linkedin.com/company/abshrms",
      "founded_year":2019,
      "logo":"company/8ddf71a9-619e-40da-8618-db3ed8613f21-abshrms.png",
      "number_of_employees":112,
      "industry":"Human Resources Services",
      "location":"India IN"
   }
}

{
   "uuid":"d67edc9b-0d87-4a2f-869a-f5973f727546",
   "first_name":"Praveen",
   "last_name":"Saw",
   "full_name":"Praveen Saw",
   "linkedin_url":"https://www.linkedin.com/in/praveen-saw-a5a09b27b",
   "title":"Java Developer",
   "headline":"\"Passionate Java Developer|Scholar Trainee @\"WIPRO\"| Pursuing MTech - Software Systems | Wipro| Java FullStack Developer from Co",
   "industry":"Information Technology & Services",
   "emails":[
      {
         "email":"praveen.saw@wipro.com",
         "type":"Work"
      }
   ],
   "location":"India IN",
   "organization":{
      "uuid":"60dae984-f37e-467f-8458-b047d7ce8012",
      "name":"Wipro",
      "website":"http://www.wipro.com",
      "website_domain":"wipro.com",
      "linkedin_url":"https://www.linkedin.com/company/wipro",
      "founded_year":1945,
      "logo":"company/60dae984-f37e-467f-8458-b047d7ce8012-wipro.png",
      "number_of_employees":242143,
      "industry":"Manufacturing",
      "location":"United States US"
   }
}

from typing import List, Dict, Tuple
from pydantic import BaseModel, Field

class Organization(BaseModel):
    name: str = Field("")
    website: str = Field("")
    industry: str = Field("")
    location: str = Field("")

class Email(BaseModel):
    email: str
    type: str

class SalesQLResponse(BaseModel):
    status_code: int
    first_name: str = Field("")
    last_name: str = Field("")
    full_name: str = Field("")
    linkedin_url: str = Field("")
    emails: List[Email] = Field(None)
    location: str = Field("")
    organization: Organization | None = Field(None)
    detail: str = Field("")


class SalesQLApi:
    def __init__(self):
        self.url = "https://api-public.salesql.com/v1/persons/enrich"
        self.headers = {
            "accept": "application/json",
            "authorization": f"Bearer {'BCOSiI5nm75k1yS9jI8TNwgFTgJ3Igcu'}"
        }
    def _fetch_details(self, linkedin_url):
        response = requests.get(self.url, headers=self.headers, params={"linkedin_url": linkedin_url})
        return response.json()

    async def fetch_details(self, linkedin_url):
        print("SalesQL request sent ---> ",self.url)
        return await asyncio.to_thread(self._fetch_details, linkedin_url)

        # response = requests.get(self.url, headers=self.headers, params={"linkedin_url": linkedin_url})
        # return response.json()


async def send_salesql_request(links: List[str]) -> Tuple[List[str], List[str]]:
    sql_api = SalesQLApi()
    before = perf_counter()

    # ASYNC
    salesql_response: List[SalesQLResponse] = await asyncio.gather(*[sql_api.fetch_details(i) for i in links])
    print("time taken for links :", perf_counter() - before)
    for idx in range(len(salesql_response)):
        print(links[idx], salesql_response[idx], type(salesql_response[idx]))

    # SYNC
    # for link in links:
    #     salesql_response = sql_api.fetch_details(link)

    # print("time taken for links :", perf_counter() - before)


if __name__ == '__main__':
    asyncio.run(send_salesql_request(
                    ["https://www.linkedin.com/in/nick-kastenholz-7468b8271/",
                     "https://www.linkedin.com/in/muzammil-shaikh-90b278184/",
                     "https://www.linkedin.com/in/bhaveshtiwari704/",
                     "https://www.linkedin.com/in/shailesh-singh-b3344a45/",
                     "https://www.linkedin.com/in/hossain-ahamed-14274712a/"]
            )
    )
    pass