import socket
import os
import sys
import hashlib
import struct
import gmpy
from Crypto.Cipher import AES

import ecc

def create_server(host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind((host, port))
        sock.listen(5)
    except:
        print("[-] Failed to bind to %s:%d" % (host, port))
        sys.exit(1)
    return sock

def connect_to_serv(host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((host, port))
    except:
        print("[-] Failed to connect to server")
        sys.exit(1)
    return sock


def sendmsg(sock, msg):
    sock.send(struct.pack('!H', len(msg)) + msg)


def recvmsg(sock):
    size = sock.recv(2)
    if size == None or len(size) < 2:
        return None

    (size,) = struct.unpack('!H', size)
    return sock.recv(size)


def bits_to_int(bits):
    return int.from_bytes(bits, 'big')


def int_to_bits(n):
    l = gmpy.mpz(n).bit_length()
    if l%8 == 0:
        l = int(l/8)
    else:
        l = int(l/8) + 1

    return n.to_bytes(l, 'big')


def point_to_bits(p):
    if p.isInf():
        return struct.pack('!H', 0)

    x = int_to_bits(p.x)
    y = int_to_bits(p.y)

    msg  = struct.pack('!H', len(x)) + x
    msg += struct.pack('!H', len(y)) + y

    return msg


def bits_to_point(p):
    (x_size,) = struct.unpack('!H', p[:2])
    if x_size == 0:
        return ecc.PointInf()

    x = bits_to_int(p[2:x_size+2])
    y = bits_to_int(p[x_size+4:])

    return ecc.Point(x, y)


def gen_aes_key(key):
    return hashlib.sha256(int_to_bits(key)).digest()[:16]


def unpad(msg):
    b = msg[-1]
    return msg[:-b]


def pad(msg):
    l = 16 - len(msg)%16
    return msg + chr(l)*l


def decrypt(key, msg):
    (iv, cipher) = (msg[:16], msg[16:])
    aes = AES.new(key, mode=AES.MODE_CBC, IV=iv)
    return unpad(aes.decrypt(cipher))


def encrypt(key, msg):
    iv = os.urandom(16)
    aes = AES.new(key, mode=AES.MODE_CBC, IV=iv)
    return iv + aes.encrypt(pad(msg))


def key_exchange(sock, curve, P):
    l = gmpy.mpz(curve.p).bit_length()

    r = bits_to_int(os.urandom(int(l/8)+1)) % curve.p
    print("[+] r = %d" % r)

    A = curve.mul(r, P)

    print("[+] rP = %s" % A)

    sendmsg(sock, point_to_bits(A))

    B = bits_to_point(recvmsg(sock))
    print("[+] B = %s" % B)

    K = curve.mul(r, B)
    print("[+] K = %s" % K)

    return K
