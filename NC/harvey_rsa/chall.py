#!/usr/bin/python
#encoding:utf8
import random
import sys
from binascii import hexlify, unhexlify

def iterative_egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q,r = b//a,b%a
        m,n = x-u*q,y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    return b, x, y

def GF2_add(p1, p2):
    assert(p1>=0 and p2>=0)
    return p1 ^ p2

def GF2_mod(p, mod):
    assert(p>=0 and mod>0)
    while p.bit_length() >= mod.bit_length():
        mask = mod << (p.bit_length() - mod.bit_length())
        p ^= mask
    return p

def GF2_mul_mod(p1, p2, mod):
    assert(p1>=0 and p2>=0 and mod>0)
    r=0
    while p2:
        if p2 & 1:
            r ^= p1
        p2 >>= 1
        p1 = GF2_mod(p1<<1, mod)
    return r

def GF2_pow_mod(b, e, mod):
    assert(b>=0 and e>=0 and mod>0)
    r=1
    while e:
        if e&1:
            r = GF2_mul_mod(r, b, mod)
        e >>= 1
        b = GF2_mul_mod(b,b,mod)
    return r

for i in range(2,60):
    N = 0
    P = 0
    for j in range(1,102):
        N_prev = N
        for k in range(j,102):
            if GF2_pow_mod(GF2_pow_mod(i,j,103),k,103) == i:
                N+=1
                #print(i,j,k)
                #print(GF2_mul_mod(j,k,101))
        if N>N_prev:
            P += 1
    print(i,N,P)
#
# print(GF2_pow_mod(GF2_pow_mod(100,13,10000),7,10000))
# print(GF2_pow_mod(GF2_pow_mod(100,7,10000),13,10000))
# print(GF2_pow_mod(100,7*13,10000))
# print(GF2_mul_mod(9,6+32+64,789789))
# exit()
# p = 12481226043768709217244347707229502286826253570951482357303669658828541306386896214853253626285981398564918837469681943919320610891491820173584130878829963
# q = 11064978895870448975499572664206464106237617631286388794228551842420909113658939722798712785118504747087298589761988392316915764974915766033535187161970679
# N = GF2_mul_mod(p,q,2**1500)
# print(N)
# print(GF2_mul_mod(p,q,N))
# E = 6553
#
# test_plain = random.randrange(2**1024)
# test_crypt = GF2_pow_mod(test_plain, E, N)
# test_plain2 = random.randrange(2**1024)
# test_crypt2 = GF2_pow_mod(test_plain2, E, N)
# print(test_plain^test_plain2)
# print(test_crypt^test_crypt2)
# exit()

if __name__=="__main__":
    if len(sys.argv)!=2:
        print ("Usage: {0} exposant_privé".format(sys.argv[0]))
        sys.exit(1)
    D = int(sys.argv[1],0)
    N = 231002291543555016818569199325004102033150445385414455365880736176436715311790663130589862191084808106664722172105531887027184495017140783502576089624623090612010946552911266876786591303954740526520748757324542859056473246482362113968367791176213289397973534046005478174177408900797351038135732809112135056071
    E = 65532
    test_plain = random.randrange(2**1024)
    test_crypt = GF2_pow_mod(test_plain, E, N)
    D = 65533
    while GF2_pow_mod(test_crypt, D, N)!=test_plain:
        D += 1
        print(D)
    print("ENDED!! ")
    print(D)

    if GF2_pow_mod(test_crypt, D, N)==test_plain:
        flag = 3084449846433041813390375663058703285782448134840024007803494551180465048150640197025779798034586128810372902144370282944067512576975973977099499869946999914888177281161149730177343199310024653678751046701545038089863997906852127878655263416175563754210990106963126850755139552152622891343746619023468031658
        flag = GF2_pow_mod(flag,D,N)
        flag = unhexlify(hex(flag)[2:].strip("L").zfill(256)).decode()
        flag = flag[:ord(flag[-1])]
        print (flag)
    else:
        print ("Non.")
