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

#NESTED LOOP
'''
n=int(input("Enter n value:"))

print("Left angle triangle")
for i in range(1,n+1):    #LEFT ANGLE TRIANGLE
    for j in range(1,i+1):
        print(j,end=" ")
    print()

print("\nRight angle triangle")
for i in range(1,n+1):  #RIGHT ANGLE TRIANGLE
    for j in range(1,(n+1)-i):
        print(end="  ")
    for k in range(1,i+1):
        print(k,end=" ")
    print()
'''


#BREAK AND CONTINUE
for i in range(1,20):
    if i==10:
        break
    print(i,end=" ")
else:                   #ELSE IS NOT WORK WHILE USING BREAK 
    print("end of the loop")
print("\n")

name="sa b*ar,i-"
cleanedName=""
for ch in name:
    if not ch.isalpha():
        continue
    cleanedName+=ch

print("Cleaned Name:",cleanedName)