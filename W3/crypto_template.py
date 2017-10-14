#N = int("0xc8283502d6ed4c723078d5ddd299c67deaef48ca2d8cdce64f99fe50ee5705705ab25c220ba6a1521c068016aab51f5139962bf8362f8b5ea157fc3ecefebe6dec216ba655c3f2b1538907182760ffde203bbed8e0a41bc833e94369e631b7a559f71e7ed773f029b82f46fbb0842f898048e45e15330b6671a8dbda59b025eb",16)
#e = 65537
#p = int("0xf51d59442bd9c0e3d7e51e54ae8c46a3e1bce33a1b38b4fbea26803de37475b0d1702431966d058327a629ce3af3321b06e6be4a9c9671e02f488405c9e91c71",16)
#q = int("0xd10bbefe61fe293d45a0bd3266429c461977237838677bee06fe3ed051eb0b36828e627126239121913d4324029fb601b456c33863c9fa7bfa0ce85ff427861b",16)
#d = int("0xd490debb8545be4a06f04d30a6d868d4910c4e6168be905a876f23870f979b4f17031495938a0309107a56cdbbbd5ee5042357cee2bcdb6644330cd02744a336779ca1f2f5fed59951c34c216577870841cb50e6a01be8f2e23591db4e8df1551d4245049c0996a887f82636a2bb5aff48c42ed83be4f2c218cd83307395941",16)
#
##print(N)
##print(p*q)
##print((d*e) % ((p-1)*(q-1)))
#
#c = "1dca210d36fb700e0fe41e951216b89c4cf10a4d4feeeac92722184a8d1e1306da36002bef27e9f0ec3b3256e821cfd0f7220930ac3d71a9fb981e9ad5ef3713b57ec78bfd4a96d53c7b0ad9e3698deef5ba10486da5936b60768c7275bb57ee67bc832ad954ee0c38124bc9518bf84d2fe76b16036d51071d307d6d23fe19ad"
#cConverted = int(c,16)
#print(cConverted)
#
#m = pow(cConverted,d,N)
#
#print(m)
#print(hex(m))





#import binascii
#
##print(int("00c2cbb24fdbf923b61268e3f11a3896de4574b3ba58730cbd652938864e2223eeeb704a17cfd08d16b46891a61474759939c6e49aafe7f2595548c74c1d7fb8d24cd15cb23b4cd0a3",16))
#N = int("00c2cbb24fdbf923b61268e3f11a3896de4574b3ba58730cbd652938864e2223eeeb704a17cfd08d16b46891a61474759939c6e49aafe7f2595548c74c1d7fb8d24cd15cb23b4cd0a3",16)
#e = 65537
#p = 398075086424064937397125500550386491199064362342526708406385189575946388957261768583317
#q = 472772146107435302536223071973048224632914695302097116459852171130520711256363590397527
#phi = (p-1)*(q-1)
#
##print(N)
##print(p*q)
#
#def egcd(a, b):
#    if a == 0:
#        return (b, 0, 1)
#    else:
#        g, y, x = egcd(b % a, a)
#        return (g, x - (b // a) * y, y)
#
#def modinv(a, m):
#    g, x, y = egcd(a, m)
#    if g != 1:
#        raise Exception('modular inverse does not exist')
#    else:
#        return x % m
#
# d = modinv(e,phi)
#
# def int_to_string(i):
#     t = hex(i).replace('0x','').replace('L','')
#     if len(t)%2 == 1:
#         t = '0'+t
#     return binascii.unhexlify(t)
#
#
#c = int("7bca100e286c9a4be34f7b197be104f25c0dbc112c15e81817af8e3853a247a80cb4c671c5b6bf6c880b503f29577c847f480e39f1ee0796c2def426a3b6c4e0f70829fa45199040",16)
##c = int("011110111100101000010000000011100010100001101100100110100100101111100011010011110111101100011001011110111110000100000100111100100101110000001101101111000001000100101100000101011110100000011000000101111010111110001110001110000101001110100010010001111010100000001100101101001100011001110001110001011011011010111111011011001000100000001011010100000011111100101001010101110111110010000100011111110100100000001110001110011111000111101110000001111001011011000010110111101111010000100110101000111011011011000100111000001111011100001000001010011111101001000101000110011001000001000000",2)
##print(c)
#
#m = pow(c,d,N)
#
##print(hex(m).strip("0x"))
#print(binascii.unhexlify("0"+hex(m).strip("0x")))







# N = int("0x00c8283502d6ed4c723078d5ddd299c67deaef48ca2d8cdce64f99fe50ee5705705ab25c220ba6a1521c068016aab51f5139962bf8362f8b5ea157fc3ecefebe6dec216ba655c3f2b1538907182760ffde203bbed8e0a41bc833e94369e631b7a559f71e7ed773f029b82f46fbb0842f898048e45e15330b6671a8dbda59b025eb",16)
# e = 3
# c = "0x9367dc2d182f570da543a97a10af95c9b34d44b2f0c62a281ae0a7ed6d55a7f22acf2e8f144ffa82c731557d6a4fe7622fad66d5ff6519295ed13870a47c3a6bfe511fcde5ee366fc4e456bf627b7db0301cfc377a9a9bae37fc83256d678ece458832db4fb08f0f0f0a556d12c5f114fcb7b63fe78be88eafe813fc7f189ad2"
# c = "08 89 23 1a 91 de 96 a9 9d 8a ff 98 23 05 bf 35 7d ef d4 1d 88 cb f1 a0 3e 45 1c 49 a0 08 22 0f d5 92 1b 57 16 c3 46 b9 b4 fa 1e cf c4 cf 80 e5 ee 32 2d 0d 4b 95 50 7f 1a 52 17 41 ec 20 de 10 d1 f1 85 5d 3a 7e 0c fa a7 69 2d 06 75 98 0e 01 cf 98 25 61".replace(' ', '')
#
# from decimal import *
#
# getcontext().prec = len(c)
#
#
# # c = Decimal(int(c,16)+11*N)
# c = Decimal(int(c,16))
# power = Decimal(1)/Decimal(3)
#
# answer = pow(c,power)
# ranswer = answer.quantize(Decimal('1.'), rounding=ROUND_UP)
#
# print(ranswer)
#
# print(hex(8677313409321008985903374074267835836119763539933346196890726396705))
# import binascii
# print(binascii.unhexlify(hex(8677313409321008985903374074267835836119763539933346196890726396705).replace('0x','').replace('L','')))








