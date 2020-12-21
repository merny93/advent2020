with open("day21.txt", "r") as data_file:
    sl= data_file.readlines()
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


foods = strip_list(sl)

alergens = [x.split("contains ")[-1][:-1].split(", ") for x in foods]
alergens = [y for x in alergens for y in x]
alergens = list(set(alergens))

ing_list = [x.split(" (")[0].split(" ") for x in foods]
ing_list = [y for x in ing_list for y in x]
ing_list_dup = copy.deepcopy(ing_list)
ing_list = list(set(ing_list))
print(alergens)
print(ing_list)

alrg = {}
for i in alergens:
    alrg[i] = list()

for food in foods:
    ingrediants = food.split(" (")[0].split(" ")
    alergens = food.split("contains ")[-1][:-1].split(", ")
    for alergen in alergens:
        alrg[alergen].append(set(ingrediants))

print(alrg)
for steps in range(1):
    for alergen in alrg:
        print(alrg[alergen])
        alrg[alergen] = reduce(lambda x,y: x.intersection(y), alrg[alergen])
print(alrg)

ingrediants_copy = copy.deepcopy(ing_list)
print(ingrediants_copy)

for a in alrg:
    for al in alrg[a]:
        if al in ingrediants_copy:
            ingrediants_copy.remove(al)

print(ingrediants_copy)
count = 0
for safe_ing in ingrediants_copy:
    count += ing_list_dup.count(safe_ing)
print(count)
print(alrg)

the_res = []
prev_len = -1
while len(the_res) != prev_len:
    prev_len = len(the_res)
    print(prev_len)
    for key in alrg:
        if len(alrg[key]) == 1:
            #found a unique pair:
            the_res.append([list(alrg[key])[0], key])
            for key1 in alrg:
                if the_res[-1][0] in alrg[key1]:
                    alrg[key1].remove(the_res[-1][0])

print(alrg)
print(the_res)
the_res.sort(key = lambda x: x[1])
print(the_res)
power_law = reduce(lambda x,y: x+","+y[0], the_res, "" )[1:]
print(power_law)