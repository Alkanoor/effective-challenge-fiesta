from util import *


clear_msg = clean_text(open('input_test').read())[:2000]
clear_msg = "BONJOURMADAME"

random_grid = craft_random_grid(False)
print(sorted(random_grid[0].items()))
print(sorted(random_grid[1].items()))

random_key = [0,3,1,2]
ciphered = cipher(random_key,random_grid[0],clear_msg,False)
print(ciphered)
deciphered = decipher(random_key,random_grid[1],ciphered)
print(coincidence(deciphered))

print(coincidence(''.join([chr(randint(ord('A'),ord('Z'))) for _ in range(400)])))
print(coincidence_bigrams(ciphered))
