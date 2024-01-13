# ANONYMS FUNCTION (PURPOSE : USE AND THROW)
'''
sum = lambda x, y, z=0: x + y + z
square_root = lambda num: num * num
is_eligible = lambda age: 'eligible' if age > 18 else 'Not eligible'
tot_sum= lambda arr :type(arr)

print(sum(10, 20, 3.33))
print(sum(10, 20))
print(square_root(12))
print(is_eligible(13))
print(is_eligible(21))
print(tot_sum([10,20,30,40]))
'''

# SORTING WITH KEYS
print('-----------SORTING WITH KEYS----------')
arr = [19, 53, 67, 32, 88, 34]
arr.sort(reverse=True)  # DESC SORTING
print(arr)

students = [(4, 'sabari', 90), (1, 'arasu', 92), (3, 'saran', 70), (9, 'dinesh', 88), (0, 'hajara', 95)]
students.sort()
print("Normal sorting:", students)
students.sort(key=lambda student: student[0])
print("Sorting based on id:", students)
students.sort(key=lambda student: student[2],reverse=True)
print("Sorting based on mark:", students)
print()

items = ((1002,'pen',50),(1001,'laptop',15000),(1010,'shirt',300),(1010,'book',300))
print(sorted(items,key=lambda item:item[1]))
