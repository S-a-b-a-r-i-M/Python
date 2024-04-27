# Writing to a file
with open('/home/hire10x/today_task', 'w') as file:
    file.write('Hello, this is an example.\n')

# Reading from a file
with open('/home/hire10x/today_task', 'r') as file:
    contents = file.read()
    print('Contents of the file:')
    print(contents)

# Appending to a file
with open('/home/hire10x/today_task', 'a') as file:
    file.write('Appending some more content.\n')

# Reading the updated file
with open('/home/hire10x/today_task', 'r') as file:
    contents = file.read()
    print('Updated contents of the file:')
    print(contents)
