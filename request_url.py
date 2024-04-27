import requests


class ContactOutApi:
    def __init__(self, api_token: str = ""):
        self.url = "https://api.contactout.com/v1/people/linkedin?profile="
        self.query = "&include_phone=true"
        self.headers = {
            "authorization": "basic",
            "token": "FdOR6dB6oKs9k0vvVco58lI",
            "Accept": "application/json",
        }

    def contact(self, linkedin_url):

        url = self.url + linkedin_url + self.query
        print(url)
        response = requests.request("GET", url, headers=self.headers)
        try:
            print(response.text)
            return response.text
        except Exception as e:
            print(response.text)


# ContactOutApi().contact("https://www.linkedin.com/in/jsjoeio/")

res = requests.get("https://medium.com/@almaswebconsulting/django-5-0-what-is-new-in-it-ab990e5e782d#:~:text=The"
                   "%20Django%205.0%20comes%20with,into%20the%20distribution%20of%20data.")
print(res.content)
print(res.text)
