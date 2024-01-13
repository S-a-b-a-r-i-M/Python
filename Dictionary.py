# DICTIONAY{}
'''
user1={'name':'sabari','age':21,'profession':"SDE",'log-in':True,'hobbi':['palying','learning']}
print(user1)

del user1['hobbi']
print(user1['name'],"'s Profession :",user1['profession'])
#print("not a key :",user1['mom'])    # KeyError: 'mom'

#ITERATION
print("----ITERATION----")
user1['log-in']=False

for key in user1:
    print(key,":",user1[key])

#METHODS
print("----METHODS----")
print("Keys:",type(user1.keys()))
print("Values:",user1.values())
print("Entries:",user1.items())

#LIST OF DICT
user2={'name':'arasu','age':21,'profession':"SDE",'log-in':False}
user3={'name':'ureka','age':25,'profession':"Testing",'log-in':True}

users=[user1,user2,user3]
print("All users list :",users)

#LIST IN DICT
user4={'name':'arasu','age':21,'profession':"SDE",'hobbi':['playing','reading','cycling']}
print(user4)
print(type(user4['hobbi']),user4['hobbi'])

# CONTAINS
print(user4.__contains__('name'))
print(user4.__contains__('arasu'))

print(user4.get('name'))

# DELETE AN ENTRY
practice2(user4.pop('name'))
'''

# COMPREHENSION
hero_names = ['Iron Man', 'Captain America', 'Thor', 'Hulk', 'Black Widow']
org_names = ['Tony Stark', 'Steve Rogers', 'Thor', ' Bruce Banner', 'Natasha Romanoff']

# my_dict = {}
# for key,value in zip(hero_names, org_names):
#     my_dict[key]= value
my_dict = {key : value for key, value in zip(hero_names,org_names)}
print('my_dict :', my_dict)

my_dict = {key : value for key, value in zip(hero_names,org_names) if key != 'Hulk'}
print('my_dict :', my_dict)