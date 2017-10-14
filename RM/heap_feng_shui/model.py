
class Model:

    User = 0
    Thread = 1
    Unknown = 2
    states = {User:"User", Thread:"Thread", Unknown:"Unknown"}
    begin_markers = ["1. Create user", "1. Create thread"]
    end_markers = ["6. Quit", "7. Loggout", ""]

    def __init__(self, p, timeout=1, print_header=True, wait=False):
        self.program = p
        self.state = Model.Unknown
        self.timeout = timeout
        self.print_header = print_header
        self.wait = wait
        self.instructions = []

    def recv_and_state(self, print_recv=True):
        if self.print_header:
            print "=================== New step ==================="
        if self.wait:
            tmp = self.program.recvuntil('> ', timeout=30)
        else:
            tmp = self.program.recvuntil('> ', timeout=self.timeout)
        if print_recv:
            print tmp
        split = tmp.split('\n')
        if len(split)<2:
            self.state = Model.Unknown
        else:
            for i in range(len(split)):
                for j in range(len(Model.end_markers)):
                    if Model.end_markers[j] != "" and Model.end_markers[j] in split[len(split)-1-i]:
                        self.state = j
                        if self.state != Model.Unknown:
                            tmp = tmp.split(Model.begin_markers[self.state])[0]
                        else:
                            tmp = ""
                        return (tmp, Model.states[self.state])
        self.state = Model.Unknown
        return (None, Model.states[self.state])

    def go_until_cur(self, print_recv=True):
        tmp = self.recv_and_state(print_recv)
        prev = tmp
        while tmp[0] is not None:
            prev = (tmp[0], tmp[1])
            tmp = self.recv_and_state(print_recv)
        return prev

    def add_user(self, u, p):
        self.program.sendline('1')
        self.program.sendline(u)
        self.program.sendline(p)
        self.instructions.append('1')
        self.instructions.append(u)
        self.instructions.append(p)
        return self.recv_and_state()

    def login(self, u, p):
        self.program.sendline('2')
        self.program.sendline(u)
        self.program.sendline(p)
        self.instructions.append('2')
        self.instructions.append(u)
        self.instructions.append(p)
        return self.recv_and_state()

    def change_password(self, u, p1, p2):
        self.program.sendline('3')
        self.program.sendline(u)
        self.program.sendline(p1)
        self.program.sendline(p2)
        self.instructions.append('3')
        self.instructions.append(u)
        self.instructions.append(p1)
        self.instructions.append(p2)
        return self.recv_and_state()

    def delete_user(self, u):
        self.program.sendline('4')
        self.program.sendline(u)
        self.instructions.append('4')
        self.instructions.append(u)
        return self.recv_and_state()

    def list_users(self):
        self.program.sendline('5')
        self.instructions.append('5')
        return self.recv_and_state()

    def quit(self):
        self.program.sendline('6')
        self.instructions.append('6')
        return self.recv_and_state()

    def create_thread(self, t):
        self.program.sendline('1')
        self.program.sendline(t)
        self.instructions.append('1')
        self.instructions.append(t)
        return self.recv_and_state()

    def create_post(self, t, p, col, l=None):
        self.program.sendline('2')
        self.program.sendline(t)

        self.instructions.append('2')
        self.instructions.append(t)

        if l is None:
            self.program.sendline(str(len(p)+2))
            self.instructions.append(str(len(p)+2))
        else:
            self.program.sendline(str(l))
            self.instructions.append(str(l))

        self.program.sendline(p)
        self.program.sendline(col)

        self.instructions.append(p)
        self.instructions.append(col)

        return self.recv_and_state()

    def list_threads(self):
        self.program.sendline('3')
        self.instructions.append('3')
        return self.recv_and_state()

    def list_posts(self, t):
        self.program.sendline('4')
        self.program.sendline(t)
        self.instructions.append('4')
        self.instructions.append(t)
        return self.recv_and_state()

    def delete_thread(self, t):
        self.program.sendline('5')
        self.program.sendline(t)
        self.instructions.append('5')
        self.instructions.append(t)
        return self.recv_and_state()

    def modify_thread(self, t1, t2):
        self.program.sendline('6')
        self.program.sendline(t1)
        self.program.sendline(t2)
        self.instructions.append('6')
        self.instructions.append(t1)
        self.instructions.append(t2)
        return self.recv_and_state()

    def logout(self):
        self.program.sendline('7')
        self.instructions.append('7')
        return self.recv_and_state()

    def instructions_until_now(self):
        return self.instructions
