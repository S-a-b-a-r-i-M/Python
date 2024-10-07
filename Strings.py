#MULTIPLE ASSIGNMENTS IN A SINGLE LINE
'''
age,sis,mom="chithra","nithika",21

inspiration = "brucee-lee"
name="sabari"

#.format() OPERATOR
print("my inspiration is{}".format(inspiration))

#LENGTH
print("length :",len(name))

#REPEATED -> IT RETURNS A SINGLE STRING
print(name*3)

#STRING CASE CONVERSION
print("Upper->",inspiration.upper())  #UPPER
print("Lower->",inspiration.lower())  #LOWER
print("Title->",inspiration.title())  #TITLE - Pascal Case

#STRIP IT'S LIKE TRIM()
cricket="    India    "
print(cricket.strip())

#SPLIT  - Return a list of the substrings in the string, using sep as the separator string.
quote="Consistency is the key to success(Consistency)"
splitted_quote=quote.split(" ")
print(splitted_quote)
joined_quote="".join(splitted_quote)
print(joined_quote)

#STRING SEARCHING
print("Find ->",name.find("z"))  #Return -1 on failure
print("Index ->",name.index("a"))   #Raises ValueError when the substring is not found
print("Count->",quote.count('o'))

#REPLACE
updated_quote=quote.replace("Consistency","Commitment")
print("New quote ->",updated_quote)

#SUBSTRING
substr=quote[0:11]
print(substr)

#VALIDATION
name.isalnum()
name.isalpha()
name.isdigit()

#ITERATE BY CHARACTER BY CHARACTER
#print("Value in index2 ->",name[2])

'''

#SLICING
'''
print("------STRING SLICING------")
# @  h  i  r  e  1  0  x
# 0  1  2  3  4  5  6  7
# -8 -7 -6 -5 -4 -3 -2 -1
cmp_name="@hire10x"

print(cmp_name[2]) # i
print(cmp_name[0:5])
# print(cmp_name[5:0]) # IT WONT PRINT ANYTHING
print(cmp_name[-1])
print(cmp_name[-8:])
print(cmp_name[0:8:2]) #[stat:end-1:step]
# print(cmp_name[15]) # GIVING OUT OF RANGE INDEX (IndexError)
print("reverse :",cmp_name[8::-2]) #IT DECREMENT -1 FROM 8 EACH TIME
'''

value = "2 months"
periods = ["months", "weeks", "days", "month", "week", "day"]
if "month" in value.lower():
   print(value)
else:
   print("not found")


