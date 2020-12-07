with open("day7.txt", "r") as data_file:
    sl= data_file.readlines()

from functools import reduce
import string
from collections import Counter

##read in if the seperator is enters
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
#get rid of pesky new lines
def strip_list(data_strings):
    return [line.strip() for line in data_strings if len(line.strip()) != 0]

##write here
import numpy as np

data_stripped = strip_list(sl)


mat = np.zeros((len(data_stripped), len(data_stripped)), dtype=int)
bag_types = []
for line in data_stripped:
    bag_types.append(line.split("bag")[0][:-1])
#print(bag_types)



for idx, line in enumerate(data_stripped):
    rules = line.split("contain ")[-1]
    rules = rules.split(", ")
    if rules == ['no other bags.']:
        continue
    for rule in rules:
        idy = bag_types.index(rule.split(" bag")[0].split(" ", 1)[1])
        mat[idx,idy] = int(rule.split(" ")[0])
mat = mat.T
print(mat)

N = 100

good_idx = bag_types.index("shiny gold")
print(good_idx)
count = 0
for i in range(len(bag_types)):
    vec = np.zeros(len(bag_types), dtype=int)
    vec[i] = 1
    res = np.dot(mat, vec)
    if res[good_idx] != 0:
        count += 1
        continue
    for i in range(N):
        res = np.dot(mat,res)
        if res[good_idx] != 0:
            count += 1
            break
        if np.sum(res) == 0:
            break

print(count)

count = 0
vec = np.zeros(len(bag_types), dtype=int)
vec[good_idx] = 1
for i in range(N):
    vec = np.dot(mat, vec)
    the_sum = np.sum(vec)
    count += the_sum
    if the_sum == 0:
        break

print(count)

exit()
print(get_enter(sl)[-1])
print(strip_list(sl)[-1])