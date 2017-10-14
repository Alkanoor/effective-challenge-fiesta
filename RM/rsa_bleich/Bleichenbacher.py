#https://github.com/duesee/bleichenbacher

from TypeChecking.Annotations import typecheck
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
import re
import socket
import binascii

class Oracle():
    def __init__(self):
        self.n = int('D68590FE1F678EF6C962A4B231177E044B6E769242D36229DD9CE3462ABC7EFD39568F56F1CE6A8C124ED2E0DC2F44611E2962CF6C2E3941FC23F44DAB153E52A266E9282EDE44EB3175BF8DCB399A0CCCA5041C0CCB03A3D896B29D503EE4607FBB853ED8EB5F2C21C485FA9743E356DF46C5EE093461BC8AD8FDC722F4682977C6FAA9B0143659B16AF373F7A499892D680F48EBC6A5276D7DEAEACABDC76B4F2AE8A9980FB01529D1F8D79A708E6765718F2436A70DE2C8E30691B23AEB76E0BF93001DE98C63252DAD3A01E27B544315A51A0EF0D0FBD2C84D36768924BCB5784DE6CB3AD48100E1FFD5F332CCAC82398661CA0A66F7469A0C36633DFA3B',16)
        self.k = 2048//8
        self.e = 0x10001

        HOST = 'localhost'
        HOST = 'challenge01.root-me.org'
        PORT = 51027
        self.LEN = 1024

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((HOST, PORT))

        self.ciphered = binascii.unhexlify('AB4BEEE8FE53773EBDF5BFF1A4C5364558CA986BA74BAD44ECC106694BEC44CD25681FAE106C81C7195231B4A2F6CA1E1E7853C6BBA2A18E4A9B8FDDD262ED27325F6F56045CE8593A2BD10AFFC8F42B16E43E4655EC328F4F34C8EE0269FC4F00B02B37FC7296A9B2E78D25E2D5777D83A1510B97F9F44896CAAB14078E6300740B3A25D2098D8042F5C6953BE70108A88040E48109F05E7E2923A481475293C5AD68F540754EA6CAB139BC803A91890383D2D1AF33D2C6216F4C68D0D0895B5E5B7B627AE36FBABEDB67ADC742FF911909D65E8B9B07D805F24B2ABD336F28C412A433F0FE2F19F066DFA8833AB2A2CCB9764D0CF1D754082D0BE770230EF6')

    @typecheck
    def get_n(self) -> int:
        """
        Returns the public RSA modulus.
        """
        return self.n

    @typecheck
    def get_e(self) -> int:
        """
        Returns the public RSA exponent.
        """
        return self.e

    @typecheck
    def get_k(self) -> int:
        """
        Returns the length of the RSA modulus in bytes.
        """
        return self.k

    def eavesdrop(self) -> bytes:
        return self.ciphered

    @typecheck
    def decrypt(self, ciphertext: bytes) -> bool:
        self.sock.send(ciphertext)
        tmp = self.sock.recv(self.LEN)

        if len(tmp.split(b'error'))<=1:
            print(tmp)
            print(ciphertext)
            return True

        return False
