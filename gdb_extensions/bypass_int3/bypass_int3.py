import re

class BypassInt3(gdb.Command):
    def __init__(self):
        super().__init__(
            'bypass_int3',
            gdb.COMMAND_BREAKPOINTS,
            gdb.COMPLETE_NONE,
            False
        )

    def invoke(self, arg, from_tty):
        if arg == '':
            gdb.write('Argument missing (address to go when bypassing)\n')
        else:
            pc_min_bound = 0x08040000
            pc_max_bound = 0x0804ffff
            dont_step = False
            int_block = False
            bp = []
            for a in gdb.breakpoints():
                bp.append(int(re.search('(0x[0-9a-fA-F]*)',a.location).group(1),16))
            if len(gdb.inferiors()[0].threads()) <= 0:
                gdb.write('No program is attached.\n')
            else:
                split = arg.split(' ')
                addr_to_go = int(split[0],16)
                f = -1
                if len(split)>1:
                    f = open(split[1],'w')
                thread = gdb.inferiors()[0].threads()[0]
                while thread.is_valid():
                    if not dont_step:
                        gdb.execute('si', to_string=True)
                    else:
                        dont_step = False

                    frame = gdb.selected_frame()
                    arch = frame.architecture()
                    pc = gdb.selected_frame().pc()
                    instruction = arch.disassemble(pc)

                    if pc>=0x80499cc:
                        gdb.execute('i r')

                    if pc in bp:
                        break

                    if instruction[0]['asm'].startswith('call'):
                        gdb.execute('break *'+hex(pc+instruction[0]['length']), to_string=True)
                        gdb.write("Breaking on "+hex(pc+instruction[0]['length']))
                        #if f != -1:
                        #    f.write('break *'+hex(pc+instruction[0]['length'])+'\n')
                        #    f.flush()
                    elif instruction[0]['asm'].startswith('ret') and int_block:
                        print("================================================")
                        print("Found ret at "+hex(pc))
                        int_block = False
                        gdb.execute('set $eip= '+hex(solved_address), to_string=True)
                        if f != -1:
                            f.write('break *'+hex(pc)+'\n')
                            f.write('continue\n')
                            f.write('set $eip= '+hex(solved_address)+'\n')
                            f.flush()
                        continue
                    elif instruction[0]['asm'].startswith('cmp') and not int_block:
                        print("Comparaison !")
                        tmp = instruction[0]['asm'].split('cmp ')[1]
                        a = tmp.split(',')
                        b = a[1]
                        a = a[0]
                        print("A : ")
                        o = a.split('ebp')
                        if len(o) > 1:
                            print("ebp"+o[1][:-1])
                            gdb.execute("x/4xw $ebp"+o[1][:-1])
                        else:
                            print(a)
                        print("B : ")
                        o = b.split('ebp')
                        if len(o) > 1:
                            print("ebp"+o[1][:-1])
                            gdb.execute("x/4xw $ebp"+o[1][:-1])
                        else:
                            print(b)
                    if not int_block:
                        print(instruction)

                    if (pc>pc_max_bound or pc<pc_min_bound):
                        print("CONTINUING ....")
                        gdb.execute('continue')
                        #if f != -1:
                        #    f.write('continue\n')
                        #    f.flush()
                        dont_step = True

                    if instruction[0]['asm'].startswith('int3'):
                        print("Found int 3 at "+hex(pc))
                        print(hex(addr_to_go))
                        gdb.execute('set $eip= '+hex(addr_to_go), to_string=True)
                        int_block = True
                        solved_address = pc+instruction[0]['length']
                        print("Solved address : "+hex(solved_address))
                        if f != -1:
                            f.write('break *'+hex(pc)+'\n')
                            f.write('continue\n')
                            f.write('set $eip='+hex(addr_to_go)+'\n')
                            f.flush()
BypassInt3()
