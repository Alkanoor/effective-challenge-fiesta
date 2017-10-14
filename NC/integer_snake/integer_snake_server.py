#!/usr/bin/python

import io
import re
import time
import socket
import pycurl
import certifi
import StringIO
from urllib import urlencode


def clear(o):
    o.truncate(0)
    o.seek(0)

body_buffer = StringIO.StringIO()
header_buffer = StringIO.StringIO()


c1 = pycurl.Curl()
c1.setopt(c1.CAINFO, certifi.where())
c1.setopt(c1.SSL_VERIFYHOST, 0)
c1.setopt(c1.WRITEFUNCTION, body_buffer.write)
c1.setopt(c1.HEADERFUNCTION, header_buffer.write)

c1.setopt(c1.COOKIE, 'SMFCookie89=a%3A4%3A%7Bi%3A0%3Bs%3A5%3A%2263127%22%3Bi%3A1%3Bs%3A40%3A%228f76ee4e57b4cb44bc9082e26c5dd7be554dbd81%22%3Bi%3A2%3Bi%3A1625593163%3Bi%3A3%3Bi%3A0%3B%7D; PHPSESSID=f0dfd2ecb5b8fd2fa2ea02606d7ade53')
c1.setopt(c1.URL, "https://www.newbiecontest.org/epreuves/prog/progintegersnake.php")


c2 = pycurl.Curl()
c2.setopt(c2.CAINFO, certifi.where())
c2.setopt(c2.SSL_VERIFYHOST, 0)
c2.setopt(c2.WRITEFUNCTION, body_buffer.write)
c2.setopt(c2.HEADERFUNCTION, header_buffer.write)

c2.setopt(c2.COOKIE, 'SMFCookie89=a%3A4%3A%7Bi%3A0%3Bs%3A5%3A%2263127%22%3Bi%3A1%3Bs%3A40%3A%228f76ee4e57b4cb44bc9082e26c5dd7be554dbd81%22%3Bi%3A2%3Bi%3A1625593163%3Bi%3A3%3Bi%3A0%3B%7D; PHPSESSID=f0dfd2ecb5b8fd2fa2ea02606d7ade53')


HOST = ''
PORT = 8888
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((HOST, PORT))
except socket.error as msg:
    exit(-1)

s.listen(10)
conn, addr = s.accept()

while True:
    time.sleep(3)
    
    t = conn.recv(10)
    while t[0] != 'a':
	  t = conn.recv(10)
    c1.perform()
    
    body = body_buffer.getvalue()
    header = header_buffer.getvalue()

    clear(body_buffer)
    clear(header_buffer)
    
    try:
      seed1 = re.search('seed1=([0-9]*)\n', body).group(1)
      seed2 = re.search('seed2=([0-9]*)\n', body).group(1)
      seed3 = re.search('seed3=([0-9]*)\n', body).group(1)
    except:
	  print("Not new seed ...")
	  pass
    
    print("New seed : ", seed1, seed2, seed3)
    
    conn.send(str(seed1)+" "+str(seed2)+" "+str(seed3))
    
    send_back = conn.recv(10)
    print("Received : ["+send_back+"]")
    if send_back[0] == '1':
        to_send_back = conn.recv(60000)

        url = "https://www.newbiecontest.org/epreuves/prog/verifprintegersnake.php?path="+to_send_back
        c2.setopt(c2.URL, url)
        c2.perform()
        
        body = body_buffer.getvalue()
        header = header_buffer.getvalue()

        clear(body_buffer)
        clear(header_buffer)
        
        print(body)
        print(header)
		
        with open("out_python.txt", "w+") as f:
		   f.write("https://www.newbiecontest.org/epreuves/prog/progintegersnakereplay.php?seed1="+str(seed1)+"&seed2="+str(seed2)+"&seed3="+str(seed3)+"&path="+to_send_back)
		
        exit()
    else:
        print("Not sent because bad")
