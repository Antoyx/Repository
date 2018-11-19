a = [1, 3, 5, 30, 42, 43, 500,600]


#def IsInList(list,value):
#    if value in list:
#        return 1
#    else:
#        return 0


print()

def BinarySearch(list,value):
    x = list[(len(list)) // 2]
    while value != x:
        print(str(len(list))+ "list length")
        if len(list)==1:
            return 0
        if value < x:
            del list[len(list)//2:len(list)]
            print ("List is now halved")
            x = a[len(a) // 2]
            print(x)
            print(list)
        if value > x:
            del list[0:len(list)//2]
            print("List is now halved")
            x = a[len(a) // 2]
            print(x)
            print(list)
    return 1


b=int(input("Give number"))

#print(IsInList(a,b))
print(BinarySearch(a,b))

