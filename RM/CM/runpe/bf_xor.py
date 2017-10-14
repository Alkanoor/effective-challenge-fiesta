import binascii
import re
import binascii
import numpy as np


def reverse(msg):
	r = ''
	for i in msg:
		t = ord(i)-0xe-0x21
		if t<32:
			t += 0x5e
		r += chr(t)
	return r


content = open('to_xor','rb').read().split('\x00')
content_bis = []
for c in content:
    if len(c)>0:
        content_bis.append(c)
        print(c)
        print(reverse(c))

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

def column(msgs, col, length):
    r = []
    for m in msgs:
        for j in range(col,len(m),length):
            r.append(m[j])
    return r

base = column(content_bis,0,1)
print(coincidence(base))
exit()

alls = []
for i in range(3,15):
    moy = np.array([])
    for j in range(i):
        s = column(content_bis,j,i)
        print(s)
        moy = np.append(moy,coincidence(s))
    print(moy)
    print(moy.mean())
    print(moy.std())

exit()
print(content_bis)

for i in range(256):
    for c in content_bis:
        print(''.join([chr(i^ord(d)) for d in c]))
    print()
