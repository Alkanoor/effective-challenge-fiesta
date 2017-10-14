#!/bin/python2

import gensafeprime
import random
import fractions

def generate(bits=512):
    p = gensafeprime.generate(bits)
    q = gensafeprime.generate(bits)

    N = p*q

    e = random.randint(2,N-1)

    while fractions.gcd(e,N) != 1:
        e = random.randint(2,N-1)

    r1 = random.randint(2,N-1)
    r2 = random.randint(2,N-1)

    a1 = pow(e,r1*(p-1),N)
    a2 = pow(e,r2*(q-1),N)

    privkey = {'p': p, 'q': q, 'r1': r1, 'r2': r2}
    pubkey = {'N': N, 'a1': a1, 'a2': a2}

    return (privkey,pubkey)


def encrypt(pubkey,message):
    N = pubkey['N']
    a1 = pubkey['a1']
    a2 = pubkey['a2']

    l = len(hex(N)[2:])-1
    messagehex = message.encode('hex')

    blocks = [ int(messagehex[i : i+l],16) for i in range(0, len(messagehex), l) ]
    res = []

    for m in blocks:
        s1 = random.randint(2,N-1)
        s2 = random.randint(2,N-1)

        d1 = pow(a1,s1,N)
        d2 = pow(a2,s2,N)

        c1 = (m*d1)%N
        c2 = (m*d2)%N

        res.append((c1,c2))

    return res