#import socket
#
#TCP_IP = 'vuln2015.icec.tf'
#TCP_PORT = 30896
#BUFFER_SIZE = 1024
#
#
#try:
#    decAr = [line.rstrip('\n') for line in open('fileDec.txt')]
#except:
#    decAr = []
#
#temp = ""
#i = 0
#while i<800 and len(decAr)<780:
#    if temp is not "" and not decAr.__contains__(str(int(temp,16))):
#        decAr.append(str(int(temp,16)))
#
#    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#    s.connect((TCP_IP, TCP_PORT))
#    data = s.recv(BUFFER_SIZE)
#    data = s.recv(BUFFER_SIZE)
#
#    temp = data.decode("utf-8").strip("\n")
#    s.close()
#    i = i+1
#
#decAr = sorted(decAr)
#with open('fileDec.txt','w+') as currentKeys:
#    currentKeys.write("\n".join(decAr))
#
#
#def pgcd(a,b):
#    while (b>0):
#        r=a%b
#        a,b=b,r
#    return a
#
#
#try:
#    primes = [line.rstrip('\n') for line in open('primes.txt')]
#except:
#    primes = []
#
#if len(primes)<40:
#    for x in decAr:
#        x = int(x,10)
#        for y in decAr:
#            y = int(y,10)
#            if x > y:
#                gcd = pgcd(x,y)
#                a = x//gcd
#                b = y//gcd
#                if gcd != 1 and gcd not in primes:
#                    print(gcd)
#                    primes.append(gcd)
#                    if a != 1 and a not in primes:
#                        print(a)
#                        primes.append(a)
#                    if b != 1 and b not in primes:
#                        print(b)
#                        primes.append(b)
#
#
#possibilities = [3,5,9,17,33,65,129,257,513,1023,2049,4097,8193,65537]
#
#cVerif = 27134539740327372277016096853435890120677470119612424124869327819124029912990004448750434621403418542927781194142877244503562989100969794546726189679434973051199593686324469650695332464843866317242833309989642047675838763945117051708685755516681732600344477784607819725824461400081264484810830802070160626494750360668977494105105567529042035493471083490134591723283745502956169145544321430921932449188900918387414900628355258180161727963712905333194811283381016749488185293777854150520335564364850062292655420041681761888247884838176822010929853437116012249823316297480912216876461230774949536318942112650569572741229
#cCrypted = 21833706562424363526758144595528139378681868374355612924041399984966569709971402846162543351650992393259625378308766376918010037809411868937951264540233547911616955412668210947953666054174014762004709853178682474885483298510115565509957726137783160293746001217719965940995344574478555209182195121905187551848171141764244076996783305517744086819333014890572868236912842045064036434736842358851218773925473983781900791489911542650152543840593725659311233554355918780080457663947286285012785980160999737442977651996204521503213470778632213967510707131516893141063362768682472114553632059355826524352103299651991899005722
#
#
#def egcd(a, b):
#    if a == 0:
#        return (b, 0, 1)
#    else:
#        g, y, x = egcd(b % a, a)
#        return (g, x - (b // a) * y, y)
#
#def modinv(a, m):
#    g, x, y = egcd(a, m)
#    if g != 1:
#        raise Exception('modular inverse does not exist')
#    else:
#        return x % m
#
#
#for i in range(0,len(primes)):
#    x = int(primes[i],10)
#    for j in range(i+1,len(primes)):
#        y = int(primes[j],10)
#        N = x*y
#        if N == cVerif:
#          phi = (x-1)*(y-1)
#          for e in possibilities:
#              inv = modinv(e,phi)
#              m = pow(cCrypted,inv,N)
#              print(hex(m))



def isqrt(n):
    x = n
    y = (x + 1) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x

def is_square(n):
    return (isqrt(n)*isqrt(n)==n)

def fermat(n,max):
    if is_square(n):
        return isqrt(n),isqrt(n)

    a = isqrt(n)+1
    i = 0
    while not is_square(a*a-n) and i<max:
        a = a+1
        i = i+1
    if i>=max:
        return None
    else:
        b = isqrt(a*a-n)
        return a+b,a-b



#import socket
#
#TCP_IP = 'vuln2015.icec.tf'
#TCP_PORT = 31896
#BUFFER_SIZE = 1024
#
#key = int("ccac6732bf9244596d97bbeacf14500202fac187b7a7167db3b261dc338cbdad45b86b8f41ece292e4cca081179160a0b1e9d74d6f692d3cdcb234b16afc87a834c672919789ba6962d52ec841686b46210d024a00ba9f47d8c4c7871637a1aa9ac6612374d478a5584d087f28743d0c9115bc24e1b05f0c58c5461063611d3b54b626ea3e060ae8e1ee002eec17608f0e35e08bec261368976e14402547bac5c1af7e0d0e143b73ccd1c27fe1fbf36668bd89b37939d65006f5f7520086d1ef77d522511cf19572140b2e2ed0236942c227b76044c2b694a453c54faf0be63fdc8fa7979b0889afa9ebd54e4569b0da1ac0e3a0a92338ad748d208710e53a17db736e8c03d72918a449b515faf902930762b4fd323325c5cfaf1715b7ae8dead483eaa1e08de96a3adb55d1535968ce228a59cf618a2ba79745643cb8dfa42046c03137d18b68fe3df2477b5e7531e8c0c309a24f83627a3f4bd8e7dca3587ba6086cbdb48b032db0f5e8f04b79b844989a763705ee4ceb86d2216de023f1dba53ac473b3f3228f0575afac815164c82d18d2c1dd7fb4483f8347b0c3e3cd126feab1e0bc5cda3d279265f52d2db2e381ca4049041754c82eb236e00118d4c44f21b7a62fde1febf16e739dfed6504b25d628d04ee5e8b79801f6c86e911dec61e4241eea9242a7b02acd431e5ed05d20ea2bdf2832cc0a87702383a5a6ba19",16)
#
#ar = []
#temp = ""
#i = 742
#while i<1000:
#    if temp is not "" and not ar.__contains__(temp):
#        ar.append(temp)
#
#    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#    s.connect((TCP_IP, TCP_PORT))
#    data = s.recv(BUFFER_SIZE)
#    s.send((str(i)+"\n").encode("utf-8"))
#    data = s.recv(BUFFER_SIZE)
#    data = s.recv(BUFFER_SIZE)
#    temp = data.decode("utf-8").strip("\n")
#    print(temp)
#    data = s.recv(BUFFER_SIZE)
#    temp = data.decode("utf-8").strip("\n")
#    print(temp)
#    print()
#    s.close()
#    i = i+1



