import sys

def asknumber():
    try:
        a=int(input("please provide the amount of numbers for fibonacci"))
    except ValueError:
        print("value not given")
        return 0
    return a

def dothemath(value):
    y=[]
    y.append(0)
    new=1
    for x in range(1,value):
        y.append(new)
        new = new + y[len(y)-2]
    return y

def print1(fibonacci=[0,1,2,3,5]):
    print(fibonacci)

number = 0
while number == 0:
    number =asknumber()
list=dothemath(number)

print1(list)
