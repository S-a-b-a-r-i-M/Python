#TUPLES()

prime=(2,3,5,7,11,13,17,19,23,23,23,23)#BELOW 25
print(prime)

print("index of 11 :",prime.index(11))
try:
    print("index of not a value :",prime.index(21))
except:
    print("no value in tuple")
    
print("Frequency of 23 :",prime.count(23))
print("Frequency of not a value :",prime.count(21))

#prime[5]=32   #WE CANN'T MODIFY IT

days=('sun','mon','tue','wed','thu','fri','sat')

for day in days:
    print(day,end=" ")
print()

if 'mon' in days:
   print(True) 

print('mon' not in days)