###Timing attack root me
#import statistics
#import math
#import time
#
#TCP_IP = 'challenge01.root-me.org'
#TCP_PORT = 51015
#BUFFER_SIZE = 1024
#
#
#millis = int(round(time.time() * 1000))
#s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#s.connect((TCP_IP, TCP_PORT))
#data = s.recv(BUFFER_SIZE)
#s.send(("30467-132630").encode("utf-8"))
#data = s.recv(BUFFER_SIZE)
#temp = data.decode("utf-8").strip("\n")
#print(temp)
#
#
#for i in list(range(48,58)) + list(range(65,91)) + list(range(97,123)):
#    ar = []
#    while len(ar)<1:
#        millis = int(round(time.time() * 1000))
#        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#        s.connect((TCP_IP, TCP_PORT))
#        data = s.recv(BUFFER_SIZE)
#        s.send(("30467-132630"+chr(i)).encode("utf-8"))
#        data = s.recv(BUFFER_SIZE)
#        millis2 = int(round(time.time() * 1000))
#        ar.append(millis2-millis)
#
#    print(chr(i))
#    print(math.sqrt(statistics.pvariance(ar)))
#    print(statistics.mean(ar))



###Hash length extension root me
#import socket
#TCP_IP = 'challenge01.root-me.org'
#TCP_PORT = 51022
#BUFFER_SIZE = 1024
#
##envoi :
##
##pseudo : ""
##role : "guest"
##
##serveur:
##"secret"+":guest"
##=> sha256
##retourne base64(:guest)+base64(sha256(secret+:guest))
##
##
##client:
##renvoie base64(:guest)+base64(sha256(secret+Alkan:guest))
##but:
##renvoyer base64(:guest:admin)+base64(sha256(secret+:guest:admin))
#
#s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#s.connect((TCP_IP, TCP_PORT))
#data = s.recv(BUFFER_SIZE)
#temp = data.decode("utf-8").strip("\n")
#print(temp)
#s.send("0\n".encode("utf-8"))
#data = s.recv(BUFFER_SIZE)
#temp = data.decode("utf-8").strip("\n")
#print(temp)
#s.send("\n".encode("utf-8"))
#data = s.recv(BUFFER_SIZE)
#temp = data.decode("utf-8").strip("\n")
#print(temp)
#s.send("guest\n".encode("utf-8"))
#data = s.recv(BUFFER_SIZE)
#temp = data.decode("utf-8").strip("\n")
#print(temp)
#data = s.recv(BUFFER_SIZE)
#temp = data.decode("utf-8").strip("\n")
#print(temp)
#data = s.recv(BUFFER_SIZE)
#temp = data.decode("utf-8").strip("\n")
#print(temp)
#data = s.recv(BUFFER_SIZE)
#temp = data.decode("utf-8").strip("\n")
#print(temp)
#
#s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#s.connect((TCP_IP, TCP_PORT))
#data = s.recv(BUFFER_SIZE)
#temp = data.decode("utf-8").strip("\n")
#print(temp)
#s.send("1\n".encode("utf-8"))
#data = s.recv(BUFFER_SIZE)
#temp = data.decode("utf-8").strip("\n")
#print(temp)
##voir programme le programme fait en C hashLengthExtension
#s.send(("Omd1ZXN0gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACwOmFkbWlu:NTkwOTUwZGUwOTc0NzE1YzRiZGEzM2UxYjIwYzUxMDY2ODhmZDYzN2JmYWE3ZjkxNTExZGRhNzI4YmU4ZjExMw==\n").encode("utf-8"))
#data = s.recv(BUFFER_SIZE)
#temp = data.decode("utf-8").strip("\n")
#print(temp)



