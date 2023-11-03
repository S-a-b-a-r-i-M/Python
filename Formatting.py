#STRING FORMATTING
name='sabari'
age=21
#FORMAT
name='sabari'
age=21

print("{}'s age is {}".format(name,age))

msg="Welocme"
print("****{:20}*****".format(msg))
print("****{:>20}*****".format(msg))
print("****{:<20}*****".format(msg))
print("****{:^20}*****\n".format(msg))

#NUMBER FORMAT
num=125000000
print("{:,}".format(num))

PI=22/7
print("Before format",PI," After formatting {:.2f}".format(PI))

num=5
print("Binary value of {} is {:b}".format(num,num))
print("Octal value of {} is {:o}".format(10,10))
print("Hexa value of {} is {:x}".format(21,21))