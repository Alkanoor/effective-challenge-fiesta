import random


class Oracle_Iteration:

    def __init__(self, base_addr, aligned, delay_double_period, stop_period, random_reset_smaller_period):
        self.base_addr = base_addr
        self.aligned = aligned
        self.delay_double_period = delay_double_period
        self.stop_period = stop_period
        self.random_reset_smaller_period = random_reset_smaller_period


    def reset_oracle(self, callback):
        self.callback = callback

    def itere(self):
        self.addresses1 = []
        self.addresses2 = []

        modulow = 0
        while self.addresses1 == [] and self.addresses2 == [] and modulow<4:

            ok_forward = True
            ok_backward = True

            initial = self.base_addr//self.aligned

            cur = 0
            delay = 0
            period = 1
            delay_double_period = self.delay_double_period

            while ok_forward:
                if period>=self.stop_period:
                    ok_forward = False
                    break

                addr = (initial+cur)*self.aligned+modulow
                cur_answer = self.callback(addr)
                if cur_answer[0]:
                    print("We added address !!")
                    print(hex(addr))
                    print("[.] Cur is "+str(cur))
                    if cur_answer[1]:
                        self.addresses2.append(addr)
                    else:
                        self.addresses1.append(addr)
                    period = 1
                    delay_double_period = self.delay_double_period
                    delay = 0
                else:
                    delay += 1
                    if delay>=delay_double_period:
                        delay = 0
                        delay_double_period /= 2
                        period *= 2
                        print("[.] Doubling period : "+str(period))
                        print("[.] Cur is "+str(cur)+" and "+hex(addr))
                    if (delay+1)%self.random_reset_smaller_period == 0 and period>1:
                        if period>2:
                            if random.randint(0,1) == 0:
                                cur -= period/4
                            else:
                                cur -= period/2
                        else:
                            cur -= period/2

                cur += period

            print("[.] Beginning next part")

            cur = 1
            delay = 0
            period = 1
            delay_double_period = self.delay_double_period

            while ok_backward:
                if period>=self.stop_period:
                    ok_backward = False
                    break

                addr = (initial-cur)*self.aligned+modulow
                cur_answer = self.callback(addr)
                if cur_answer[0]:
                    print("We added address !!")
                    print(hex(addr))
                    print("[.] Cur is "+str(-cur))
                    if cur_answer[1]:
                        self.addresses2.append(addr)
                    else:
                        self.addresses1.append(addr)
                    period = 1
                    delay_double_period = self.delay_double_period
                    delay = 0
                else:
                    delay += 1
                    if delay>=delay_double_period:
                        delay = 0
                        delay_double_period /= 2
                        period *= 2
                        print("[.] Doubling period : "+str(period))
                        print("[.] Cur is "+str(-cur)+" and "+hex(addr))
                    if (delay+1)%self.random_reset_smaller_period == 0 and period>1:
                        if period>2:
                            if random.randint(0,1) == 0:
                                cur -= period/4
                            else:
                                cur -= period/2
                        else:
                            cur -= period/2

                cur += period
            modulow += 1

        return (sorted(self.addresses1), sorted(self.addresses2))
