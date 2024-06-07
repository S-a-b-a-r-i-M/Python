# 1.FIBONACCI
'''
f1 = 0
f2 = 1
f3 = 0

size = int(input("Enter the size"))

print(f2, end=" , ")
while size > 0:
    f3 = f1 + f2
    f1 = f2
    f2 = f3
    print(f3, end=" , ")
    size -= 1
'''

# STRING PALINDROME
'''
while(True):
    str = input('Enter the word : ').strip()

    i=0
    j=len(str)-1

    while i<j:
        if(str[i]!=str[j]):
            print("Given string is not a palindrome")
            break
        i+=1
        j-=1
    else:
        print('Given string is prime')
'''

# 3.REVERSING STRING
'''
str = input("Enter a string : ")
rev_str = ""

i = len(str)-1
while i >= 0:
    rev_str += str[i]
    i -= 1

print("Reverse string is :",rev_str)
'''

# PRINTING REPEATING ELEMENTS IN A STRING
'''
string = "welcoomeBuddy".lower().strip()
arr = list()

for i in range(26):
    arr.append(0)

print("Repeating chars in",string)
for ch in string:
    idx = ord(ch) - 97
    arr[idx] += 1

for i in range(len(arr)):
    if arr[i] > 1:
        print(chr(i + 97), end=" , ")

print("\n",arr)
'''

# 4.SQUARE ROOT OF A NUMBER (BINARY SEARCH)
'''
while True:
    num = int(input('Enter the number : '))
    s, e = 1, num
    count = ans = 0
    
    while s <= e:
        mid = (s + e) // 2
        if (mid * mid) > num:
            e = mid - 1
        elif (mid * mid) < num:
            s = mid + 1
            ans = mid
        else:
            ans = mid
            break
        count += 1

    print("Approximate Square root of {} is {}".format(num, ans))
    print("Number of iteration :", count,"\n")
'''

# Online Python - IDE, Editor, Compiler, Interpreter
from datetime import datetime
import re
def calculate_duration(start_date, end_date):
        try:
            try:
                pattern = "%b %Y"
                start_date = datetime.strptime(start_date, pattern)
            except ValueError:
                pattern = "%m/%Y"
                start_date = datetime.strptime(start_date, pattern)

            # if end_date is not in the expected format then take the current date as end_date
            if not (re.findall(r'\d{4}',end_date)): 
                end_date = datetime.now()
            else:
                end_date = datetime.strptime(end_date, pattern)

            # Calculate the difference in years and months
            total_months = (end_date.year - start_date.year) * 12 + (
                end_date.month - start_date.month
            )
            years = total_months // 12
            months = total_months % 12

            # Construct the formatted output
            year_suffix = "years" if (years > 1) else "year"
            month_suffix = "months" if (months > 1) else "month"

            if years==0 and months==0:
                return f"0 month"
            elif not months:
                return f"{years} {year_suffix}"
            elif not years:
                return f"{months} {month_suffix}"
            else:
                return f"{years} {year_suffix} {months} {month_suffix}"
                
            
        except Exception as e:
            return None
            
# print(calculate_duration("09/2014", "12/2017"))

def calculate_exp(text) -> float:
        """
        Calculate the total experience based on the provided text.

        Parameters:
            text (str): The text containing the work experience information.

        Returns:
            float: The total experience calculated from the text.

        Example:
            >>> WorkExperienceRepo().calculate_exp("2 years 6 months")
            2.5

            >>> WorkExperienceRepo().calculate_exp("1 year")
            1.0

            >>> WorkExperienceRepo().calculate_exp("3 months")
            0.25
        """
        year = ""
        yr = r"\d+[ ]?yr"
        yrf = r"\d+[ ]?year"
        mh = r"\d+[ ]?mo"
        mhf = r"\d+[ ]?month"

        print(f"total text: {text}")

        exp = ""
        s1 = re.findall(yr, text)
        if len(s1):
            year = "".join([i for i in s1[0] if i.isdigit()])
            exp = year if year else "0"
        else:
            s2 = re.findall(yrf, text)
            if len(s2):
                year = "".join([i for i in s2[0] if i.isdigit()])
                exp = year if year else "0"

        s1 = re.findall(mh, text)
        if len(s1):
            month = "".join([i for i in s1[0] if i.isdigit()])
            if exp == "":
                exp = "0"
            exp += "." + month if month else "0"
        else:
            s2 = re.findall(mhf, text)
            if len(s2):
                month = "".join([i for i in s2[0] if i.isdigit()])
                if exp == "":
                    exp = "0"
                exp += "." + month if month else "0"

        # Convert years and months to a floating-point number
        try:
            years = float(exp.split(".")[0])
        except ValueError:
            years = 0

        # Check if there is a dot ('.') in exp before attempting to split
        try:
            months = float(exp.split(".")[1]) if "." in exp else 0
        except ValueError:
            months = 0

        total_exp = round(years + (months / 12), 2)

        return total_exp
    

print(calculate_exp("8 years 9 months"))