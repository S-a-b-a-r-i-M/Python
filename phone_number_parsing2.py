import re
import logging
import phonenumbers
from typing import List


class PhoneNumberFormatResult:
    def __init__(self, number: str | None, country_code: str | None, alpha_code: str | None, status: bool):
        self.number = number
        self.country_code = country_code
        self.alpha_code = alpha_code
        self.status = status


class PhoneNumbersFormatter:
    """
    This class is mainly used to format phone numbers.

    Args:
        cid : The candidate id
        phones : List of phone numbers or string of phone numbers (ex:['ph1',ph2','ph3'] or 'ph1,ph2,ph3')
        country_code : The country code of the candidate
        country_alpha_codes : List of country alpha codes which will be used to parse the phone number 
                              if there is no country code 

    Common-Attributes:
        number: It is the just phone numbers without any country code  digit number.
                Ex: 1234567890, 12345678901, etc,....
        country_alpha_code: It is the 2 or 3 digit(alphabet numbers) which represents the country.
                            Ex: India - IN, United States - US, United Kingdom - GB, etc,....
        country_code: It is the 1 or 2 digit numbers which represents the country.(mostly with '+')
                      Ex: India - +91, United States - +1, United Kingdom - +44, etc,....
        0 - invalid phone number, 1 - valid phone number

    Methods:

        format_phone_without_country_name(phone):
            Returns PhoneNumberFormatResult(number, country_code, alpha_code, valid) or 
            PhoneNumberFormatResult(phone, , None, False) if not parsable.

        format_phone_using_prefix(phone):
            Returns PhoneNumberFormatResult(number, country_code, alpha_code, valid) or 
            PhoneNumberFormatResult(phone, self.country_code, None, False) if not parsable.

        format_phone(phone, country_name):
            This is the starting method for parsing if the country name is
            provided it will parse otherwise it will try to parse the number
            using other methods.
    """

    def __init__(self, phones: List[str] | str, country_code: str, country_alpha_codes: List[str] = None):
        self.country_code = country_code
        self.country_alpha_codes = country_alpha_codes if country_alpha_codes else ["IN", "US"]

        if isinstance(phones, str):
            self.phones = phones.split(',')
        else:
            self.phones = phones

    def _format_phone_using_prefix(
            self, phone: str
    ) -> PhoneNumberFormatResult:
        """
        This method parse the number using prefix code.
        if prefix code exists in the number it will parse , (ex.+9199XXXXXXXX)
        otherwise it's try to parse by adding '+' as a prefix in the number

        Args:
            phone: The phone number

        Returns:
            number, country_code, alpha_code or "","","" if not parsable
        """
        try:
            phone = phone if '+' in phone else '+'+phone

            parsed_number = phonenumbers.parse(phone)
            if phonenumbers.is_valid_number(parsed_number):
                number = str(parsed_number.national_number)
                country_code = "+" + str(parsed_number.country_code)
                country_alpha_code = phonenumbers.region_code_for_number(
                    parsed_number
                )

                return PhoneNumberFormatResult(number, country_code, country_alpha_code, True)

            return PhoneNumberFormatResult(None, None, None, False)
        except phonenumbers.phonenumberutil.NumberParseException as exp:
            print("Phone number is not parsable using prefix")
            return PhoneNumberFormatResult(phone, self.country_code, None, False)

    def _format_phone_with_country_code(
            self, phone: str
    ) -> PhoneNumberFormatResult:
        """
        This is the starting point for parsing algorithm.
        if the country name and number is provided, it will parse the number and return the result.
        else it will try to parse the number using other methods. Those are,
        1) format_phone_without_country_name(phone)

        if any Exception occurs, it will return "","","", 0
        Args:
            phone: The phone number

        Returns:
            number, country_code, alpha_code or number,"","" if parsable.
            if not parsable returns "","",""
        """
        try:
            parsed_number = phonenumbers.parse(phone, self.country_code)
            if phonenumbers.is_valid_number(parsed_number):
                number = str(parsed_number.national_number)
                country_code = "+" + str(parsed_number.country_code)

                return PhoneNumberFormatResult(
                    number, country_code, self.country_code, True
                )

            return PhoneNumberFormatResult(None, None, None, False)
        except phonenumbers.phonenumberutil.NumberParseException as exp:
            print("Phone number is not parsable")
            return PhoneNumberFormatResult(phone, self.country_code, None, False)

    def _format_phone_without_country_code(
            self, phone: str
    ) -> PhoneNumberFormatResult:
        """
        This method is the last try of this parsing algorithm, it will try to parse the number
        by using a lot of country codes.
        if the number is parsable by only one country, the number is valid.
        else the number is parsable by more than one country its not valid returns only the number
        like number,"",""

        Args:
            phone: The phone number

        Returns:
            number, country_code, alpha_code or number,"","" if parsable by more than one country
            or "","","" if not parsable at least by one.
        """
        try:
            valid_formatted_res = []
            for alpha_code in self.country_alpha_codes:
                parsed_number = phonenumbers.parse(phone, alpha_code)
                if phonenumbers.is_valid_number(parsed_number):
                    number = str(parsed_number.national_number)
                    country_code = "+" + str(parsed_number.country_code)
                    valid_formatted_res.append(
                        PhoneNumberFormatResult(number, country_code, alpha_code, True)
                    )

            if len(valid_formatted_res) == 1:  # if its parsed by only one country
                return valid_formatted_res[0]
            elif len(valid_formatted_res) > 1:  # if its parsed by more than one country
                print("Phone number is parsable by more than one country")
                formatted_phone = (valid_formatted_res[0]).number
                return PhoneNumberFormatResult(formatted_phone, None, None, False)
            else:
                return PhoneNumberFormatResult(phone, None, None, False)

        except phonenumbers.phonenumberutil.NumberParseException as exp:
            print("Phone number is not parsable without_country_name")
            return PhoneNumberFormatResult(phone, None, None, False)

    def _format_single(self, phone: str) -> PhoneNumberFormatResult:
        """
        This method formats the phone number using the country code
        obtained from the candidate's information.
        1. Try to format the phone number using prefix code (ex. +91 1234567890) (if prefix code exists)
        2. If Prefix code does not exist, try to format the phone number by adding '+' as a prefix
        3. If not parsable, try to format the phone number with country code
        4. If not parsable, try to format the phone number without country code
        Args:
            phone (str): single phone number to be formatted
            cid: Candidate ID

        Returns:
            formatted phone number with status code for is_valid number or not
        """
        try:
            res = self._format_phone_using_prefix(phone)
            if res.status:
                return res

            if self.country_code:
                res = self._format_phone_with_country_code(phone)
            else:
                res = self._format_phone_without_country_code(phone)

            return res

        except phonenumbers.phonenumberutil.NumberParseException as exp:
            print("Phone number is not parsable")
            return PhoneNumberFormatResult(phone, self.country_code, None, False)

    @staticmethod
    def is_valid_phone(phone: str):
        """
        International phone numbering plan:
            1.phone numbers cannot contain more than 15 digits. 
            2.The shortest international phone numbers in use contain seven digits.
        """
        pattern = r"[a-zA-Z$@#^%]"
        if re.search(pattern, phone):
            return False

        return True

    def format(self) -> List[PhoneNumberFormatResult]:
        """
        This method is used to format the phone numbers using the country code
        obtained from the candidate's information.
        Logic:
        1. Try to format the phone number using prefix code (ex. +91 1234567890) (if prefix code exists)
        2. If Prefix code does not exist, try to format the phone number by adding '+' as a prefix
        3. If not parsable, try to format the phone number with country code
        4. If not parsable, try to format the phone number without country code

        Args:
            cid: Candidate ID

        Returns:
            list of formatted phone numbers with status code for is_valid number or not
        """
        results = []

        if not self.phones:
            return []

        for phone in self.phones:
            if not PhoneNumbersFormatter.is_valid_phone(phone):
                print("Phone number is not parsable - invalid phone number")
                continue

            res = self._format_single(phone)
            results.append(res)

        return results


def ph_number_formatter_helper():
    formatter = PhoneNumbersFormatter([''], 'IN')
    # formatter = PhoneNumbersFormatter(['9942976913', '6374605894', '+1 (848) 468-1086',
    #                                    '2016162186', '1 (848) 468-1087', '91 70228 95190',
    #                                    '89047 38967', '8801701068536', '9123d1sf9',
    #                                    '-994@29 #7 6 &9 1 2-', '12016162186'], '')

    for phone in formatter.format():
        print(phone.number, phone.country_code, phone.alpha_code, phone.status)


ph_number_formatter_helper()
