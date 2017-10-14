class FollowI(gdb.Command):
    def __init__(self):
        super().__init__(
            'follow',
            gdb.COMMAND_BREAKPOINTS,
            gdb.COMPLETE_NONE,
            False
        )

    def invoke(self, arg, from_tty):
        if arg == '':
            gdb.write('Usage : follow [addr1, addr2, addr3][: output_file][: n_instructions_max]\n')
        else:
            split = arg.split(':')
            addrs = split[0]
            output = "tmp_out"
            n_instructions_max = -1
            if len(split)>1:
                output = split[1]
                if len(split)>2:
                    n_instructions_max = int(split[2])

            addrs_split = addrs.split(',')
            int_addrs = []
            for a in addrs_split:
                int_addrs.append(int(a.replace(' ',''),16))
                gdb.execute('break *'+hex(int_addrs[-1]))

            if len(int_addrs) == 0:
                print("No address specified ...")
                return

            try:
                f = open(output,'w')
            except:
                print("Output file cannot be opened ...")
                return

            if len(gdb.inferiors()[0].threads()) <= 0:
                gdb.write('No program is attached.\n')
            else:
                thread = gdb.inferiors()[0].threads()[0]
                n = 0
                N = 0
                while thread.is_valid() and (n_instructions_max<0 or n<n_instructions_max):
                    gdb.execute('continue', to_string=True)
                    frame = gdb.selected_frame()
                    arch = frame.architecture()
                    pc = gdb.selected_frame().pc()
                    if pc in int_addrs:
                        f.write(str(N) + '\n')
                        f.write(hex(pc) + '\n')
                        f.flush()
                        gdb.write(str(N) + '\n')
                        gdb.write(hex(pc) + '\n')
                        n += 1
                        N = 0
                    else:
                        N += 1

FollowI()
