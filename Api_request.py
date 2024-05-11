import requests

# signal hire ----------------------------------------------->
"""def get_keys_validity(keys):
    headers = {"apikey": keys}
    apiend = "https://www.signalhire.com/api/v1/credits"
    res = requests.get(apiend, headers=headers)
    print(res.content)
    print(res.status_code)
    if res.status_code == 200:
        return res.json()["credits"]
    return 0

@api_view(["GET"])
@authentication_classes([])
def get_signal_hire_credit_count(request):
    keys = SingleHireKeys.objects.filter(is_used=0).all()

    print("Total Keys found", len(keys))

    keys_dict = {}

    count = 0
    for key in keys:
        values = get_keys_validity(key.keys)
        if values == 0:# if the credit point is 0 then it is already used
            key.is_used = 1
            key.save()
            continue
        else:
            count += values

    return count"""


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
