#!/bin/sh


arm-linux-gnueabi-as open_and_write.asm -o test.o
arm-linux-gnueabi-ld test.o -o test
echo "cat<<EOF>/home/user/q" &&
python -c 'import base64; a=base64.b64encode(open("test","rb").read()); print("\n".join([a[i:i+400] for i in range(0, len(a), 400)]))' &&
echo "EOF"
echo "base64 -d /home/user/q > /home/user/r"
echo "chmod u+x /home/user/r"
