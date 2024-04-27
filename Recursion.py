#FACTORIAL
def factorial(num):
    if num<=1:
        return 1
    fact=num * factorial(num-1)
    return fact

num=int(input("enter the number:"))
print(factorial(num))