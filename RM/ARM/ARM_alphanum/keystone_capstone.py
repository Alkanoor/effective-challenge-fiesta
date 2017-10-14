from keystone import *
from capstone import *
from pwn import *

# code1 = b"ldm r0, {r4, r5, r6, r8, sb, sl, ip, sp, lr, pc}"
# code2 = b"ldm r0!, {r4, r5, r6, r7, sl, ip, sp, pc} ^"
# code1 = b"pop {r0, r1, r2, ip, sp, pc}"
# code2 = b"pop {r0, r1, ip, pc}"
#
# ks = Ks(KS_ARCH_ARM, KS_MODE_ARM)
#
# encoding, count = ks.asm(code1)
# print("%s = %s (number of statements: %u)" %(code1, encoding, count))
# encoding, count = ks.asm(code2)
# print("%s = %s (number of statements: %u)" %(code2, encoding, count))

from capstone import *

CODE = "k0xBXp9RV01RVp7RB0GBtp3RF0cB7pqBI01RH0IBEPCRx07BlPIB405BDpCR3P8BqpyBRP5Bd0eBypRRbpsBZpRBppXRkpSRz0SRtp4R4pOR8pOB4pWU0pWEVPWBVPWRV0GRz0CRV0CRV0CRsEOPW0GRV0GRIP3RbPER5CDPW0GRoP3RVPDEVPWBsEDPsEDPsEDPsEDPhP7RVPDUsEDPV0GRHP3RWPER5CDPW0GRoP3RVPDEVPWBsEDPsEDPsEDPiP3RbP5BVPDEVPWBsEDPVP3RVP5BVPDEVPWBsEDPoP3RoP5BVPDEVPWBsEDPsEDPsEDPGP7RQP5RVPDUsEDPsEDPVpWR7GGP7gGPtVCPwpDR7tOP7d4Pq04BK0WU5tGPKMWUcj9PK0FU5dFP5tGP2byRIBLKLHFUfaFPlOKRfskOToxaRXpFTLTpIPcvUQLPSyuJobTZvkEwTAYODosDrMbPDoRKpoPkROdoAfSEplrNw0"

md = Cs(CS_ARCH_ARM, CS_MODE_ARM)
for i in md.disasm(CODE, 0x1000):
     print("0x%x:\t%s\t%s" %(i.address, i.mnemonic, i.op_str))
