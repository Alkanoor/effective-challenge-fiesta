#!/usr/bin/python3

from common import *
import config
import ecc

def send_flag(sock, flag, key):
    for l in flag.split("\n"):
        sendmsg(sock, encrypt(key, l))

FLAG = open("flag.txt").read()

curve = ecc.Curve(config.A, config.B, config.N)
sock = create_server(config.HOST, config.PORT)
print("[+] Listenning...")

while True:
    (clisock, cliaddr) = sock.accept()

    key = key_exchange(clisock, curve, config.P)
    aes_key = gen_aes_key(key.x)
    send_flag(clisock, FLAG, aes_key)

    clisock.close()
