r = range(ord('a'),ord('z')+1)
r.extend(range(ord('A'),ord('Z')+1))
r.extend(range(ord('0'),ord('9')+1))
r.append(ord('!'))
r.append(ord(';'))
r.append(ord('='))
r.append(ord('.'))
r.append(ord('-'))
r.append(ord('+'))
r.append(ord('['))
r.append(ord(']'))
r.append(ord('@'))
r.append(ord('$'))
r.append(ord('*'))
r.append(ord('_'))

def check(v12):
    v6 = v12[0]-v12[1]
    v5 = v12[0]-v12[2]
    v10 = v12[2]-v12[3]
    if 6+v12[2]-2*v5+v6*3-v12[3]+1 != 0:
        return False
    elif 222*v5+51*v6-v12[2]+v12[3] != -8985:
        return False
    elif 100*v10-v5+-22*v6 != 1550:
        return False
    return True

for i in r:
    for j in r:
        for k in r:
            for l in r:
                v12 = [i,j,k,l]
                if check(v12):
                    print(''.join([chr(o) for o in v12]))

#en fait la seconde partie tout ajout à v17 doit être nul
#=> on obtient "Soul3d6e "
