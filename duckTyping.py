'''
duck typing allows you to focus on what an object can do (its interface) rather than what it is (its explicit class or type). It's a way to perform operations on objects
without requiring them to be of a specific class or type as long as they support the required methods and behaviors.

Key principles of duck typing:

1.Focus on Behavior: Instead of checking the type or class of an object, you check if it has the methods and properties needed for a specific operation.

2."If It Quacks Like a Duck...": If an object can perform the expected behavior, it's treated as if it belongs to the desired class.

3.Dynamic Nature: Duck typing is associated with dynamically typed languages like Python, where the type of a variable or object is determined at runtime.

'''

class Lion:
    def food(self):
        print("Lion etas meat")

class Deer:
    def food(self):
        print("Deer eats grass")

class Human:
    def food(self):
        print('Human eats both meat and grass')


def type_of_food(obj):
    obj.food()

lion=Lion()
type_of_food(lion)

deer=Deer()
type_of_food(deer)

human=Human()
type_of_food(human)


