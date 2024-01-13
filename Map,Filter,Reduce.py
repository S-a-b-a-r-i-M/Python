employees = [('sabari', 'male', 21), ('arasu', 'male', 21), ('varsa', 'female', 20)]
numbers = [2, 3, 4, 5, 6, 7, 8, 9]
# MAP()
'''
detail1=list(map(lambda item:(item[0],item[2])))
print(detail1)

def square(num):
    return num*num

num=list(map(lambda num:num-1,numbers))
print(num)

square_of_nums=list(map(square,numbers))
print(f"square of numbers : {square_of_nums}")
print("square of numbers : {}".format(square_of_nums))
'''


# FILTER FUNCTION

def is_odd(num) -> bool:
    if num % 2 == 0:
        return False
    return True


odd_nums = list(filter(is_odd,numbers))
print(f"odd numbres are {odd_nums}\n")


filterd = list(filter(lambda emp: emp[0][0] == 'v', employees))
print(filterd)
