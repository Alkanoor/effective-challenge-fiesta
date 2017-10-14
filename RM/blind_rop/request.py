import re
import time
import socket
import binascii


class Request:
    unique_answers = []
    unique_answer_strings = []
    new_request_callback = None
    request_counter = 0
    test_cookie_changed = 20
    test_cookie_callback = None

    #challenge03.root-me.org, 56542
    def __init__(self, host='localhost', port=8888, length=4096, timeout=1.5, retry=100, delay=0.1):
        self.host = host
        self.port = port
        self.len = length
        self.delay = delay
        self.timeout = timeout

        i = 0
        good = False
        while i<retry and not good:
            try:
                #self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                #self.s.settimeout(timeout*(i+1))
                #self.s.connect((self.host, self.port))
                self.s = socket.create_connection((self.host, self.port), self.timeout*(i+1))
                self.s.settimeout(None)
                good = True
            except Exception,e:
                print("[!"+"-"*i+"] Exception received during connect in request : "+str(e))
                try:
                    self.s.close()
                except:
                    print("[!"+"-"*i+"] No socket has been created")
                time.sleep((i+1)*5)
            except:
                print("[!!!] Bad exception received during connect, exiting")
                exit()
            i += 1

        if i>=retry:
            print("[!!!!] Number of tries exceeded, exiting")
            exit()

    def send(self, input):
        self.s.settimeout(self.timeout)
        try:
            self.s.send(input)
        except:
            print("[!!!] Broken pipe during send, exiting")
            exit()

    def send_receive_list(self, inputs, test_again_when_timeout=True):
        self.s.settimeout(self.timeout)
        try:
            for i in inputs:
                self.s.send(i+'\n')
        except:
            print("[!!!] Broken pipe during send, exiting")
            exit()

        tmp = []
        all_str = ''
        self.exit = 1
        self.crash = 0
        try:
            for j in range(len(inputs)):
                t = 'a'
                while len(t)>0:
                    t = self.s.recv(self.len)
                    u = t.split('\n')
                    for i in u:
                        if i != '':
                            tmp.append(i)
                            all_str += i
        except Exception, e:
            if re.search('Connection reset by peer',str(e)):
                self.crash = 1
            elif re.search('timed out',str(e)):
                self.exit = 0
            else:
                print("Exception : "+str(e))
                print("[-] Unknown exception, exiting")
                exit()
        except:
            print("[!!!] Bad exception received during receive, exiting")
            exit()
        finally:
            #print(binascii.hexlify(input))
            self.s.close()
            time.sleep(self.delay)

        return tmp

    def send_receive(self, input, times_to_send=1, test_again_when_timeout=True):
        self.s.settimeout(self.timeout)
        try:
            self.s.send(input)
        except:
            print("[!!!] Broken pipe during send, exiting")
            exit()

        tmp = []
        all_str = ''
        self.exit = 1
        self.crash = 0
        try:
            for j in range(times_to_send):
                t = 'a'
                while len(t)>0:
                    t = self.s.recv(self.len)
                    u = t.split('\n')
                    for i in u:
                        if i != '':
                            tmp.append(i)
                            all_str += i

                if j+1<times_to_send:
                    try:
                        self.s.send(input)
                    except:
                        print("[!!!] Broken pipe during send, exiting")
                        exit()
            if len(tmp)>8:
                index = 0
                stop = False
                while not stop:
                    try:
                        open('important'+str(index), 'rb')
                        index += 1
                    except:
                        stop = True
                print("[+] We fished a big fish ! Writing in important"+str(index))
                open('important'+str(index), 'wb').write(all_str)
        except Exception, e:
            if re.search('Connection reset by peer',str(e)):
                self.crash = 1
            elif re.search('timed out',str(e)):
                self.exit = 0
                self.s.close()
                if test_again_when_timeout:
                    print("Testing again ")
                    time.sleep(self.timeout/2.0)
                    retest = Request(self.host,self.port,self.len,self.timeout*1.2)
                    res = retest.send_receive(input, times_to_send, False)
                    if res&2 != 0:
                        time.sleep(self.timeout/2.0)
                        retest_again = Request(self.host,self.port,self.len,self.timeout*1.5)
                        res_again = retest_again.send_receive(input, times_to_send, False)
                        if res_again == res:
                            print("Testing again again (good) "+binascii.hexlify(input)+" "+str(res)+" => "+str(self.get_answer(res>>2)))
                            self.exit = 1
                            return res
                        else:
                            print("Testing again again (bad) "+binascii.hexlify(input)+" "+str(res)+" => "+str(self.get_answer(res>>2)))
                            if res_again&2 == res&2:
                                self.exit = 1
                                return res
            else:
                print("Exception : "+str(e))
                print("[-] Unknown exception, exiting")
                exit()
        except:
            print("[!!!] Bad exception received during receive, exiting")
            exit()
        finally:
            #print(binascii.hexlify(input))
            self.s.close()
            time.sleep(self.delay)

        t = ''.join(tmp)
        if t in Request.unique_answer_strings:
            index = Request.unique_answer_strings.index(t)
        else:
            index = len(Request.unique_answer_strings)
            Request.unique_answer_strings.append(t)
            Request.unique_answers.append(tmp)
            if self.new_request_callback is not None:
                self.new_request_callback(tmp, input)

        Request.request_counter += 1
        if Request.request_counter%self.test_cookie_changed == 0 and self.test_cookie_callback is not None:
            if not self.test_cookie_callback():
                print("[!] Cookie changed or something went wrong, exiting")
                exit()

        return index*4+self.exit*2+self.crash

    def dump(self, input, bytes_to_recv, separator):
        self.s.settimeout(self.timeout)
        try:
            self.s.send(input)
        except:
            print("[!!!] Broken pipe during send, exiting")
            exit()

        tmp = []
        self.exit = 1
        self.crash = 0
        try:
            t = ''
            while len(t.split(separator))<2:
                t = self.s.recv(max(self.len, len(separator)))

            v = ''
            w = ''
            while len(v)<bytes_to_recv:
                v += w
                w = self.s.recv(bytes_to_recv-len(v))
                if w == '':
                    break
            t = separator.join(t.split(separator)[1:])
            if t[0]=='\x0a':
                t = t[1:]
            if len(v)!=0:
                t += v

            tmp = [t]

        except Exception, e:
            if re.search('Connection reset by peer',str(e)):
                self.crash = 1
                self.exit = 1
                return -1
            else:
                print("Exception : "+str(e))
                print("[-] Unknown exception, exiting")
                exit()
        except:
            print("[!!!] Bad exception received during receive, exiting")
            exit()
        finally:
            #print(binascii.hexlify(input))
            self.s.close()
            time.sleep(self.delay)

        if t in Request.unique_answer_strings:
            index = Request.unique_answer_strings.index(t)
        else:
            index = len(Request.unique_answer_strings)
            Request.unique_answer_strings.append(t)
            Request.unique_answers.append(tmp)
            if self.new_request_callback is not None:
                self.new_request_callback(tmp, input)

        Request.request_counter += 1
        if Request.request_counter%self.test_cookie_changed == 0 and self.test_cookie_callback is not None:
            if not self.test_cookie_callback():
                print("[!] Cookie changed or something went wrong, exiting")
                exit()

        return index*4+self.exit*2+self.crash

    @staticmethod
    def get_answer(index):
        return Request.unique_answers[index]
