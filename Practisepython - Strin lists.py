b=input("Please provide a palindrome")


for n in range(len(b)):
    print (n)
    print (b[n])
    print (b[len(b)-n-1])
    if b[n] != b[len(b)-n-1]:


        print("NOT A PALINDROME")
        break
    if n == len(b)-1:
        print ("Palindrome found!")