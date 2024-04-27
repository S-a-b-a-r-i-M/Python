import itertools

my_ls = [('8904738967', 'IN', '+91'), ('9942976912', 'IN', '+91')]
emails = ['sabari@gmail.com', 'muthu@gmail.com']

fill_values = ['N/A1', 'N/A2']  # Replace with your desired fill values

zipped_data = list(itertools.zip_longest(my_ls, emails, fillvalue=fill_values))
print(zipped_data)