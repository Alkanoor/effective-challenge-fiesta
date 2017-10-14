#!/usr/bin/python

from urllib import urlencode
import StringIO
import certifi
import pycurl
import sys
import re
import io


if len(sys.argv)<4 or (sys.argv[1] != "send" and sys.argv[1] != "load"):
    print "Usage : "+sys.argv[0]+" [send|load] [file to read/write from] [cookie]"
    exit()

def clear(o):
    o.truncate(0)
    o.seek(0)

body_buffer = StringIO.StringIO()
header_buffer = StringIO.StringIO()

c = pycurl.Curl()
c.setopt(c.CAINFO, certifi.where())
c.setopt(c.SSL_VERIFYHOST, 0)
c.setopt(c.WRITEFUNCTION, body_buffer.write)
c.setopt(c.HEADERFUNCTION, header_buffer.write)

c.setopt(c.COOKIE, sys.argv[3])


if sys.argv[1] == "send":
    content = open(sys.argv[2], 'rb').read()

    c.setopt(c.URL, 'https://www.newbiecontest.org/epreuves/prog/verifprogcrc.php?solution='+content)
    c.perform()

    received = body_buffer.getvalue()
    print(received)
    open('final_get.html','wb').write(received)

elif sys.argv[1] == "load":
    c.setopt(c.URL, 'https://www.newbiecontest.org/epreuves/prog/progcrc.php')
    c.perform()

    received = body_buffer.getvalue()
    print(received)
    f = received.split('\n')
    f = [_.split(' ') for _ in f][2:]

    h = 20
    w = 20

    T = [[0 for i in range(w)] for j in range(h)]
    for i in range(h):
        for j in range(w):
            try:
                T[i][j] = int(f[i][j][:2],16)
            except:
                pass

    with open(sys.argv[2], 'w') as g:
        g.write(str(h)+" "+str(w)+"\n")
        for i in range(len(T)):
            for j in range(len(T[i])):
                g.write(str(T[i][j])+" ")
            g.write("\n")
        g.flush()
        g.close()

else:
    print "Please select send or load as option"
