import gensafeprime
import binascii
import random


def generate(bits=512):
    p = gensafeprime.generate(bits)
    while p%4 != 3:
        p = gensafeprime.generate(bits)
    q = gensafeprime.generate(bits)
    while q%4 != 3:
        q = gensafeprime.generate(bits)

    N = p*q
    return (N,p,q)


def encrypt(m, n):
    return ((pow(m,2)) % n)


def iterative_egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q,r = b//a,b%a
        m,n = x-u*q,y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    return b, x, y


def decrypt(p, q, c):
    g, x, y = iterative_egcd(p,q)

    n = p*q

    r = (pow(c,((p+1)//4),p))
    s = (pow(c,((q+1)//4),q))

    r1 = ((x*p*s)+(y*q*r))%n
    r2 = ((x*p*s)-(y*q*r))%n
    r3 = n-r1
    r4 = n-r2

    return r1, r2, r3, r4

def decrypt_random(p, q, c):
    g, x, y = iterative_egcd(p,q)

    n = p*q

    r = (pow(c,((p+1)//4),p))
    s = (pow(c,((q+1)//4),q))

    return ((random.randint(415687421635,78987987987564235487984)*p*s)+(y*q*r))%n


key = generate()
print(key)
N = key[0]

a = encrypt(N-1,N)
b = encrypt(N//2,N)

N_found = abs(iterative_egcd(a-pow(N-1,2),b-pow(N//2,2))[0])
print(N==N_found)

print(iterative_egcd(N,decrypt_random(key[1],key[2],2)-decrypt_random(key[1],key[2],2)))

import ast

expr="""
def foo():
   print("hello world")
"""
exec(expr)
foo()

exit()

m = int(binascii.hexlify("Bravo tu as trouve le message ! Le mot de passe est Gatorgokubisk"),16)
ciphered = encrypt(m,key[0])
print(ciphered)
print([hex(a) for a in decrypt(key[1],key[2],ciphered)])
