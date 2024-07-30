import requests

# contact out ----------------------------------------------->

def contact():
    # ERROR OCCURRING TOKEN IS INVALID
    url = "https://api.contactout.com/v1/stats?period=2023-04"
    headers = {
        "authorization": "basic",
        "token": "FdOR6dB6oKs9k0vvVco58lI",
        "Accept": "application/json",
    }

    response = requests.request("GET", url, headers=headers)
    print(response.text)


print(contact())
