
# coding: utf8

#14
#25
#36

import sys
from PIL import Image

# N = '006424244440a0c4602020446060c06024446424244400473f07477aa025280cb76458468914cf01473f0747002d2d4da5f567e597e3a35383a515e7a1e769e9e941000f6b3aa551eacd0573d6d025e6a919c6b887d7dc4400fd41ff3dd03fdc816de55a8cac3feee5ab48d3c540007c22261d2d38fd9643568ab1d43b714682dd879447004a3e97152aabf50fc4c396edad0d62eb5f9843800200d9134ab53724041492c1b891143b03c6b190945c000007060b155a2b840988aa12aca51be361763cd5b242004fed4d477da3551be1632301b7b9985e272597544600272d250717100d0b1f24132f24192b262d3f011f00'
#
# hexa_chars = [chr(i) for i in range(ord('0'),ord('9')+1)]
# hexa_chars.extend([chr(i) for i in range(ord('a'),ord('g'))])
#
# first_char = {}
# second_char = {}
# T = [[0,1,2,6],[3,4,5,7]]
# for i in range(16):
# 	b = bin(i).split('b')[1]
# 	b = '0'*(4-len(b))+b
# 	b = b[::-1]
#
# 	cur1 = [[False for _ in range(4)] for _ in range(2)]
# 	cur2 = [[False for _ in range(4)] for _ in range(2)]
# 	for j in range(4):
# 		if b[j] == '1':
# 			for k in range(2):
# 				for l in range(4):
# 					if T[k][l] == j+4:
# 						cur1[k][l] = True
# 					if T[k][l] == j:
# 						cur2[k][l] = True
#
# 	first_char[hexa_chars[i]] = cur1
# 	second_char[hexa_chars[i]] = cur2
#
# def sum_cols(c1,c2):
# 	c = [[' ' for _ in range(4)] for _ in range(2)]
# 	for i in range(2):
# 		for j in range(4):
# 			if c1[i][j] or c2[i][j]:
# 				c[i][j] = '1'
# 	return c
#
# s1 = []
# s2 = []
# s3 = []
# s4 = []
# x = 44
# for c in range(0,len(N),2):
# 	if c%x == 0:
# 		s1.append('')
# 		s2.append('')
# 		s3.append('')
# 		s4.append('')
# 	cols12 = first_char[N[c]]
# 	cols34 = second_char[N[c+1]]
# 	col = sum_cols(cols12,cols34)
# 	s1[len(s1)-1] += col[0][0]+col[1][0]
# 	s2[len(s2)-1] += col[0][1]+col[1][1]
# 	s3[len(s3)-1] += col[0][2]+col[1][2]
# 	s4[len(s4)-1] += col[0][3]+col[1][3]
#
# img = Image.new(size=(44,44),mode='RGB')
# for i in range(len(s1)):
# 	for j in range(len(s1[i])):
# 		if s1[i][j]=='1':
# 			img.putpixel((j,i*4),(255,255,255))
# 		if s2[i][j]=='1':
# 			img.putpixel((j,i*4+1),(255,255,255))
# 		if s3[i][j]=='1':
# 			img.putpixel((j,i*4+2),(255,255,255))
# 		if s4[i][j]=='1':
# 			img.putpixel((j,i*4+3),(255,255,255))
#
# img.save('qr.png')
#
# exit()

braille={
		'1':'a','12':'b','14':'c','145':'d','15':'e','124':'f',
		'1245':'g','125':'h','24':'i','245':'j','13':'k','123':'l',
		'134':'m','1345':'n','135':'o','1234':'p','12345':'q','1235':'r',
		'234':'s','2345':'t','136':'u',	'1236':'v','2456':'w','1346':'x',
		'13456':'y','1356':'z','2':',','256':'.','6':'#MAJ#','3456':'#NUMBER#',
		'123456':'é','16':'â','2346':'è','126':'ê','1246':'ë','146':'î','12456':'ï','1456':'ô','23456':'ù',
		'156':'û','1256':'ü','246':'œ',
		'':' ','25':':','23':';','3':'\'','236':'?','2356':'"',
		'356':'"','235':'!','36':'_','26':'#26#','34':'/',
		'12356':'à','12346':'ç',}

braille_number={
		'1':'1','12':'2','14':'3','145':'4','15':'5','124':'6',
		'1245':'7','125':'8','24':'9','245':'0'}

import re
from PIL import Image
from os import listdir
from os.path import isfile, join

onlyfiles = [f for f in listdir('imgs2') if isfile(join('imgs2', f))]
final_files = [0]*(len(onlyfiles))

for i in onlyfiles:
    final_files[int(re.search('[^0-9]([0-9]+)[^0-9]',i).group(1))] = i

res = ''
number = False
print(final_files)
for img in range(len(final_files)):
    im = Image.open('imgs2/'+final_files[img])

    s = im.size
    m = [[0 for i in range(2)] for j in range(3)]
    for i in range(s[1]//5):
        for j in range(s[0]//5):
            if im.getpixel((j*5,i*5))&1 == 1:
                m[i][j] = True
            else:
                m[i][j] = False

    r = ''
    if not m[0][0]:
        r += '1'
    if not m[1][0]:
        r += '2'
    if not m[2][0]:
        r += '3'
    if not m[0][1]:
        r += '4'
    if not m[1][1]:
        r += '5'
    if not m[2][1]:
        r += '6'
    print(m)
    print(r)
    if not number and braille.get(r) is not None:
        if r == '3456':
            print("Number is True !")
            number = True
        else:
            res += braille[r]
    elif number and braille_number.get(r) is not None:
        print("Add number !")
        res += braille_number[r]
        number = False
    else:
        if number:
            res += '['
            res += r
            res += ']'
        else:
            res += '@'
            res += r
            res += '@'
        number = False
    print(res)

N = int('006424244440a0c4602020446060c06024446424244400473f07477aa025280cb76458468914cf01473f0747002d2d4da5f567e597e3a35383a515e7a1e769e9e941000f6b3aa551eacd0573d6d025e6a919c6b887d7dc4400fd41ff3dd03fdc816de55a8cac3feee5ab48d3c540007c22261d2d38fd9643568ab1d43b714682dd879447004a3e97152aabf50fc4c396edad0d62eb5f9843800200d9134ab53724041492c1b891143b03c6b190945c000007060b155a2b840988aa12aca51be361763cd5b242004fed4d477da3551be1632301b7b9985e272597544600272d250717100d0b1f24132f24192b262d3f011f00',16)
print(bin(N))



#from PIL import Image
#from os import listdir
#from os.path import isfile, join
#
#onlyfiles = [f for f in listdir('imgs') if isfile(join('imgs', f))]
#
#im2 = Image.new('RGB',(800,600))
#
#m = 0
#k = 0
#for img in range(0,len(onlyfiles),3):
#    im = Image.open('imgs/'+onlyfiles[img])
#
#    s = im.size
#    all_pix = []
#    for i in range(s[1]):
#        for j in range(s[0]):
#            if im.getpixel((j,i))[3]&1 == 1:
#                if im2.getpixel((j,i)) == (255,255,255):
#                    m += 1
#                im2.putpixel((j,i),(255,255,255))
#            #all_pix.append(im.getpixel((j,i))[3]&1)
#
#    im2.save('out'+str(k)+'.png')
#
#    print("=============")
#    print(k)
#    print("m = "+str(m))
#
##    n = 0
##    for i in all_pix:
##        if i>0:
##            n += 1
#
##    print(n)
##    print(' out of '+str(len(all_pix)))
#
#    k += 1
#
#
#im2.save('out.png')
#
#NC{VideoSt3g4n0}
