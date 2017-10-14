import math
import random

bloc_size = 512
offset = 0

content = open('file.None.0x84e13338.dat', 'rb').read()
print(len(content)//512)

def entropy(content, offset):
    t = []
    print_next = False
    cur = ""
    n = 0
    for i in range(offset, len(content), bloc_size):
        m = {}
        j = 0
        while j<bloc_size and i+j<len(content):
            if m.get(content[i+j]) is None:
                m[content[i+j]] = 1
            else:
                m[content[i+j]] += 1
            j += 1

        sum = 0.0
        for j in m:
            sum -= float(m[j])/float(bloc_size)*math.log(float(m[j])/float(bloc_size))/float(math.log(2))

        if float(sum)/8>=0.93:
            if not print_next:
                title = 'dump_'+hex(i)+"_"+str(float(sum)/8)+".tc"
            print(hex(i),float(sum)/8)
            t.append((i,float(sum)/8))
            print_next = True
            cur += content[i:i+bloc_size]
            n += 1
        elif print_next:
            print("=>",hex(i),float(sum)/8)
            print_next = False
            if n>300:
                print("WRITING !!!")
                print(title)
                open(title, 'wb').write(cur)
            cur = ""
            n = 0

    if print_next:
        print("=>",hex(i),float(sum)/8)
        if n>300:
            print("WRITING !!! ", n)
            print(title)
            open(title, 'wb').write(cur)

    return t

entropy(content, 0)
