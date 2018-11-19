import sys

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 1, 16, 25]


def RemoveDuplicatesLoop (List):
    b =[]
    for x in List:
        if x not in b:
            b.append(x)
    return b


def RemoveDuplicatesSet (List):
    List = set(List)
    print(List)
    return List

print(RemoveDuplicatesLoop(a))
print(RemoveDuplicatesSet(a))



