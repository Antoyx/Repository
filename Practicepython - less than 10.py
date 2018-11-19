a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
c =int(input("Provide a number"))
b=[]
for n in a:
    if n < c:
        b.append(n)
        print(b)
