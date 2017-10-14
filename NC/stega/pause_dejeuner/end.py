#!/usr/bin/python


f = open('pause_dejeuner.mid', 'rb').read()

m = {}
n = {}
o = {}
p = {}
q = {}
for i in range(256):
    ref = chr(i)
    m[ref] = {}
    n[ref] = {}
    o[ref] = {}
    p[ref] = {}
    q[ref] = {}
    for j in range(5):
        m[ref][j] = {}
        n[ref][j] = {}
        o[ref][j] = {}
        p[ref][j] = {}
        q[ref][j] = {}
        for k in range(0, len(f)-j-4):
            if f[k] == ref:
                if m[ref][j].get(f[k+j+1]) is None:
                    m[ref][j][f[k+j+1]] = 1
                    n[ref][j][f[k+j+1]] = f[k+j+2]
                    o[ref][j][f[k+j+1]] = f[k+j+3]
                    p[ref][j][f[k+j+1]] = f[k+j+4]
                    q[ref][j][f[k+j+1]] = [k+j+1]
                else:
                    m[ref][j][f[k+j+1]] += 1
                    n[ref][j][f[k+j+1]] += f[k+j+2]
                    o[ref][j][f[k+j+1]] += f[k+j+3]
                    p[ref][j][f[k+j+1]] += f[k+j+4]
                    q[ref][j][f[k+j+1]].append(k+j+1)

for i in m:
    for j in m[i]:
        for k in m[i][j]:
            if m[i][j][k]==3:
                bad = False
                for a in n[i][j][k]:
                    if ord(a)<32 or ord(a)>=127:
                        bad = True
                if bad:
                    bad = False
                    for a in o[i][j][k]:
                        if ord(a)<32 or ord(a)>=127:
                            bad = True
                    if bad:
                        bad = False
                        for a in n[i][j][k]:
                            if ord(a)<32 or ord(a)>=127:
                                bad = True
                if not bad:
                    print i,j,k
                    print n[i][j][k], o[i][j][k], p[i][j][k]

                if n[i][j][k] == 'Mid' or o[i][j][k] == 'Mid' or p[i][j][k] == 'Mid':
                    print "FOUND!"
                    print(q[i][j][k])
                    exit()
