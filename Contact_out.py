import json
import logging
from typing import List

import requests
from pydantic import BaseModel, Field


class ContactOutProfile(BaseModel):
    url: str = Field("")
    email: List[str] = Field([])
    work_email: List[str] = Field([])
    personal_email: List[str] = Field([])
    phone: List[str] = Field([])
    github: List[str] = Field([])


class ContactOutResponse(BaseModel):
    status_code: int
    profile: ContactOutProfile = Field({})
    message: str = Field("")


class ContactOutApi:
    def __init__(self, api_token: str = ""):
        self.url = "https://api.contactout.com/v1/people/linkedin?profile="
        self.query = "&include_phone=true"
        self.headers = {
            "authorization": "basic",
            "token": "FdOR6dB6oKs9k0vvVco58lDI",
            # "token": api_token if api_token else ENVIRONMENT.CONTACT_OUT_API,
            "Accept": "application/json",
        }

    def contact(self, linkedin_url) -> ContactOutResponse:
        """
            Fetch contact details from ContactOut API
            using linkedin url
        Args:
            linkedin_url: linkedin url of the candidate

        Returns: ContactOutResponse
        """
        url = self.url + linkedin_url + self.query
        print(url)
        response = requests.request("GET", url, headers=self.headers)
        try:
            return ContactOutResponse.model_validate_json(response.text)
        except Exception as e:
            # logger.exception(e, extra={"url": url, "response": response.text})
            print(e)
            return ContactOutResponse(
                status_code=500, message="Error in ContactOut API"
            )
        
    def is_phone_exists(self, linkedin_url: str) -> bool:
        """
            Check if phone number exists in contact out server
            using linkedin url
        Args:
            linkedin_url: linkedin url of the candidate

        Returns: bool
        """
        url = f"https://api.contactout.com/v1/people/linkedin/phone_status?profile={linkedin_url}"
        response = requests.get(url, headers=self.headers)
        try:
            print(response.text)
            res = json.loads(response.text)
            return res['profile']['phone']
        
        except Exception as e:
            # logger.exception(e, extra={"url": url, "response": response.text})
            print(e)
            return False


if __name__ == '__main__':
    contact_out = ContactOutApi()
    linkedin_url = "https://www.linkedin.com/in/sabari-m-7b1112252/"
    if contact_out.is_phone_exists(linkedin_url):
        print("Sending contact out request ---> ")
        response = contact_out.contact(linkedin_url)
        print(response)
    else:
        print("Phone number is not available")

    
