import sys


def getnumber():
    try:
        number=int(input("please provide a number"))
    except ValueError:
        print("you did not provide a proper number, try again")
        return 0
    return number

def searchprimes(number):
    for x in range(2,number):
        if number%x ==0:
            return 0
    return 1

print("This is a prime number searching tool")
number=0
while number==0:
    number=getnumber()

if searchprimes(number)==True:
    print("Your number is primenumber")
else:
    print("Your number is not a primenumber")