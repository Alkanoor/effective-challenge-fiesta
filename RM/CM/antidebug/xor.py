import struct
import binascii

input = open('to_xor','rb').read()
output = open('xored','wb')

for i in range(0,len(input),4):
    a = struct.unpack('I',input[i:i+4])[0]
    print(binascii.hexlify(struct.pack('I',a^0x08048FC1)))
    output.write(struct.pack('I',a^0x08048FC1))

input = open('to_xor2','rb').read()
output = open('xored2','wb')

for i in input:
    output.write(chr(ord(i)^0xfc))
