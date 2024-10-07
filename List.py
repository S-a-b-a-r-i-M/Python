#LIST
names=["sabari","arasu","tamil","george","ureka"]
ages=[21,20,21,24,25]
hetro=['a',97,'z',122,'A',65,"Z",91,9.01,False]
'''
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
names.remove("arasu")    #REMOVES FIRST OCCURRENCE OF THE MATCHED VALUE
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

#LIST OPERATION
"""
print("--------- LIST OPERATION ---------")
cs=["tamil","eng","maths","cs","phy","che"]
bio=["tamil","eng","maths","bio","phy","che"]
com=['tamil','eng','com']
sub=cs #'sub 'IT POINTS THE SAME MEMORY ADDRESS As 'cs'

# Print the memory address of the list
print("cs:",id(cs))
print("bio:",id(bio))
print("sub:",id(sub))

if not bio==cs:
    print("Content comparator")

#2D LIST
subjects=[cs,bio,com.copy()] # SHALLOW COPY
print("2D list:",subjects)
print("Removed maths from cs it will reflect on 2d",cs.remove("maths"))

for i in range(len(subjects)):  #ITERATION
    #print(subjects[i])
    for j in range(len(subjects[i])):
        print(subjects[i][j],end=' ')
    print()

subjects[2].append('bus_maths')
print("2D list:",subjects[2],"1D list:",com)
"""
#IF WE WANT TO COPY 2D LIST WE HAVE TO USE DEEP COPY


# MAP 
# WE CAN EASILY REPLACE THE map AND filter FUNCTIONS BY LIST COMPREHENSION
incremented_ages = list(map(lambda x: x+1,ages))
print(incremented_ages)