import numpy as np
from util import *


msg = 'XAFAFFDXFFAFVDXAGDFGAVAVXAFAGDGFVFXAGDDGVDVDXADADGFAFXXAGDGDGXVXVDXAAVVXFGFAXGVGVXGFXGDGFAFAGFXDGXXAVDXAXVFFDADGVXGDVAGXGFGDGDGXVXVDXAAVVXFGFAXGAVVXDGFAAADGGFGDFXXAVDDGGFGDFAXAVDXAXVXFDADGGFDAXAFADGAADGGFXAFAXGFXGFVXXAAAXGXADAXAFAXGVADGVXGFGDFAGXVDFAXAGDDGVFDGGFXGDGVDFGVXGDFGGXGDXAVAVXFGFXGXGFVXDGGFXGVDDGVAVXFGAAGVDGGFFAXAFGAVAVXAFAGDGFVFXAXAFAFAXADAGFXAVDXAXGVXDGVFDGGFVDFXXAFAFGGDAAVXGGVAXGFGVDFGXXGXXAGDFXXAVFDGGFXGVAXAVXDAXAXGXGVXXAFXXAVDXAGDDGVFFGGFVXDGVFXAAAXAAGDGAAXGGFXGGXFXXAVDXAFAFGGXVFXADGGXAAGVGFAVAVVXXADGVDVDXADADGFAFXDAGFGDXAFAGDXAVXVFGFAAXAXAFADADGVXGDFFDXFFAFFAGXXGGFVDGFGDDGGFXGXDGXXAAAGFFAXDVDXAXGXGVXXAGDDGFXAVXXAGAAXAGDGGGDXGXADAXAXGVXXAGDAAFGDAVAVDGFXDGXXAFAXAAAXAGDGDGFXGDGGFXGVDXADAVAVDFGGFFXXAFXXAGXAGAAVDXAGDAAGVDGFAXXXAXAGDAAGVDGXDGXXAFVFGGXVXFXXAGDVDXAGADGVFVXGFVDVDXAAADGVAGFXGDGGFFAXAXXFVVADGGFFAVFGFFADGVFDGGFXGFXXAAAFGGXVFXAVXXGVADGVXVDXAXGGXFXXAFXXAGDDAXAGDGDDGXXXAGDAAGVGFAVAVVXXAGDFXGXFFXAVXDGVFVXGFVDVDXAGDFXXAGXAGAAVDXAGDGXXGGFVDGFGDXAXAGDXAXGVXXAAAFGFAGDXGGFXGGXXAVDXAGDGGGDXGXADAXAFXXAAAGVGFAVAVVXXADAXAFAXGDADGGFGDVDXAFFXAVXFVGXGFFAXAFAVAVDXAGFFAXAAAVXGFGDXAFXXAVDFGAVAVXAFAGDGFVFXAGDGXVXVDDGGFGDFAXAVDXAGDDGVDVDXADADGFAFXGDDGFVFGGXXGXAVXXAFAXGGXFAXAGDGFAGGFXADAXAVDXAXGXGVXXAVDXAVFDAXAXGXGDGFAXGFAFGGDGDXAVXVFGFAAXAGDDGGXAGVAVXGFGDXAGDDGVFXAAAGXFAXAFXGFAVAVGFAAGXVDXGXAFAFGGXVFXAVDVDXAVDXAXVFVGXGFFAVDXAAADGVAGFXGDGGFFAXAVADGGFFAVFGFFADGVFDGGFXGVXXAGDFGVDGXVDXAVAVXFGVGVDXADAXAXAXGVXXAGDXGGFXGGXXAVDXAGDFXXAGXAGAAVDXAGDXAVDVDXAGDVAXAVXDAGFVXXAFAXGVDXAFXXAAAVXGGVAXGDGXXXAFXXAXGFGGXGDVDXAGDDAXAGDGDDGXXXAGDAAGVGFAVAVVXXAGDAADGVAXGXAGDVDXAFFXAVXFVGXGFFAVADGVXDAGFAAXAGXAGAAGFAVGFXXGXVXDGGFXGGXFAVXDGFXGFFGXXVXDGDADAXADGFXVXXAGDGDXAVADGVXVDXAGVDGGXXGAAFGDADADGFAFXXADAXAFAXGDGVDVDXADADGFAFXDGGXFAXADAFXDGVXDAXAXAVXXAVAXAVXXAVADGVXVDDGVXDGFXGFFGXXFGFAGFFGDAXAXGVXGFXAFXDGFAGDVDDGVXXAXXGFFGFAVXXADADGGXXXGFGDXGGFVDVDFGVDFGGGDGVDXAGDXGFXXADAFGFAXGFXGFFXGFXAVXDGAAAAXAVDXAVXXAVXVDDGDAFGFAXGXAXAFXXAGDDAGXFAGFXGGFFGFAGDVAFGGFFAXGDAXADAXAVAXAFAFXDGFAXGVDXAFVFGGXVXVADGVXXGFGGXXGFGGXVDFGFAFAXAGDXGVADGGDVFGXVDXAAVVDDGXXXAGDXGAAFGFXXADGFXAVXXVFAGGDGXAADDGDFFDXFFAFXGGVXAAVVDDGXXGFGDAAFGFXXADGFXAVXXVFAGGDGXAADDGDFFDXFFAFVDXAGDFXGFVFGFGDGFFGFAGDFXGXXXXAFAXAVXDGVDDADGFAXXGFFAAVGXVXXAFAXGFXFGFAAAAAFGFAAAXAFAXGVXXAXAGDFXXAGDVDXAGDVAVXXADAGFXAVXGDFVFGGXVXGDFXXAFVGXGFFAAVDGAAXADGGXVAFGGFFAXGVAVXXAAAGFGDFGGXGDXAFXXAAAVDXAFAAAGVDGVDXADXFVGXGFFAVDFGAVAVXAFAGDGFVFXADGVDVDXADADGFAFXXAAAXAVDVDXAAAGFXAAAGVFGGXDGVDDGVAFGVXXGXAFXXAVADGVXGFGDXAXGDGGFXGFXXAAVGFFAGFXGGFVFXADAXAFAXGAVXAVXDAXAXADGVDXAFAFAXADAGFVAFGGXVXFAFGGXGDAAXAVDVDXAFXXAVDDGVFGFAAXGFGGFVXXADGVDVDDGGFXGGDFGGXVFVXGFVXXXXXX'

