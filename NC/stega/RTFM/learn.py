#!/usr/bin/python

import io
import os
import re
import numpy as np
from PIL import Image



def load_table_basic(path):
    with open(path) as f:
        content = f.readlines()

    ret = {}
    for i in range(0,len(content),2):
        char = content[i][0]
        t = content[i+1].split('\n')
        ret[char] = int(t[0])

    return ret

def save_table_basic(path, table):
    with open(path,'w+') as f:
        for u in table:
            f.write(u)
            f.write('\n')
            f.write(str(table[u]))
            f.write('\n')

def load_table(path):
    files = os.listdir(path)

    ret = {}
    for f in files:
        ret[f.strip(".png")] = Image.open(path+"/"+f)

    return ret

def save_table(path, table):
    for u in table:
        table[u].save(path+"/"+u+".png")

def compute_sum(im1, im2, offx, offy):
    s = 0
    n = 0
    if im1.size != im2.size:
        print("Sizes don't match ... ")
        exit()
    sizes = im1.size
    if offx>=0:
        for i in range(offx,sizes[0]):
            if offy>=0:
                for j in range(offy,sizes[1]):
                    s += abs(im1.getpixel((i-offx,j-offy))[0]-im2.getpixel((i,j))[0])
                    n += 1
            else:
                for j in range(-offy,sizes[1]):
                    s += abs(im1.getpixel((i-offx,j))[0]-im2.getpixel((i,j+offy))[0])
                    n += 1
    else:
        for i in range(-offx,sizes[0]):
            if offy>=0:
                for j in range(offy,sizes[1]):
                    s += abs(im1.getpixel((i,j-offy))[0]-im2.getpixel((i+offx,j))[0])
                    n += 1
            else:
                for j in range(-offy,sizes[1]):
                    s += abs(im1.getpixel((i,j))[0]-im2.getpixel((i+offx,j+offy))[0])
                    n += 1
    return float(s)/float(n)


def moy(basis,next,coeff):
    if basis.size != next.size:
        print("Sizes don't match ... ")
        exit()
    s = basis.size
    tmp = Image.new(mode="RGB",size=s)
    for i in range(s[0]):
        for j in range(s[1]):
            t = basis.getpixel((i,j))[0]*coeff+next.getpixel((i,j))[0]
            t = int(float(t)/float(coeff+1))
            tmp.putpixel((i,j),(t,t,t))
    return tmp


def index_of_nearest(f, table):
    m = -1
    index = '?'
    for u in table:
        tmp_m = -1
        for offx in range(-1,2):
            for offy in range(-1,2):
                tmp = compute_sum(f,table[u],offx,offy)
                if tmp<tmp_m or tmp_m<0:
                    tmp_m = tmp
        if tmp_m < m or m < 0:
            m = tmp_m
            index = u

    return index

def log(table):
    for u in table:
        #table[u].show()
        print("Index "+str(u)+" => "+str(table[u].size[0])+";"+str(table[u].size[1]))

def log_basic(table):
    for u in table:
        print("Index "+str(u)+" => "+str(table[u]))


table = load_table("models")
table2 = load_table_basic("counter")
print(table)
print(table2)


def predict_and_ask(img):
    img.show()

    estimated = index_of_nearest(img,table)

    print("Estimated :")
    print(estimated)

    real = raw_input()

    if table.get(real) is None:
        table[real] = img.copy()
        table2[real] = 1
    else:
        table[real] = moy(table[real],img,table2[real])
        table2[real] += 1

    if estimated == real:
        print("Good job !")

    #log(table)
    log_basic(table2)
    save_table("models",table)
    save_table_basic("counter",table2)

def predict(img):
    return index_of_nearest(img,table)


# im = Image.open('cafebabe.jpg')
# im.crop((0,0,65000,33*6)).save('normal_cafebabe.jpg')
# exit()

def frange(x, y, jump):
  while x < y:
    yield x
    x += jump

# lors de l'apprentissage
im = Image.open('out.png')
im = im.convert(mode='RGB')
s = im.size
print(s)
cur = 0
offset = 1
for j in frange(0.0,float(s[1]),16.793):
    for i in frange(0.0,float(s[0]),10.34):
        if cur>=offset:
            print("Cur offset "+str(cur))
            # tmp = Image.new(mode="RGB",size=(13,33))
            print("Examining image at position "+str(i/10)+" ; "+str(j/17))
            tmp = im.crop((int(i),int(j),int(i)+11,int(j)+17))
            # for k in range(13):
            #     for l in range(33):
            #         if i+k<s[0] and j+l<s[1]:
            #             tmp.putpixel((k,l),im.getpixel((i+k,j+l)))
            predict_and_ask(tmp)
        cur += 1

#sur la vraie image
out = open("out.txt","w+")
im = Image.open('normal_cafebabe.jpg')
im = im.convert(mode='RGB')
s = im.size
print(s)
cur = 0
offset = 0
new_res = ""
final_res = ""
for j in range(0,s[1],33):
    for i in range(0,s[0],13):
        if cur>=offset:
            print("Cur offset "+str(cur))
            print("Examining image at position "+str(i/13)+" ; "+str(j/33))
            tmp = im.crop((i,j,i+13,j+33))
            print(tmp.size)

            l = predict(tmp)
            final_res += l
            new_res += l
            print(final_res)
        cur += 1
        if cur%100 == 0:
            print("Writing !!!")
            out.write(new_res)
            new_res = ""
