from keystone import *


code1 = b"ldm r0, {r4, r5, r6, r8, sb, sl, ip, sp, lr, pc}"
code2 = b"ldm r0!, {r4, r5, r6, r7, sl, ip, sp, pc} ^"
code1 = b"pop {r0, r1, r2, ip, sp, pc}"
code2 = b"pop {r0, r1, ip, pc}"

ks = Ks(KS_ARCH_ARM, KS_MODE_ARM)

encoding, count = ks.asm(code1)
print("%s = %s (number of statements: %u)" %(code1, encoding, count))
encoding, count = ks.asm(code2)
print("%s = %s (number of statements: %u)" %(code2, encoding, count))
