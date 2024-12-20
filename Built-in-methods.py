# 1.any()
"""
any() function returns True if at least one element in the iterable is True, otherwise it returns False
syn:
    any(iterable) -> bool
"""
my_list = [0, '', None, False]
print(any(my_list))  # False - because none the single ele in this iterable is true
my_list.append(1)
print(any(my_list))  # True - because 1 is present in the list

# check is any non-alpha char present in text
text = "ugadhi!!!"
print("checking is any non-alpha char present in text", end=" , ")
print(any(not ch.isalnum() for ch in text))

values = {"m":7, "jd_id": 1}
validation_rules = {
    "JD": {
        "required_fields": ["jd_id","m"],
        "error_message": "JD id should not be empty"
    },
}
print(any(
    not values.get(field, False)
    for field in validation_rules["JD"]["required_fields"]
))


"""
class CustomException(Exception):
    def __init__(self, msg):
        print("Exception occured:", msg)


password = "P@ssword998877"

if not any(ch.isupper() for ch in password):
    raise CustomException("password should contain one upper case letter")

if not any(ch.isnumeric() for ch in password):
    raise CustomException("password should contain numeric value")

print("password accepted")
"""