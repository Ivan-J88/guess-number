print("GUESS THE NUMBER")
import random
choice1 = random.randint(1,101)
choice2 = int(input("Enter your choice: "))

def choice():
    if choice1 > choice2:
        print("Too low!")
    elif choice1 < choice2:
        print("Too high!")
    elif choice1 == choice2:
        print("You got it!")
    else:
        print("You entered the wrong choice!")

while choice1 != choice2:
    choice()
    print("Try again!")
    choice2 = int(input("Enter your choice: "))


