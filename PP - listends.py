import sys

a = [5, 10, 15, 20, 25]
print(a)
print(len(a))


def firstlast(a):
    b=[a[0], a[len(a)-1]]
    print (b)
    return b

c=firstlast(a)
print(c)

