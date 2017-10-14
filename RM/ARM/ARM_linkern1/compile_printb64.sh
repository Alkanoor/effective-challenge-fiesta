#!/bin/sh


arm-linux-gnueabi-as $1.asm -o $1.o
arm-linux-gnueabi-ld $1.o -o $1
python -c 'import base64; a=base64.b64encode(open("'$1'","rb").read()); print("\n".join([a[i:i+400] for i in range(0, len(a), 400)]))'
