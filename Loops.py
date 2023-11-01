# print(output,end='')    #USED TO PRINT ON THE SAME LINE

# WHILE LOOP
'''
num1 = num2 = int(input("enter the num:"))
res = 0
while num1 > 0:
    rem = num1 % 10
    res = (res*10)+rem
    num1 //= 10

print("Reverse of {} is : {}".format(num2, res))
'''

# FOR LOOP
# for i in range(1,100,3):
#     print(i,end=" ")
#
# print("\n",list(range(1,10)))


# PRACTICE
'''
import math
end=int(input("Enter the end number:"))
for num in range(2,end):
    for i in range(2,int(math.sqrt(num))):
        if num%i == 0:
            print(num,"is not a prime ->{} * {}".format(i,num//i))
            break
    else:
        print(num,"is a prime")
'''

