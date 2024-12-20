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

    # response = requests.request("GET", url, headers=headers)
    # print(response.text)


# print(contact())


url = "http://localhost:8080/user-service/v1/users/user"
headers = {
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1bmlxdWVfaWQiOiJoaXJlMTB4In0.d3ej4utGlmlIBbPUpfTvp6OR2Dj9HFWY8y6_8AE6rxI",
    "Content-Type": "application/json"
}

# res = requests.post(url, headers=headers)
# print(res.text)

url =  "https://raw.githubusercontent.com/dr5hn/countries-states-cities-database/refs/heads/master/json/countries%2Bstates%2Bcities.json"

res = requests.get(url)

with open("/home/new/PROGRAMMING_GROUND/Python/contries.json", "w") as file:
    file.write(res.text)