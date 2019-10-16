import sys
import random
import string
arr = [106, 255, 184, 238, 0, 32, 77, 255, 37, 60, 23, 101, 47]
compArr = [57, 180, 225, 195, 69, 108, 14, 182, 8, 11, 39, 87, 25]
answer = ""

#b r u t e f o r c e 
def find_match(x):
    global answer
    while 1 > 0:
        #all possible characters
        test_letter = random.choice(string.printable)
        #reverse engineer function
        if arr[x] ^ ord(test_letter) == compArr[x]:
            return test_letter
            
#w a t c h m e
for x in range(len(arr)):
    #append
    answer = answer + find_match(x)
    print(answer)
