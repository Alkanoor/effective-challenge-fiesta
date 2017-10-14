import random


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

def count(m):
    res = {}
    for i in m:
        if res.get(i) is not None:
            res[i] += 1
        else:
            res[i] = 1
    return res

def get_reference():
    ref = clean_text(open('test.py').read())
    res = {}
    r = float(len(ref)-3)
    for i in range(0,len(ref)-3):
        quad = ref[i:i+4]
        if res.get(quad) is not None:
            res[quad] += 1.0/r
        else:
            res[quad] = 1.0/r
    return res

def measure(m,reference):
    s = 0
    for i in range(0,len(m)-3):
        quad = m[i:i+4]
        if reference.get(quad) is not None:
            s += reference[quad]
    return s

def itere(m,count,reference,n_iterations,callback):
    count_items = count.items()
    last = -1
    prev = 0
    for i in range(n_iterations):
        measures = {}
        limit = 100
        v1 = range(len(count_items))
        v2 = range(len(count_items))
        random.shuffle(v1)
        random.shuffle(v2)
        for i in v1[:limit]:
            for j in v2[:limit]:
                if count_items[i][0] != count_items[j][0]:
                    tmp = m.replace(count_items[i][0],'@').replace(count_items[j][0],count_items[i][0]).replace('@',count_items[j][0])
                    measures[count_items[i][0]+count_items[j][0]] = measure(tmp,reference)

        items = measures.items()
        s = 0.0
        for i in items:
            s += i[1]*i[1]
        if s<=0.00001:
            s = 1
        #print("Giving => "+str(s))

        r = random.random()
        c = 0
        cur = 0
        while c < r and cur < len(items):
            c += items[cur][1]*items[cur][1]/s
            cur += 1
        cur -= 1
        item = items[cur]

        if item[1]>last or prev>5:
            prev = 0
            last = item[1]
            print("cur chosen : "+str(cur)+" "+item[0]+" with "+str(item[1]))

            now = m.replace(item[0][0],'@').replace(item[0][1],item[0][0]).replace('@',item[0][1])
            callback(now)
            m = now
        else:
            prev += 1