def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def egcdIter(a, b):
    l = []
    while a!=0:
        l.append((a,b))
        a,b = b%a,a
    g,y,x = (b,0,1)
    s = len(l)
    for i in range(s):
        g,y,x = (g, x-(l[s-1-i][1]//l[s-1-i][0])*y, y)
    return (g,y,x)




def modinv(a, m):
    g, x, y = egcdIter(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m


def isPrime(n):
    if n==2 or n==3: return True
    if n%2==0 or n<2: return False
    for i in range(3,int(n**0.5)+1,2):   # only odd numbers
        if n%i==0:
            return False

    return True


def factor(n,offsetForPrimes=1000):
    ret = {}
    primes = []
    cur = 1
    found = False
    findPrimes = True
    while not found:
        if findPrimes:
            for i in range(cur,cur+offsetForPrimes):
                if isPrime(i):
                    primes.append(i)

        findPrimes = True
        for p in primes:
            if n%p == 0:
                findPrimes = False
                if ret.get(p) is None:
                    ret.update({p:1})
                else:
                    ret.update({p:ret[p]+1})
                n = n//p
            if n<=1:
                found = True
        cur = cur+offsetForPrimes

    return ret

def factorStop(n,numberPrimes=1000):
    ret = {}
    primes = []

    for i in range(1,numberPrimes):
        if isPrime(i):
            primes.append(i)

    for p in primes:
        while n%p == 0:
            if ret.get(p) is None:
                ret.update({p:1})
            else:
                ret.update({p:ret[p]+1})
            n = n//p

    ret.update({n:1})
    return ret


###Discrete log a la main root me
#p = 7863166752583943287208453249445887802885958578827520225154826621191353388988908983484279021978114049838254701703424499688950361788140197906625796305008451719
#y = 6289736695712027841545587266292164172813699099085672937550442102159309081155467550411414088175729823598108452032137447608687929628597035278365152781494883808
#g = 2862392356922936880157505726961027620297475166595443090826668842052108260396755078180089295033677131286733784955854335672518017968622162153227778875458650593
#
#factors = factor(p-1)
#residuals = {}
#for key in factors:
#    residual = 0
#    cur = y
#    puis = 1
#    for j in range(0,factors[key]):
#        print(j)
#        for i in range(0,key):
#            if pow(cur,(p-1)//(puis*key),p) == pow(g,i*(p-1)//key,p):
#                temp = i
#        residual = residual+temp*puis
#        cur = ((cur*pow(g,p-1-temp*puis,p))%p)
#        puis = puis*key
#    residuals.update({key:residual})
#    print(residual)
#    print("was for "+str(key)+" and "+str(factors[key]))
#
#final = 0
#for key in residuals:
#    product = 1
#    for key2 in residuals:
#        if key is not key2:
#            product = product*pow(key2,factors[key2])
#    final = final + product*residuals[key]*modinv(product,pow(key,factors[key]))
#
#print(final%(p-1))
#print(final)
#print(pow(g,final,p))



###Discrete log mma ctf
#import re
#import pycurl
#
#TCP_IP = 'cry1.chal.mmactf.link'
#TCP_PORT = 39985
#BUFFER_SIZE = 1024
#
#class Storage:
#        def __init__(self):
#            Storage.clear(self)
#
#        def clear(self):
#            self.contents = ''
#            self.line = 0
#
#        def store(self, buf):
#            self.line = self.line + 1
#            self.contents = "%s%i: %s" % (self.contents, self.line, buf)
#
#        def __str__(self):
#            return self.contents
#
#
#ok = False
#while not ok:
#    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#    s.connect((TCP_IP, TCP_PORT))
#    data = s.recv(BUFFER_SIZE)
#    temp = data.decode("utf-8").strip("\n")
#    print(temp)
#    s.send("1\n".encode("utf-8"))
#    data = s.recv(BUFFER_SIZE)
#    temp = data.decode("utf-8").strip("\n")
#    print(temp)
#    s.send("1\n".encode("utf-8"))
#    data = s.recv(BUFFER_SIZE)
#    temp = data.decode("utf-8").strip("\n")
#    print(temp)
#    data = s.recv(BUFFER_SIZE)
#    temp = data.decode("utf-8").strip("\n")
#
#    print(temp)
#    g = int(re.search('\((.*),',temp).group(1),10)
#    h = int(re.search(', (.*)\)',temp).group(1),10)
#
#
#    s.send("1\n".encode("utf-8"))
#    data = s.recv(BUFFER_SIZE)
#    temp = data.decode("utf-8").strip("\n")
#    print(temp)
#    s.send("2\n".encode("utf-8"))
#    data = s.recv(BUFFER_SIZE)
#    temp = data.decode("utf-8").strip("\n")
#
#    r1 = int(re.search('\((.*),',temp).group(1),10)
#    print(temp)
#
#    data = s.recv(BUFFER_SIZE)
#    temp = data.decode("utf-8").strip("\n")
#    print(temp)
#    s.send("1\n".encode("utf-8"))
#    data = s.recv(BUFFER_SIZE)
#    temp = data.decode("utf-8").strip("\n")
#    print(temp)
#    s.send("3\n\n".encode("utf-8"))
#    data = s.recv(BUFFER_SIZE)
#    temp = data.decode("utf-8").strip("\n")
#
#    r2 = int(re.search('\((.*),',temp).group(1),10)
#    print(temp)
#
#    data = s.recv(BUFFER_SIZE)
#    temp = data.decode("utf-8").strip("\n")
#    print(temp)
#
#
#    def pgcd(a,b):
#        while (b>0):
#            r=a%b
#            a,b=b,r
#        return a
#
#    print(g,r1,r2,h)
#
#
#    p = pgcd(pow(g,2)-r1,pow(g,3)-r2)
#    print(p)
#
#
#
#    body = Storage()
#
#
#    c = pycurl.Curl()
#    c.setopt(c.URL, 'http://factordb.com/index.php?query='+str(p-1))
#    c.setopt(c.USERAGENT, 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0')
#    c.setopt(c.WRITEFUNCTION, body.store)
#    c.perform()
#
#    print(body.contents)
#    matches = re.findall('&lt;([0-9]*)&gt;',body.contents)
#    print(matches)
#
#    ok = True
#    for i in range(1,len(matches)):
#        if int(matches[i],10) > 13:
#            ok = False
#
#    if ok:
#        print('Super !')
#    else:
#        print('Pasuper ....')




import math

class frac:
    def __init__(self, p, q):
        self.p = p
        self.q = q

    def add(self, p, q):
        self.p = p*self.q+q*self.p
        self.q = q*self.q
        self.simplify()
        return self

    def __add__(self, other):
        return self.add(other.p,other.q)

    def simplify(self,max_=100000):
        ma = max(self.p,self.q)
        mi = min(self.p,self.q)
        for i in range(2,min(max_,min(math.floor(math.sqrt(ma)),mi))):
            while self.p%i==0 and self.q%i==0:
                self.p = self.p//i
                self.q = self.q//i

    def inverse(self):
        temp = self.p
        self.p = self.q
        self.q = temp
        return self

    def __str__(self):
        return str(self.p)+"/"+str(self.q)


def computeFrac(ar):
    if len(ar)<=1:
        return frac(ar[0],1)
    else:
        temp = computeFrac(ar[1:])
        if temp.p != 0:
            return frac(ar[0],1)+temp.inverse()
        else:
            return frac(ar[0],1)


N = int("0x0207a7df9d173f5969ad16dc318496b36be39fe581207e6ea318d3bfbe22c8b485600ba9811a78decc6d5aab79a1c2c491eb6d4f39820657b6686391b85474172ae504f48f02f7ee3a2ab31fce1cf9c22f40e919965c7f67a8acbfa11ee4e7e2f3217bc9a054587500424d0806c0e759081651f6e406a9a642de6e8e131cb644a12e46573bd8246dc5e067d2a4f176fef6eec445bfa9db888a35257376e67109faabe39b0cf8afe2ca123da8314d09f2404922fc4116d682a4bdaeecb73f59c49db7fa12a7fc5c981454925c94e0b5472e02d924dad62c260066e07c7d3b1089d5475c2c066b7f94553c75e856e3a2a773c6c24d5ba64055eb8fea3e57b06b04a3",16)
e = int("0xf70b3bd74801a25eccbde24e01b077677e298391d4197b099a6f961244f04314da7de144dd69a8aa84686bf4ddbd14a6344bbc315218dbbaf29490a44e42e5c4a2a4e76b8101a5ca82351c07b4cfd4e08038c8d5573a827b227bce515b70866724718ec2ac03359614cdf43dd88f1ac7ee453917975a13c019e620e531207692224009c75eaef11e130f8e54cce31e86c84e9366219ae5c250853be145ea87dcf37aa7ece0a994195885e31ebcd8fe742df1cd1370c95b6684ab6c37e84762193c27dd34c3cf3f5e69957b8338f9143a0052c9381d9e2ecb9ef504c954b453f57632705ed44b28a4b5cbe61368e485da6af2dfc901e45868cdd5006913f338a3",16)
N = int("9C2F6505899120906E5AFBD755C92FEC429FBA194466F06AAE484FA33CABA720205E94CE9BF5AA527224916D1852AE07915FBC6A3A52045857E0A1224C72A360C01C0CEF388F1693A746D5AFBF318C0ABF027661ACAB54E0290DFA21C3616A498210E2578121D7C23877429331D428D756B957EB41ECAB1EAAD87018C6EA3445",16)
e = int("466A169E8C14AC89F39B5B0357EFFC3E2139F9B19E28C1E299F18B54952A07A932BA5CA9F4B93B3EAA5A12C4856981EE1A31A5B47A0068FF081FA3C8C2C546FEAA3619FD6EC7DD71C9A2E75F1301EC935F7A5B744A73DF34D21C47592E149074A3CCEF749ECE475E3B6B0C8EECAC7C55290FF148E9A29DB8480CFE2A57801275",16)

N = 370099671033141588376175581756360980424491995580600109524304692636792296120563363822977313410192016444986004859764911043147546964441891697775267469000813669187672202081765367588450379462043354336198833248696996620972969
e = 81217094210485305385908579085692955326960349012604988068015706478441236225473844540647797970330619202555571329961498543648679750305330820511812583724439577876079704157507012627626025198913463610479163744279625574680393
c = 91571267326134805910248069602074631240609709441545816949292962574287315805746477317383190676219563884569472817412122280789692032465427579523421783145180190039521150808597806422306625230943560935871831677869844034626576

print(N)
print(e)

a = [e,N]
t = []
fracs = []
denum = 1
i = 0
ok = False
while denum>0 and not ok:
    num = a[i]
    denum = a[i+1]
    i = i+1
    if denum>0:
        t.append(num//denum)
        a.append(num-denum*t[len(t)-1])
        print(num-denum*t[len(t)-1])
        f = computeFrac(t)
        if f.p > 0:
            phi = (f.q*e-1)//f.p
            pPlusQsur2 = (N-phi+1)//2
            qMoinsPsur2 = isqrt(pPlusQsur2*pPlusQsur2-N)
            q = pPlusQsur2+qMoinsPsur2
            p = pPlusQsur2-qMoinsPsur2
            if p*q == N:
                ok = True
                print("OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO "+str(p)+" "+str(q))
                exit()

p = 273067835270880086905225991495379768025497181071655465691068234751894433419924689398578343149876505032891110212422075482294849988417876098468455656340271714411918145829343178315564694346337087829483997746033122936265729805143582391157953230943745740375876718066059315171626227510845447370568918599985468283447
q = 240235037993086647490360091251920509660926008787784163933134217892938306866733942789677346753386227305733054945882967240289722901543973488715609201686292184661845932338700104193843036687863902362262743558762135191383008370605906319072352806840967443808455667223189470493469726348267326087313303773058894562037
print(p*q-N)
exit()
#
#print(hex(p))
#print(hex(q))
#phi = (p-1)*(q-1)
#d = modinv(e,phi)
#print(hex(d))
#print(hex(d%(p-1)))
#print(hex(d%(q-1)))
#print(hex(modinv(q,p)))


N = int("25B18BF5F389097D17237866BB51CFF8DE922453749EBC403B0995C97C0E386D46C161CADFF77C69860DAE4791C214CF8487AAAA9F26E920A977834906038AEFB5C30827DFCF3FC9E9769544F94E07CDFE0872039A3A6262116678B261FB2D6B9D32539E92A153B3675629BAB3942E7D35E30F7EEF5ABF1C50D797D0CC88E1BDCCFD1A12EA6F7EF75C3727DBDF2E780F3428AE8F7A4FB7A89F184A365032B153F8425E845750EB2B7ABC02DC15CE0207507AA950863BB8480A78028DD62979944D6C633FAFA103E4DB28CE87F5A0C6ED4A2F2664427F565C7781AB6191456D971C7FFA395272374CEC0155E5F91189DB742E4C28B03A0FA11CFFB03173D2A4CCE6AE53",16)
N = int("0A545BC4AC4DBB946202D12279316989FB8D76156070B26787F70302038885F826D6289D4EDF",16)
print(N)
e = 65537
print(hex(e))

p = 3133337
q = 25478326064937419292200172136399497719081842914528228316455906211693118321971399936004729134841162974144246271486439695786036588117424611881955950996219646807378822278285638261582099108339438949573034101215141156156408742843820048066830863814362379885720395082318462850002901605689761876319151147352730090957556940842144299887394678743607766937828094478336401159449035878306853716216548374273462386508307367713112073004011383418967894930554067582453248981022011922883374442736848045920676341361871231787163441467533076890081721882179369168787287724769642665399992556052144845878600126283968890273067575342061776244939
p = 279125332373073513017147096164124452877
q = 295214597363242917440342570226980714417
p = 1090722153235996330142075410436478002243695169
q = 1205715780593990230392627394727261364477802783
print(p*q-N)

print(hex(p))
print(hex(q))
phi = (p-1)*(q-1)
d = modinv(e,phi)

message = "09 01 9D F6 C0 BF 87 D9 67 2E 9B 9A E7 4F F4 EF 59 27 4A C3 F8 37 C5 9D 99 1B 23 A0 D2 1D 7D C9 6B 06 13 23 A7 B3 68 33 9C 72 D9 29 4D 2C B0 B6 CA 1E F0 6D 1C 34 F2 7C 23 A3 A5 05 E2 D9 86 28 A7 DC 8C F7 1B E2 5E 1B 15 AE 6E BF 23 18 D6 72 41 BE 6A 90 CA 50 DB 88 29 EC 38 38 E1 A4 1D 41 25 F7 69 53 52 D4 2A DC 2C 0B 16 DC ED F3 CB FF 3C D4 75 68 0E FA 87 FF 47 D5 A6 33 E4 0E 04 F6 A0 4C 03 5B 26 8D 26 A4 36 31 BC D2 91 8E F6 9C F4 1C 38 09 04 D3 87 CE E6 A2 AB 0D 45 21 3F 22 4E 6D 57 6A 64 15 16 5F 43 10 19 5A E5 5E 3E C1 E9 D1 15 D5 8A D1 F0 BC AC F0 98 DF 6F 32 A1 A6 E7 B5 9B D9 2B 68 EB 87 5B E2 02 C9 0E 1F 46 44 E4 0D F8 44 21 DF22E8492F0D36D06B6420DD7737CA1DAF30BFACCDFF9CE7BC1B2DB030641B28BCF0DCD0C70F643868C25ADC2947".replace(' ','')
message = "90 f9 83 14 b9 39 6f fb 68 ac 6e 77 b1 38 56 c0 47 8d 9b 40 08 a4 44 1e 93 4a d5 1b 7b c2 b6 d7".replace(' ','')
message = "0A24843F04581940EDB0F69F8169CC9783CDDDB1C4CEB7DC216F271A413EDB3135622C9D761C"
m = int(message,16)
print(hex(pow(m,d,N)))



#import socket
#
#TCP_IP = 'challenge01.root-me.org'
#TCP_PORT = 51014
#BUFFER_SIZE = 1024
#
#cipher = "BC16542433100D9522DC3B6428D4FF5F7FC67B4994323C47ED09F185C3CE7A2E"
#
#s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#s.connect((TCP_IP, TCP_PORT))
#s.settimeout(0.5)
#
#s.send((cipher+"\n").encode("utf-8"))
#data = s.recv(BUFFER_SIZE)
#received = data.decode("utf-8").strip("\n")
#print("=>"+received)
#
#
#for i in list(range(48,58)) + list(range(65,71)):
#    for j in list(range(48,58)) + list(range(65,71)):
##       672BD7FC5C => n
##       52662AD6FD5D => en
##       B15D6925D9F252 => hen
##       43B05C6824D8F353 => chen
##       FC40B35F6B27DBF050 => tchen
##       72FD41B25E6A26DAF151 => 1tchen
##       2D75FA46B5596D21DDF656 => K1tchen
##       752C74FB47B4586C20DCF757 => lK1tchen
##       46762F77F844B75B6F23DFF454 => llK1tchen
##       3747772E76F945B65A6E22DEF555 => 3llK1tchen
##       352858683169E65AA945713DC1EA4A => H3llK1tchen
#        cipher = ""+chr(j)+chr(i)+"352858683169E65AA945713DC1EA4A"+"7FC67B4994323C47ED09F185C3CE7A2E"
#        s.send((cipher+'\n').encode("utf-8"))
#        data = s.recv(BUFFER_SIZE)
#        received = data.decode("utf-8").strip("\n")
#        print(chr(j)+' '+chr(i)+" =>"+received)



#from fractions import gcd
#import binascii
#
#a = 1536831091626134344438562231262955999946747271027592454085080144975668680116633974319738838314902671476361252000779278994694659331506514289825134202998923512208559837631294865714096366262625651641224815256023747612527195574981227458782225722378872877726156517419049543333249517100953017829975150178811183051072420620920351512550441692883372916625292779222549959972827892990998074974011820708412769448585824233964010823527283596363758019335173298785567326907562869725831298384056166394854331945427092768780512408697309431195959298622391255021501620353297671404338080932330645769264634941456038882152334719430726109338429569337547704428005985982750015052443048433495064870200257365769414378785715253560971149171681438084191571439495195259219781689240323356859973420344882465167137033865632910444012905831594139665120851209803580111064330410313979952241963117076560493364598715028110591528077312715775397005038663520201729983592950907518633046810236034766654347443064135657482229428611935898108129337877416106235893772898887514558518410336608404740719016898181126549445118952269233850039884416238819750863431709956544730721450588873256178564213332283660727537669708142035616276318637554028394450781252902822999858076881677813954865672699
#b = 1405455047898827740601006407021150296528909540585121562589198449328218001225629686983792772541888537155044378244210689354548955262100293119596991029131482663677746780367170205455335004374126148925378320933009615607453603513225795133835429979078060753792655889467862517259336039567601271145650104894018988850999145240209913202961689191909064159128836497858763935559284599398929323345712734680121822215491459016972886662226074883181573318554458498606613651103013451173080463035466390004673614917869214148267833156247978656894719759671402802392357265806814372240833280538028745324171218173439276322620866751083968569792089323417700727899283538611306368397552298662070026985059152462486451121108147945864732050327267485968951733500201020385738040351520444271695179889200261334840316617883334955182418284149699551952650903441820386831185385161343684056382744050008735663588547157445387692747417002410174613096634382275934290599252757705014372370386331855300203726195321995346819169449213229408581911203220004832264128760395194678471712201456749651066777841770422772382633988959515430296693112207616126805062452052630756426442452599875800562863827372270736334965097675800013051366067392650711300512521008046846017805670240684012532551976837
#
#c = gcd(a,b)
#p1 = a//c
#p2 = b//c
#print(c)
#print(p1)
#print(p2)
#
#N = a
#e = 65537
#phi = (p1-1)*(c-1)
#d = modinv(e,phi)
#
#print(p1*c==N)
#
#msg = "00 09 2C 5D 91 AF EB 4D FD 33 6B 4A 02 B9 2C D7 FD E3 84 C8 9D D2 83 7C B3 FF 8A 8D C1 CF 23 DB BC 3F DD 2B A3 AD D4 0D 45 68 FC 43 8F BA F3 8D FC 0D 13 93 D0 F1 B2 C6 D8 13 77 4E 87 8B 8C 61 75 03 F5 CB 6E 03 B0 6F 59 42 9B A8 FA 98 F6 86 F5 69 A9 54 79 07 5D D1 AC 11 B2 EA 67 36 9D 9C BD D1 AB 0A CB 44 8A 78 F1 B5 DD 87 9E 75 6C DA BE 4D 13 3E 4B 85 BB 18 F3 B0 42 10 F5 B8 39 14 62 08 F4 1B B5 60 F0 FC 12 C8 A1 31 45 61 71 26 E4 BB 82 9A 88 36 14 17 02 D9 56 8B CC 41 F1 8E 4B F3 1F E7 97 03 DC 29 77 9D A5 36 F0 6D 1D 35 85 4C F8 E7 EB 9E CB 13 15 08 1B 64 63 36 7F 0E BE 2B E8 89 5F 80 02 BF 6B DC 55 11 21 52 4C B3 D2 4F DA 35 94 87 A5 55 9F F7 B2 73 6C C9 8C 5D B6 67 72 D3 D9 59 6D CD 13 4C 2F 98 A9 3D 69 AE A0 13 80 68 22 B8 97 75 6C C4 38 A5 05 BC 7C 9F A6 FE 6D 05 57 55 C8 0D FA 92 2A 60 F1 28 4B A6 D7 4B CE 50 0A CA 44 56 86 F8 F9 58 B2 E9 64 02 13 24 C9 7F B7 D9 0B D3 A5 E9 D7 C9 04 80 B6 90 FA AE B4 A9 C6 55 91 C5 35 4C B3 4C 2E EA B2 5C 9E 4D 54 0D AE D8 A3 72 B0 CC EC 62 19 60 99 9F 3F 0F 85 12 A8 0C CB 00 66 25 39 30 D5 57 49 BB 6D 39 43 3B 3C 14 48 C7 95 C4 F6 FD 7E 87 B5 92 EF 62 59 45 DE 0F D1 92 43 DF 04 07 BA 99 F4 E1 72 BC B0 C3 64 86 E6 F6 07 13 3A BE 60 EF 59 9E 1E 84 1D 0D F1 B0 E6 8B 08 5F E2 30 4F 89 7F A2 5B E3 9D 52 BD 66 38 A7 75 4B C4 96 12 2E D3 D4 93 71 4B D5 A1 A5 E5 A4 60 A6 29 AA 40 78 3E 2A F3 1C 35 A1 8B 31 11 19 F2 33 AD 2B 91 A3 AF F4 32 9C 43 10 D4 F0 2F 68 71 D5 7C FE DF 34 22 FD 21 0A 5D 7B A5 86 83 7C 4B F2 23 30 98 43 09 9C C8 D2 39 E4 5D B6 F6 58 6C 72 F9 40 51 54 21 9B 70".replace(' ','')
#m = int(msg,16)
#print(msg)
#print(m)
#print(N)
#print(binascii.unhexlify(hex(pow(m,d,N)).replace('0x','')))



n0 = "BED09481E6C5438DEA330688659FB0DDA3B934924B86D522F131D41A4FDD49CA066346BA716D2B2AE6B0AA655EA1C72FC78672532E21B4EA5E268AA321B8A31C5FFAB1A0F7E83BC37892999729D9BA322465237FCB00AC683B16CA9AA40C84496857C6018D8FC7C58F397D0656E8B6C85553F9A14F61965FECE0B85EEEE99B8128BF8B4CFFE25BE78A4B269944320138D45F4A16C84192AB5895FC64A4F2796A87234B48C46F2DF8719F28EFDAD022118652E3D25E44DA3E51FC13344E1C3ABD75E40C624949B29375BAB36E1FF9A692DF39EADCA179F26B4417CD5D71201F7DEEF7BD0533394157EB9CD292602C481448C3C20A36E189D7733B12AC39888F3B"
n1 = "BA05F0CCE54B987C3EDADD20FE386AFC91BBA05F6BC9592D5EE3D4FD430D7DC31503F5857A6C75695B46AA93FF792C55C3F7FC814A59B50F01037C7A66BD9A8AB2813B459FC7604F0CBF3E7B4AECA875B6C080685759F84E0956A276A9F789DF9A6CF5D32ED0ED28D05730D068089FBFA2CE6C4DAC9A2B82090A1B84019A3F699E0D26B8E0CD19B90980970D3231BF9BE17C12E970B05F4252D98B78470E75C61B4157489D41CDDA72B2E0EC9F7E310ADFB8BFF29DE344654CBFEE7243280B1F821FE5C90239A850AA4BE43D50C4202352CC97B211D7CB728A142CF2DF7AD73999119D478DFB676A943C5B7CAE30BA0E1A274E23D4CC635504B4B454C717F621"
n2 = "ABC757E220D1F0DA46D017D0542273FAAEACA99D68EA3B400F99752B5DEBDB67AE3107D8F491F917BA079E14708F702FC8FC1A6189FC1F41EBA334482695642AFC8083D53DDA77B0B58C251926ED779446A137BBC4EFE3572B0D61DFC1A524C2C7891A6DE6BDA5B15B1604284CCA98B97F6E60974CB17F0A5B1A17BEF2007E02FA8A8BF0E0269DE44DAC25C7C7826CBAC2019435373E887658E5FAF733E08AE04A052FA51447FFFB3B9EEDF7FEEC0C8E62AB0E51C516DB537EE93D9F780B20E1665D8E9E541D5E8DE9AA2EA1447B56D07770A2E5B72CAA0891988D97B77F38274830814BD48E338800B0837FEF4135BAD88F5178941406CFDB831FE18171A13F"

c0 = "be 35 c9 bd 68 ac f7 9b 5c db 91 be c3 10 b9 6a 00 a5 08 91 41 f6 f5 2c 94 5c 95 f8 8e 1b 4a 2c 12 e1 29 ba 93 c7 85 eb 51 22 cc aa 38 85 91 70 44 e9 4e dc 28 b7 61 06 93 ac 09 be 63 df ea 11 b3 3b 6a cb f0 29 37 8f 29 7f 9c 2d 53 7a d6 5d 31 c5 f4 cb f0 27 68 5e 44 44 da b4 9c ce 9d 40 cf 39 85 cf cd ce 1e 0b 33 5f f5 9f ee 48 16 53 83 3b df e7 9f 3e f5 3d 16 67 16 39 ab 9a 92 b7 49 67 1f 01 d0 4a c9 e5 c6 16 35 2d 19 09 a9 b4 36 5c fe a4 84 aa 75 22 7a 31 2c f4 12 4e b6 52 56 f7 7a 2f 08 e3 51 4e 74 7b 5d f2 68 42 ed d7 e9 75 f9 95 2c e4 84 5b 8c 84 9e 7e 62 b8 c5 b4 c9 db d6 d3 9e 5d a1 d2 dc f5 12 9c bc 96 9f 1f d7 b7 cd ff 3f 4b 5f d1 39 15 d9 a1 41 d6 9c 15 c1 10 53 a5 f2 25 57 cf bd 06 70 34 cf cc 88 71 87 a8 a6 8b 4c a7 2d b5 7a f2 a5 b6 bf 0d 97 45".replace(' ','')
c1 = "32 2e 0c 9e 86 d5 69 bb 75 f9 0e d1 ff 46 88 60 10 69 79 1c 4f 46 e4 7a 82 48 6b fd 66 f0 fc 3d b7 cb 0b b6 29 b5 18 05 a6 f6 5d b1 20 b9 1c fc cb 30 65 c5 27 1b 16 38 db f7 c0 ee 20 bc 54 46 81 4d f2 53 4a 54 92 d2 dd df c8 ac 61 ab d2 18 e8 71 bc f6 ee e0 52 f7 b8 6c 79 7d 12 e2 77 7e 04 be 8b 52 7d 28 ee a7 bf c8 2a a4 ed 8d 2d 12 18 5c b9 23 2b 1a 7f e5 f4 df fa 52 38 0d df c4 f2 a3 2b d5 6d dd 54 1f a0 47 18 b7 63 f6 0e 49 44 12 80 bd c1 ae 9b 29 9f 88 4d 2a 4b b2 0e 9c cd e6 37 95 bc 81 12 5a 10 60 e4 84 38 a6 db 53 e6 d5 88 36 19 10 49 fb 3e c2 f0 01 32 f8 3c fa 38 5b d6 b8 3b 18 db 81 9b fb ae 37 0f b2 ab 98 53 9b 27 59 fc 43 29 9e fd 8d 5b 7e f0 64 1b ec 5d bc 6a 01 cf 24 2b 94 34 f5 d9 08 e4 7e 8a 9b df b1 cd ac 65 14 0f 97 23 da ae 78 83 2a 7c d3".replace(' ','')
c2 = "84 c4 15 56 ca 45 1a 1e cd c4 2a 8b 7f b0 d5 b6 8d ce c6 00 cb 9f d9 fd 80 e0 a3 3a 31 0e 62 18 bf 57 06 77 69 d1 6c 6c 12 fe cc b6 71 60 d7 64 28 b3 56 08 d4 64 b5 1c 29 9d 6a e2 12 c5 b5 b8 39 d5 b7 62 db c5 22 ef 8e f4 4a 6d 1f e1 ca fa 58 fb 45 14 64 54 ba c0 25 90 8c 6c b1 53 27 43 c5 0f 3c 8c d3 39 75 8e 7c ff 59 f1 b1 dd 38 23 79 f7 32 df 7b 4a ea b0 04 dd 7e e1 54 b7 4a ca ad 6d 1d 06 53 50 bb 38 39 0f a0 27 86 55 dd cf 36 41 87 3e 06 d3 ed 0c cc c3 19 7a dc f9 77 8b fb 29 d0 8d bf 82 a4 a7 2a ee 42 0d 2e de d9 61 0b cf 48 5f 88 e2 76 bf 64 6f 22 89 f6 10 46 cf c3 1d 7f eb 3c 59 94 c8 47 b8 65 c7 35 92 83 b7 2a 9e e8 37 7e 10 88 e9 c2 14 05 5b 77 87 ed f0 c8 8a b4 5b 68 f3 d7 01 8b 28 ca 94 b9 78 50 f7 98 85 94 b3 8c 95 38 7f 72 92 47 4a 43 d1 4d c2".replace(' ','')

N0 = int(n0,16)
N1 = int(n1,16)
N2 = int(n2,16)

C0 = int(c0,16)
C1 = int(c1,16)
C2 = int(c2,16)

M0 = N1*N2
M1 = N0*N2
M2 = N0*N1

Mi0 = modinv(M0,N0)
Mi1 = modinv(M1,N1)
Mi2 = modinv(M2,N2)

print(Mi0)
print(Mi1)
print(Mi2)
print()

print(N0)
print(N1)
print(N2)
print()

print(C0)
print(C1)
print(C2)
print()


p0 = (C0*M0*Mi0)%(N0*N1*N2)
p1 = (C1*M1*Mi1)%(N0*N1*N2)
p2 = (C2*M2*Mi2)%(N0*N1*N2)
y = (p0+p1+p2)%(N0*N1*N2)
print(y)

#from decimal import *
#
#getcontext().prec = len(str(y))
#
#c = Decimal(y)
#power = Decimal(1)/Decimal(3)
#
#answer = pow(c,power)
#ranswer = answer.quantize(Decimal('1.'), rounding=ROUND_UP)
#
#print(ranswer)

sq = 8388131359720046063872833100811325574570587786581033027443036972651370077226249633121066183702174905601194465162357203577717819386494559177357917520660217340214386313732889000995729043726276593413446227015142952546721646496051966772341834642570390834410121150397884781773266075473849193791775472457384434191196865262762067763768895485761779044905909446640835467821924369760638688355298154242940763320223330690939894916560502053278601601747985596894083811725949290750309782142188283705393989948406653725691406575786268881626886111264816551591864627974415487282240166658800843761054383756438874711807710508977464811552
print(y==pow(sq,3,N0*N1*N2))
print(hex(sq))
