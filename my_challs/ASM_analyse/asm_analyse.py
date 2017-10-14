import sys

b = 32
if len(sys.argv)>1:
    b = int(sys.argv[1])
    if b != 16 and b != 32 and b != 64:
        print("Expecting 16, 32 or 64")
        exit()

try:
    cur_content = open('out_'+str(b)+'.txt').read()
except:
    pass

f = open('out_'+str(b)+'.txt','wb+')

instructions_2_mixed = ['mov','xor','add']
instructions_2_register = ['xchg']
instructions_1_stack_mixed = ['push']
instructions_1_stack_register = ['pop']

registers = {'32':['eax','ebx','ecx','edx','edi','esi'],'64':['rax','rbx','rcx','rdx','rdi','rsi']}

import subprocess

print(dir(subprocess))
tmp = open('tmp','w')
tmp.write('BITS '+str(b)+'\n')
tmp.write('shr eax\n')
tmp.write('a:\n')
tmp.write('mov eax,34\n')
tmp.close()
ps = subprocess.Popen(['nasm','tmp','-o','tmp.out'],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
ps.communicate()

tmp_out = open('tmp.out').read()

import binascii

print(binascii.hexlify(tmp_out))
