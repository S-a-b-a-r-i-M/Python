import re


# print("This is an escape string with newline: \n and tab: \t")  # ESCAPE CHARACTER STRING
# print(r"This is a raw string with literal backslash: \n")  # RAW STRING

'''
def check_email(text) -> bool:
    # create a regex to validate an Email
    regex = "([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+.[a-zA-Z0-9-.]+)"
    # pass the regular expression
    # and the string in search() method
    if re.search(regex, text):
        return True
    else:
        return False


email1 = "john.doe@example.com,jane_doe123@gmail.com,info@my-company.co.uk,invalid.email"
email2 = "jane_doe123@gmail.com"
email3 = "info@my-company.co.uk"
email4 = "invalid.email"
'''

# print(check_email(email1),check_email(email2),check_email(email3),check_email(email4))

# METHODS
def important_methods():
    sample1 = "123da vandha 7.15 da"
    sample2 = "naangale oru 7.15 da"
    pattern = r'\d+'
    res1 = re.match(pattern, sample1)  # Attempts to match the pattern at the beginning of the string.
    res2 = re.match(pattern, sample2)
    print("match :", res1.group() if res1 else False, res2.group() if res2 else False)

    res1 = re.search(pattern, sample1)
    res2 = re.search(pattern, sample2)
    print("search :", res1.group() if res1 else False, res2.group() if res2 else False)

    res1 = re.findall(pattern, sample1)
    print("findall :", res1)


# important_methods()

# METACHARACTERS
# bus = "The bus is ready 190 c to go"
#
# res = re.findall('[a-c]', bus)  # []	A set of characters	 "[a-m]"
# print(res)
#
# res = re.search('re..y', bus)  # Any character (except newline character)
# print(res.group() if res else 'No match')
#
# res = re.match(r'^The', bus)  # ^	Starts with	"^hello"
# print(res.group() if res else 'No match')
#
# res = re.findall(r'g.*$', bus)  # $	Ends with	"planet$"
# print(res)
#
# res = re.findall(r'r.+y', bus)  # + One or more occurrences "he.*o"
# print(res)
#
# res = re.findall(r'r.*eady', bus)  # *	Zero or more occurrences "he.+o"
# print(res)
#
# res = re.findall(r'r.*eady', bus)  # ?	Zero or one occurrences	"he.?o"
# print(res)
#
# res = re.findall(r'r.{3}y', bus)  # {}	Exactly the specified number of occurrences	"he.{2}o"
# print(res)
#
# res = re.findall(r'r.{2}y|r.{3}y', bus)  # |	Either or	"falls|stays"
# print(res)
#
# res = re.findall(r'\d', bus)  # \d	digits(0-9)
# print(res)

# sanitized_string = re.sub(r"[^\w\s]", "", input_string)


'''string = "array to_string fgfsfhfjlfsdusdnb ffhj,fgmndgjngnmdf fffdffjnxdfmvndfvbfvjm n('%c%','%c++%','%java%')"

# Extract words enclosed in '%' symbols
matches = re.findall(r'%([^%]+)%', string)

print(matches, type(matches))
'''

'''def check_gmail(text) -> bool:
    # create a regex to validate an Email
    gmail_regex = re.compile(r"^[a-zA-Z0-9_.+-]+@gmail\.com$")
    # Check if the email matches the regex
    return bool(gmail_regex.match(text))


def is_valid_mail(email):
    # Regular expression for a basic email validation
    email_pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

    # Check if the email matches the pattern
    if re.match(email_pattern, email):
        return True
    else:
        return False


print(is_valid_mail("user@gmail.com"))
print(is_valid_mail("sabari@Hire10x.ai"))

print(is_valid_mail("valid@example.com"))
print(is_valid_mail("inval@id@example.com"))
print(is_valid_mail("@gmail.com"))
print(is_valid_mail("@gmailcom"))'''


################################
### EXTRACTING NAME FROM URL ###
################################
urls = [
    "",
    "https://www.bmwmotorcycles.com/en/public-pool/cont...",
    "https://www.billjacobsbmw.com/",
    "https://www.bmwrochester.com/",
    "https://www.bmwdtla.com/",
    "https://www.faulknerbmw.com/",
    "https://www.stevenscreekbmw.com/",
    "https://www.patrickbmw.com/",
    "https://www.fieldsbmwnorthfield.com/",
    "https://www.bmw.com/en/index.html"
]

business_names = []
for url in urls:
    match = re.search(r'(?<=www\.)(.*?)(?=\.)', url)
    if match:
        business_names.append(match.group(0))

print(business_names)
