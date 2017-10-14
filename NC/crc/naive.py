import random
from crc64 import *


f = open('input', 'r').readlines()
f = [_.split(' ') for _ in f]

h = len(f)
w = len(f[0])

T = [[0 for i in range(w)] for j in range(h)]
for i in range(h):
    for j in range(w):
        try:
            T[i][j] = int(f[i][j][:2],16)
        except:
            pass

with open('input_c', 'w') as g:
    g.write(str(h)+" "+str(w)+"\n")
    for i in range(len(T)):
        for j in range(len(T[i])):
            g.write(str(T[i][j])+" ")
        g.write("\n")
    g.flush()
    g.close()

print(f)
print(w,h)
print(T)

def create_random_path(n=37):
    return [random.randint(0,1) for _ in range(n)]

import time

st = time.time()

found = False
while not found:
    s = create_random_path(37)
    t = [0 for _ in range(37)]
    cur = (0,0)
    n = 0
    for i in s:
        if (i == 0 and cur[0]+1<h) or cur[1]+1>=w:
            cur = (cur[0]+1, cur[1])
            t[n] = T[cur[0]][cur[1]]
        else:
            cur = (cur[0], cur[1]+1)
            t[n] = T[cur[0]][cur[1]]
        n += 1

    found = CRC64(t)==0x4242424242424242

print(t)
print(time.time()-st)
