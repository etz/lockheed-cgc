import hashlib
import string
import random

#on your mark...
output = ""
stri = b""

def add2string():
    global stri
    if len(stri) > 98:
        stri = stri[1:]
    add = random.choice(string.ascii_letters)
    stri = stri + str.encode(add)

def return_hash():
    global output
    #change algorithm
    output = hashlib.sha256(stri).hexdigest()

#change matching data
while output[0:3] != "057":
    add2string()
    return_hash()
    print("\nhash:" + output)
    print("\n\nresult:" + stri.decode('utf-8'))

