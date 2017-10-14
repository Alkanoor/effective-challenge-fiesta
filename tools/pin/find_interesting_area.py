import sys
import subprocess

#Popen('pin','-t','~/Téléchargements/pin-3.0-76991-gcc-linux/source/tools/ManualExamples/obj-ia32/inscount_with_difference.so','--',sys.argv[1])

def read_cur(filename):
    content = open(filename).read()
    a = content.split(',')
    return int(a[0]),int(a[1]),int(a[2])

subdivisions = 100

s = Popen('./find_interesting_area',str(subdivisions))
m,M,stride = read_cur('tmp_out')

while stride>1:
    s = Popen('./find_interesting_area',str(subdivisions),str(m),str(M),str(stride))
    m,M,stride = read_cur('tmp_out')

#entre grigy et viry chatillon