clear_msg = clean_text(open('input_test').read())[:2000]
# print(clear_msg)
# exit()

random_grid = craft_random_grid(False)
print(sorted(random_grid[0].items()))
print(sorted(random_grid[1].items()))

random_key = [1,3,5,2,0,4]
ciphered = cipher(random_key,random_grid[0],clear_msg)

ciphered = clean_text(open('challenge').read())
ciphered = clean_text(open('commcomm').read())

def find_key_length(m,length_range):
    final_array = np.array([])
    for i in length_range:
        print("===================")
        print(i)
        analysed_array = np.array([])
        for chosen_column in range(i):
            max_coincidence_indice = -1
            block_size = len(m)//i
            for j in range(i):
                for offset1 in range(4):
                    for offset2 in range(4):
                        if j != chosen_column:
                            to_analyse = ''
                            for k in range(block_size):
                                if offset2+j*block_size+k<len(m) and offset1+chosen_column*block_size+k<len(m):
                                    to_analyse += m[offset1+chosen_column*block_size+k]+m[offset2+j*block_size+k]
                            coincidence_indice = coincidence_bigrams(to_analyse)
                            if coincidence_indice>max_coincidence_indice:
                                max_coincidence_indice = coincidence_indice
            analysed_array = np.append(analysed_array,max_coincidence_indice)
        print("For length "+str(i)+" we have "+str(analysed_array.mean())+" and "+str(analysed_array.std()))
        final_array = np.append(final_array,analysed_array.mean())
    print("Finally the array has a mean "+str(final_array.mean())+" and a std "+str(final_array.std())+" => argmax = "+str(final_array.argmax()+length_range[0])+" with different : "+str(final_array.max()))
    return final_array.argmax()+length_range[0]

l = find_key_length(ciphered,range(2,10))
print(l)

def find_key_smart(m,key_length):
    for chosen_column in range(key_length):
        max_coincidence_indice = -1
        max_coincidence_indice2 = -1
        block_size = len(m)//key_length
        for j in range(key_length):
            for offset in range(4):
                if j != chosen_column:
                    to_analyse = ''
                    for k in range(block_size):
                        if offset+j*block_size+k<len(m) and chosen_column*block_size+k<len(m):
                            to_analyse += m[chosen_column*block_size+k]+m[offset+j*block_size+k]
                    coincidence_indice = coincidence_bigrams(to_analyse)
                    if coincidence_indice>max_coincidence_indice:
                        max_coincidence_indice = coincidence_indice
                        index_max = (chosen_column,offset,j)
                    elif coincidence_indice>max_coincidence_indice2 and coincidence_indice<max_coincidence_indice:
                        max_coincidence_indice2 = coincidence_indice
                        index_max2 = (chosen_column,offset,j)
        print(index_max)
        print(index_max2)

import itertools

def find_key_BF(m,key_length):
    quotient = len(m)//key_length
    remainder = len(m)%key_length
    M = -1
    for perm in itertools.permutations([i for i in range(key_length)]):
        to_analyse = ''
        begin_block = [0 for _ in range(key_length)]
        cur = 0
        for i in perm:
            begin_block[i] = cur
            cur += quotient
            if i<remainder:
                cur += 1

        for k in range(len(m)):
            to_analyse += m[begin_block[k%key_length]+k//key_length]
        coincidence_indice = coincidence_bigrams(to_analyse)
        if coincidence_indice>0.06:
            print(coincidence_indice)
            print(perm)
            if coincidence_indice>M:
                M = coincidence_indice
                ret_perm = perm
                ret = to_analyse
    return (M,ret_perm,ret)

print(find_key_BF(ciphered,l))
exit()



analysed_array = np.array([])
max_coincidence_indice = -1
for i in range(2,12):
    print("===================")
    print(i)
    for offset in range(1,i):
        to_analyse = ''
        if i%2==0:
            M = i
        else:
            M = 2*i
        for j in range(0,len(ciphered),M):
            if j+offset<len(ciphered):
                to_analyse += ciphered[j]+ciphered[j+offset]
        coincidence_indice = coincidence_bigrams(to_analyse)
        print(coincidence_indice)
        analysed_array = np.append(analysed_array,coincidence_indice)
        if coincidence_indice>max_coincidence_indice:
            max_coincidence_indice = coincidence_indice
            index_max = (i,offset)

print("We found a maximum "+str(max_coincidence_indice)+" for index "+str(index_max))
