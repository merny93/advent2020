# with open("day25.txt", "r") as data_file:
#     sl= data_file.readlines()
# with open("day12t.txt", "r") as data_file:
#     sl= data_file.readlines()
from functools import reduce
import string
from collections import Counter
import copy
from itertools import product, permutations, combinations

def strip_list(data_strings):
    return [line.strip() for line in data_strings if len(line.strip()) != 0]

def get_enter(data_strings):
    chunks = []
    full_vals = []
    for line in data_strings:
        if len(line.strip()) == 0:
            full_vals.append(chunks)
            chunks = []
        else:
            chunks.append(line.strip())
    if len(chunks) != 0:
        full_vals.append(chunks)
    return full_vals

card_p = 19774466
door_p = 7290641

card_loop = 0
card_subject = 7
card_tmp = 1
while card_tmp != card_p:
    card_tmp = (card_tmp*card_subject)%20201227
    card_loop += 1
print(card_loop)


door_loop = 0
door_subject = 7
door_tmp = 1
while door_tmp != door_p:
    door_tmp = (door_tmp*door_subject)%20201227
    door_loop += 1
print(door_loop)


num = 1
for step in range(door_loop):
    num = (num*card_p)%20201227
print(num)