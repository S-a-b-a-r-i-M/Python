# IF A FUNCTION TAKES A FUNCTION AS A PARAMETER OR RETURNS A FUNCTION THEN IT CALLED AS HIGHER ORDER FUNCTION
def welcome():
    print("hello")


def leave():
    print('good bye')
    return night


def morning(greet):
    greet()
    print("good morning")


def night():
    print('good night')


morning(welcome)
print()
gn = leave()
gn()
