def inifinite_number():
    print('statrt....')
    count = 0
    while True:
        yield count
        count += 1


gen = inifinite_number()
print(gen, type(gen))

for i in gen:
    print(i)
