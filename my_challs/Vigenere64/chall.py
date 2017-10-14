import random
from base64 import b64encode, b64decode

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789+/'
chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'

def shift(char, key, rev = False):
    if not char in chars:
        return char
    if rev:
        return chars[(chars.index(char) - chars.index(key)) % len(chars)]
    else:
        return chars[(chars.index(char) + chars.index(key)) % len(chars)]

def encrypt(message, key):
    encrypted = b64encode(message.encode('ascii')).decode('ascii')
    return ''.join([shift(encrypted[i], key[i % len(key)]) for i in range(len(encrypted))])

def decrypt(encrypted, key):
    encrypted = ''.join([shift(encrypted[i], key[i % len(key)], True) for i in range(len(encrypted))])
    return b64decode(encrypted)

def decrypt_no_b64(encrypted, key):
    encrypted = ''.join([shift(encrypted[i], key[i % len(key)], True) for i in range(len(encrypted))])
    return encrypted

# msg = "Tu pensais que ca commencerait par le mot de passe est ? Mais non ! Bien joue a toi ! Le mot de passe est lemotdepassenestpaslemotdepasseest"
# print(encrypt(msg,"jD8+Wf3axq3Z0WS"))
# exit()

m = "4KQeylMINg8CQITUgSS23teRCtWhxo4xU0rRPwWe/g13uFEoXogk1o6Xy6qy/JBxyVL6KBEN8ZODWSD/7pbfFtRUekkFWUrN/gaZUvI2q1EwZMDXiDrDyGX/+6MevlL6Nw8MQMmDcTLKn9LWFNWovY4zUVjSQwqPTQFGq6QoXsUm337c16bF/5RjyWH="
coincidence = ""

def extract_column(msg, col, l):
    e = ''
    for i in range(col,len(msg),l):
        e += msg[i]
    return e

forbidden = [{} for _ in range(4)]
def create_table():
    t = []
    for i in range(4):
        t.append({})
        for j in range(len(chars)):
            t[i][chars[j]] = False
    for j in range(10,128):
        m = chr(j)*3
        m_e = b64encode(m.encode('ascii'))
        for k in range(4):
            t[k][m_e[k]] = True
    for i in range(4):
        for j in t[i]:
            if t[i][j] == False:
                forbidden[i][j] = True

create_table()
# for i in range(4):
#     print(forbidden[i])

key_length = 15 #determine a l'oeil
key = ''
for i in range(key_length):
    bad = {}
    for j in range(len(chars)):
        column = extract_column(m,i,key_length)
        column_deciphered = decrypt_no_b64(column,chars[j])
        cur = i
        n = 0
        for c in column_deciphered:
            if c in forbidden[cur%4]:
                n+=1
            cur += key_length
        if bad.get(n) is not None:
            bad[n].append(j)
        else:
            bad[n] = [j]

    key += chars[bad[0][0]]

key = "jD8+Wf3axq3Z0WS"

index = 116
target = 'se'
r_prev = range(64)

c = decrypt(m,key)
print(c)

k = 0
ref = c[index]
while ref == c[index]:
    prev = key
    key = key[:k]+chars[random.randint(0,len(chars)-1)]+key[k+1:]
    c = decrypt(m,key)
    k += 1
    key = prev

print(k)

import binascii

i = 0
cur = index
for j in r_prev:
    i = 0
    while (c[cur-1] != 's' or c[cur] != target[cur-index]) and i<len(chars):
        key2 = key[:k-1]+chars[j]+chars[i]+key[k+1:]
        c = decrypt(m,key2)
        i += 1
    if i<64:
        print(key2)
        print(c[108:])
    key2 = 'a'*15
    c = decrypt(m,key2)
