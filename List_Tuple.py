#LIST
'''
names=["sabari","arasu","tamil","george","ureka"]
ages=[21,20,21,24,25]
hetro=['a',97,'z',122,'A',65,"Z",91,9.01,False]

print(names,"\n",ages)
print(type(names))
#ITERATE ALL ELEMENTS
for name in names:
    print(name,end=" - ")

for i in range( len(ages) ):#LENGTH
    print(ages[i],end=" - ")

names.append("kishore") #ADDED AT LAST
ages.append(45)
names.insert(0,"shiva") #ADDED AT SPECIFIC INDEX
print("\n",names,"\n",ages)

#del names[2:len(names)-1]
#del names[-1]
names.remove("arasu")    #REMOVES FIRST OCCURENCE OF THE MATCHED VALUE
print("After deleting  value:",names)
#ages.pop()     #REMOVES LAST VALUE
print(ages.pop(4))
print("After deleting  value:",ages)

print("Temporary sort",sorted(ages),"Actual age list",ages)
names.sort()
print("Permanent sort",names)

names.reverse()
print(names)

print("first 3 naems and 3 ages",names[:3],ages[:3])

'''

#TUPLE
