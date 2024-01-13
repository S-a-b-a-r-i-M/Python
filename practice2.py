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