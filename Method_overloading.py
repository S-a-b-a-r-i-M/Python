from multidispatch import dispatch

"""
Apart from this decorater we can use some other methods aslo like, 
  1.Using *args  : def add(datatype, *args):
  2.Using default parameter : def add(x,y, z=None):
"""


@dispatch(int, int)
def add(x, y):
    print('Adding two integers')
    return  x + y


@dispatch(int, int, int)
def add(x, y, z):
    print('Adding three integers')
    return x + y + z


@dispatch(float, float)
def add(x, y):
    print("Adding two floats")
    return x + y



if __name__ == "__main__":
    """
    In Backend, Dispatcher creates an object which stores different implementation and 
    on runtime it selects the appropriate method as the type and number of parameters passed.
    """
    # calling 2 int parameters method 
    print(add(5, 10),end="\n\n")

    # calling 3 int parameters method
    print(add(5, 10, 15),end="\n\n")

    # calling 2 float parameters method
    print(add(5.5, 4.4),end="\n\n")