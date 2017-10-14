from keystone import *

ks_arch = KS_ARCH_ARM
ks_mode = KS_MODE_THUMB

ks = Ks(ks_arch, ks_mode)

code = 'pop{r0, r4, pc}'

thumb_code, count = ks.asm(code)
thumb_code = ''.join(map(chr, thumb_code))

print(thumb_code, count)
