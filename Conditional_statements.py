# IF STATEMENT
if 10 > 0:
    print("positive value")

if (True):  # WE CAN USE ()
    print("Im from the if")

# IF...ELSE STATEMENT
'''
num = int(input("Enter a number:"))  # PERFORMING TYPE CASTING
if num % 2 == 0:
    print(num, "is a even number")
else:
    print(num, "is a odd number")
'''

# LADDER IF
num1 = 14.19
num2 = 13
num3 = 14.2
#if num2<num1 and num1>num3
if num2 < num1 > num3:
    print("num1 is greater")
elif num2 > num3:
    print("num2 is greater")
else:
    print("num3 is greater")
print()

# NESTED IF
'''
age = int(input("Enter age:"))
gender = input("Enter gender:").lower()

if gender == "male":
    if age >= 21:
        print("You are eligible to get married")
    else:
        print("You are not ready yet...")
elif gender == "female":
    if age >= 18:
        print("You are eligible to get married")
    else:
        print("You are not ready yet...")
'''
