import random
import sys
import string
def RandomGen(length):
    return ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=length))

password = RandomGen(9)
print(password)