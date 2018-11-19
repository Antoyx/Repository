import random
import sys
import string

PW=""

def AddNumber(PW):
    return PW+str(random.randint(1,9))

def AddLetter(PW):
    return PW+(random.choice(string.ascii_letters))

def AddSpecial(PW):
    special="!#¤%&/()=?`@£$€{[]}\|><,.-;:_"
    return PW+(random.choice(special))


def AskLength():
    Length = 0
    while Length == 0:
        try:
            Length = int(input("How many characters do you want in your password?"))
        except ValueError:
            print("You did not provide a proper value, try again")
            Length = 0
    return Length

Length = AskLength()

L1 = int(Length / 3)

for x in range(L1):
    PW=AddNumber(PW)

for x in range(L1):
    PW=AddLetter(PW)

for x in range(L1):
    PW=AddSpecial(PW)

while len(PW) !=Length:
    PW=AddNumber(PW)

print(PW)
list=list(PW)
random.shuffle(list)
print(list)
PW= ''.join(list)
print(PW)
