#IN HERER WE ARE GOING TO BUILD A SIMPLE GAME
import random

rand=random.randint(0,10)
guess=int(input("Can you guys guess the number!!! "))
point=0
while guess!=rand:
    print("Nope \U0001F61E")
    print("The answer is:",rand)
    rand=random.randint(0,10)
    guess = int(input("Can you try again??? "))

else:
    print("\U0001F600 You Won Hero!!!")

