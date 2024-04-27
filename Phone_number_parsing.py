import re
from typing import Tuple

import pycountry
import phonenumbers

nums = ["+1-212-456-7890", "+1-212-456-7890"]

for num in nums:
    try:
        phone = phonenumbers.parse(num, None)
        if not phonenumbers.is_valid_number(phone):
            raise ValueError(f"Invalid phone number: {num}")
        print('true')
    except phonenumbers.phonenumberutil.NumberParseException:
        raise ValueError(f"Invalid phone number: {num}")
'''
class PhoneNumberFormatter:
    def find_country_format(self, country_name):
        try:
            country = pycountry.countries.search_fuzzy(country_name)[0]
            country_alpha_code = country.alpha_2
            return country_alpha_code
        except LookupError:
            print("Country not found")
            return "IN"

    def format_phone_number_without_country_name(self, phone: str) -> tuple[str, str, str, int]:
        try:
            country_alpha_codes = ["IN", "US", "GB", "BD"]
            valid_formatted_res = []
            for alpha_code in country_alpha_codes:
                parsed_number = phonenumbers.parse(phone, alpha_code)
                if phonenumbers.is_valid_number(parsed_number):
                    number = str(parsed_number.national_number)
                    country_code = "+" + str(parsed_number.country_code)
                    valid_formatted_res.append((number, country_code, alpha_code, 1))

            if len(valid_formatted_res) == 1:
                return valid_formatted_res[0]
            elif len(valid_formatted_res) > 1:
                return valid_formatted_res[0][0], "", "", 0
            else:
                return "", "", "", 0
        except phonenumbers.phonenumberutil.NumberParseException as exp:
            print("Phone number is not parsable without_country_name")
            return "", "", "", 0

    def format_phone_number_using_prefix(self, phone: str) -> tuple[str, str, str, int]:
        try:
            if "+" in phone:
                parsed_number = phonenumbers.parse(phone)
                number = str(parsed_number.national_number)
                country_code = "+" + str(parsed_number.country_code)
                country_alpha_code = phonenumbers.region_code_for_number(parsed_number)
                return number, country_code, country_alpha_code, 1
            else:
                ph = "+" + phone
                parsed_number = phonenumbers.parse(ph, None)
                if phonenumbers.is_valid_number(parsed_number):
                    number = str(parsed_number.national_number)
                    country_code = "+" + str(parsed_number.country_code)
                    country_alpha_code = phonenumbers.region_code_for_number(parsed_number)
                    return number, country_code, country_alpha_code, 1

                return "", "", "", 0
        except phonenumbers.phonenumberutil.NumberParseException as exp:
            print("Phone number is not parsable using prefix")
            return "", "", "", 0

    def format_phone_number(self, phone: str, country_name: str = None) -> tuple[str, str, str, int]:
        try:
            pattern = r"[a-zA-Z$@#^%]"
            if re.search(pattern, phone):
                return "", "", "", 0

            if country_name:
                if len(country_name) > 3:
                    country_alpha_code = self.find_country_format(country_name)
                else:
                    country_alpha_code = country_name

                parsed_number = phonenumbers.parse(phone, country_alpha_code)
                number = str(parsed_number.national_number)
                country_code = "+" + str(parsed_number.country_code)

                return number, country_code, country_alpha_code, 1
            else:
                format_res = self.format_phone_number_using_prefix(phone)
                if format_res[0]:
                    return format_res

                format_res = self.format_phone_number_without_country_name(phone)
                if format_res[0]:
                    return format_res

            return phone, "", "", 0
        except phonenumbers.phonenumberutil.NumberParseException as exp:
            print("Phone number is not parsable")
            return "", "", "", 0


def ph_number_formatter_helper():
    phoneNumberFormatter = PhoneNumberFormatter()
    number_list =  [('9942976913', ''), ('6374605894', ''), ('+1 (848) 468-1086', ''),
                   ('2016162186', ''), ('1 (848) 468-1087', ''), ('91 70228 95190', ''),
                   ('89047 38967', ''), ('8801701068536', ''), ('9123d1sf9', ''),
                   ('-994@29 #7 6 &9 1 2-', ''), ('12016162186', ''), ('', '')]

    for number, country in number_list:
        formatted_number_details = phoneNumberFormatter.format_phone_number(number, country)
        if formatted_number_details[0]:
            print(formatted_number_details)

ph_number_formatter_helper()
'''

'''
10001 ->
9942976913 - +91 9942976913
6374605894 - +91 6374605894
2016162186 - 2016162186
10002 ->
+1 (848) 468-1086 - +18484681086
1(848) 468-1087 - +18484681086
10003 ->
89047 38967 - +9189047 38967
8801701068536 - +8801701068536
1004 ->
9123d1sf9 - invalid
-994@29 #7 6 &9 1 2- - invalid
'''
