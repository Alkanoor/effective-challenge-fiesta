import io
import re
import numpy as np
from PIL import Image


sizes = {}
cur = {}
for i in range(256):
    sizes[i] = np.array([])
    cur[i] = 0

def transform_pixel(t):
    if t[0]==t[1] and t[1]==t[2]:
        return (True,t[0]&1)
    else:
        return (False,t[1]&1)

img = Image.open('RTFM.png')
s = img.size
m = {}
comb = [[1],[2],[3],[1,2],[2,3],[1,3],[1,2,3]]
raw = [[] for _ in range(len(comb))]

res = ''
for j in range(s[1]):
    for i in range(s[0]):
        t = img.getpixel((i,j))

        for k in range(len(comb)):
            for l in comb[k]:
                raw[k].append(t[l-1])

        tmp = transform_pixel(t)
        # for k in range(256):
        #     if t[0] == k:
        #         sizes[k] = np.append(sizes[k],cur[k])
        #         cur[k] = 0
        #     else:
        #         cur[k] += 1
        if not tmp[0]:
            res += str(tmp[1])
            if m.get(chr(tmp[1])) is not None:
                m[chr(tmp[1])] += 1
            else:
                m[chr(tmp[1])] = 1

good = [a for a in range(ord('a'),ord('z')+1)]
good.extend([a for a in range(ord('A'),ord('Z')+1)])
good.append(ord('!'))
good.append(ord('_'))
good.append(ord(' '))
good.append(ord('.'))
good.append(ord(','))
good.append(0xd)
good.append(0xa)
good = range(32,128)


for c in range(len(raw)):
    max_cool = {}
    M = -1
    for length in range(2,1000):
        for i in range(len(raw[c])-1000):
            cur = 0
            s = ''
            while i+cur*length<len(raw[c]) and raw[c][i+cur*length] in good:
                s += chr(raw[c][i+cur*length])
                cur += 1
            if cur>M:
                M = cur
                max_cool[c] = (cur,s,i,length)
                print("New max "+s)
                print(cur,i,length)
    print(max_cool)

exit()
# for i in range(256):
#     print(i,sizes[i].mean(),sizes[i].std())
# exit()

print(len(m))
print(sorted(m.items()))
print(len(res))
res = res.replace('0',' ').replace('1','!')
exit()
print(res)


for i in range(41*3):
    print(res[i*43*3:(i+1)*43*3])

print("======================")
for i in range(41*9):
    print(res[i*43:(i+1)*43])
exit()

difs = np.array([])
for offset in range(1,1000):
    dist = 0
    for lin in range(1,len(res)//offset):
        for j in range(offset):
            if lin+j<len(res):
                if res[lin*offset+j] != res[(lin-1)*offset+j]:
                    dist += 1
    difs = np.append(difs,dist)
    print(difs)

print(difs)
print(difs.mean())
print(difs.std())
print(difs.min())
