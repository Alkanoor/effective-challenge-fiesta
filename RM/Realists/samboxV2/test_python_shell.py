import sys
import os


def parsemsg(cmd):
    commandOutput = os.popen(cmd).read()
    if commandOutput != '':
        commandOutput = commandOutput.split()
        print(str(commandOutput))

while True:
    parsemsg(raw_input())
