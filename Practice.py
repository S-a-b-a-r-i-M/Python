'''
if __name__ == '__main__':
    print("Like a main function",__name__)

if __name__ == '__main__':
    print("module 2")

name,age,salary="sabari",21,30000   #name=sabari,age=21,salary=30000
print(name,age,salary)
print("my name is {} ,im {}years old my salary is ${}".format(name,age,salary))
'''

#LIST OPERATION
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
print("Iteration")

print("Removed maths from cs it will reflect on 2d",cs.remove("maths"))
for i in range(len(subjects)):  #ITERATION
    #print(subjects[i])
    for j in range(len(subjects[i])):
        print(subjects[i][j],end=' ')
    print()

subjects[2].append('bus_maths')
print("2D list:",subjects[2],"1D list:",com)

#IF WE WANT TO COPY 2D LIST WE HAVE TO USE DEEP COPY


# PRINT ACSII VALUES
for i in str:
    print(i,ord(i))