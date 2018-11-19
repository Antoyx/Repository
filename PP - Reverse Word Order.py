
def Query():
    return input("Please provide a scentence")

def Print(printable):
    print(printable)






def Reverse(text):
    split1 = text.split( (' '))
    reverse = []
    for x in reversed(split1):
        reverse.append(x)
        print (reverse)
    return reverse

text = Query()
print(Reverse(text))