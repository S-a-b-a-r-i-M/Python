# DEFAULT ARGUMENTS
def user(fname,lname=""):
    print("welcome",fname,lname)
    return

user("sabari","Murugan")
user("Arasu")

# VARIABLE LENGTH ARGS -- ELIPSIS
def sum(*args):
    print(type(args))
    print(*args,"\t",args)
    sum=0
    for i in args:
        sum+=i
    return sum

print(sum(10,20,30,40.1))


# KEYWORD ARGS
def print_user(**kwargs):
    print(type(kwargs))
    print(*kwargs,"\t",kwargs)

print_user(user_name="sabari",age=21,hobbi=['playing','reading','coding'])
