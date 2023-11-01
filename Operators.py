x = -10
y = -20

# ASSIGNMENT OPERATOR
'''

print("10+1 :", 10 + 1)
print("1.1-0.1 :", 1.1 - 0.1)
print("10*2 :", 10 * 2)
print("15/3 :", 16 / 3)
print("12%5", 12 % 5)
print("12//5", 12 // 5) #NEW ONE
print("2**8 :", 2 ** 8)
'''

# COMPARISION OPERATOR
'''
print("10==20 =", 10 == 20, "30==30 =", 30 == 30)
print("10!=20 =",10!=20)
print("10>9 =",10>9,"10>=11 =",10>=11)
print("2<1 =",2<1,"2<=6 =",2<6)
'''

# LOGICAL OPERATOR
'''
if x > 0 and x > 10:
    print("It a positive number and greater than to 10")
elif x>0 or x%2==0:
    print("either It is a positive number or even number")
else:
    print("it is a negative number")
'''

# BITWISE OPERATOR
print("----BITWISE OPERATOR---")
print(5 & 6)
print(5 | 6)
print(5 ^ 6)
print(5 & 6)
print(~5)
print(10 << 1)
print(10 >> 1)

# TERNARY OPERATOR
print("----TERNARY OPERATOR---")
min = x if x < y else y
print("Minimum :", min)
