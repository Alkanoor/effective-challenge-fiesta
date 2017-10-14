from random import *

letters = "ADFGVX"

def clean_text(msg):
    ret = ''
    for i in msg:
        if ord(i)>=ord('a') and ord(i)<=ord('z'):
            ret += chr(ord(i)-ord('a')+ord('A'))
        elif ord(i)>=ord('A') and ord(i)<=ord('Z'):
            ret += i
        elif ord(i)>=ord('0') and ord(i)<=ord('9'):
            ret += i
    return ret

def craft_random_grid(rand=True):
    v = [i for i in range(36)]
    if rand:
        shuffle(v)
    grid = {}
    inv_grid = {}
    for i in range(26):
        grid[chr(i+ord('A'))] = letters[v[i]//6]+letters[v[i]%6]
        inv_grid[letters[v[i]//6]+letters[v[i]%6]] = chr(i+ord('A'))
    for i in range(10):
        grid[chr(i+ord('0'))] = letters[v[i+26]//6]+letters[v[i+26]%6]
        inv_grid[letters[v[i+26]//6]+letters[v[i+26]%6]] = chr(i+ord('0'))
    return grid,inv_grid

def transpose(msg, l):
    ret = ''
    for i in range(l):
        for j in range(i,len(msg),l):
            ret += msg[j]
    return ret

def cipher(key, grid, msg, horizontal=True):
    tmp = ''
    for i in msg:
        tmp += grid[i]

    if not horizontal:
        tmp = transpose(tmp,len(key))

    tmp_array = ['']*len(key)
    final_array = []
    for i in range(0,len(tmp),len(key)):
        for j in range(len(key)):
            if i+j<len(tmp):
                tmp_array[key[j]] = tmp[i+j]
            else:
                tmp_array[key[j]] = ''
        final_array.extend(tmp_array)
    return ''.join(final_array)

def decipher(key, inv_grid, msg, horizontal=True):
    tmp_array = ['']*len(key)
    final_array = []
    for i in range(0,len(msg),len(key)):
        for j in range(len(key)):
            if i+key[j]<len(msg):
                tmp_array[j] = msg[i+key[j]]
            else:
                tmp_array[j] = ''
        final_array.extend(tmp_array)
    unpermuted = ''.join(final_array)

    if not horizontal:
        unpermuted = transpose(unpermuted,len(key))

    ret = ''
    for i in range(0,len(unpermuted),2):
        ret += inv_grid[unpermuted[i:i+2]]
    return ret

def count(msg):
    m = {}
    for i in msg:
        if m.get(i) is not None:
            m[i] += 1
        else:
            m[i] = 1
    return m

def count_bigrams(msg):
    m = {}
    for i in range(0,len(msg),2):
        if m.get(msg[i:i+2]) is not None:
            m[msg[i:i+2]] += 1
        else:
            m[msg[i:i+2]] = 1
    return m

def coincidence(msg):
    s = 0
    m = count(msg)
    orig = float(len(msg))
    for i in m:
        s += float(m[i])*float(m[i]-1)/orig/(orig-1)
    return s

def coincidence_bigrams(msg):
    s = 0
    m = count_bigrams(msg)
    orig = float(len(msg)//2)
    for i in m:
        s += float(m[i])*float(m[i]-1)/orig/(orig-1)
    return s
