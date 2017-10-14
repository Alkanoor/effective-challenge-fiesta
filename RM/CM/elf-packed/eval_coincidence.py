import re
import binascii
import numpy as np


program = "ch12"
begin = "\xa0\x6c\xcc\x6e"
end = "kT2ee"

content = open(program,'rb').read()

code = begin+content.split(begin)[1]
code = code.split(end)[0]+end

#print(code)


def count(msg):
    m = {}
    for i in msg:
        if m.get(i) is not None:
            m[i] += 1
        else:
            m[i] = 1
    return m

def coincidence(msg):
    s = 0
    m = count(msg)
    orig = float(len(msg))
    for i in m:
        s += float(m[i])*float(m[i]-1)/orig/(orig-1)
    return s

alls = []
for i in range(2,80):
    moy = np.array([])
    for j in range(i):
        s = ''
        for k in range(j,len(code),i):
            s += code[k]
        moy = np.append(moy,coincidence(s))
    # print(i)
    # print(moy.mean())
    # print(moy.std())
    alls.append((i,moy.mean()))

for i in alls:
    if i[1]>0.01:
        print(i)

key_length = 19

ref = []
for j in range(key_length):
    s = ''
    for k in range(j,len(code),key_length):
        s += code[k]
    print("================")
    t = count(s).items()
    u = []
    for a in t:
        u.append((a[1],a[0]))
    u = sorted(u)[-2:]
    print(u)
    print(ord(u[0][1])^ord(u[1][1]))
    ref.append(ord(u[0][1]))

for i in range(256):
    s = ''
    for j in range(key_length):
        s += chr(ref[j]^i)
    print(s,binascii.hexlify(s))

#__CoNgrAtulAtionS__
