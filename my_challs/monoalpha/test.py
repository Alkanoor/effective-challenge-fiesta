import sys
from random import *
from cryptanalysis import *


def craft_random_map():
    v = [i for i in range(36)]
    shuffle(v)
    chars = [chr(i) for i in range(ord('A'),ord('Z')+1)]
    chars.extend([chr(i) for i in range(ord('0'),ord('9')+1)])
    grid = {}
    for i in range(36):
        grid[chars[i]] = chars[v[i]]
    return grid

def apply(m,map):
    res = ''
    for i in m:
        res += map[i]
    return res

message = clean_text(open(sys.argv[1]).read())
random_map = craft_random_map()
ciphered = apply(message,random_map)

print(random_map)
print(ciphered)

def f(m):
    print(m)

itere(ciphered,count(ciphered),get_reference(),10000,f)
