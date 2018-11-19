import sys
import random


def Asknumber():
    Guess = input("Please guess a number between 1 and 9, write exit to quit")
    if Guess == "Exit" or Guess =="exit":
        sys.exit("exiting program")
    try:
        Guess = int(Guess)
    except ValueError:
        print("You did not provide a number!")
        return 0
    if Guess <1 or Guess > 9:
        print("you provided too small or too high number")
        return 0
    return Guess


def Compare(value):
    a = random.randint(1, 9)
    print("{0} random".format(a))
    if value == a:
        print("CORRECT!")
        return 1
    else:
        print("WRONG, try again with new number new random!")
        return 0

def initiate():
    number = 0
    while number == 0:
        number = Asknumber()
        print (number)
    return number

number=initiate()
while True:
    if Compare(number)==0:
        initiate()
    else:
        break

print("Conngratulations!")