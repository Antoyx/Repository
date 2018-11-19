Name=input("Please tell me your name")
Age=input("Please tell me your age")
times = int(input("How many times do you wish to print the message?"))
Age=int(Age)
Fullk = 2018+1000-Age
Fullk=str(Fullk)
Age =str(Age)


Printout = ("Hello " + Name+ ". You are now "+ Age + " Years old. You will be 1000 years old in the year "+ Fullk+ "\n")
Printout = times * Printout
print (Printout)

##for x in range(times):
  ##  print("Hello " + Name+ ". You are now "+ Age + " Years old. You will be 1000 years old in the year "+ Fullk)