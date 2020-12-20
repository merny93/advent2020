with open("day18.txt", "r") as data_file:
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

expressions = [x.split(" ") for x in strip_list(sl)]


def del_par(ls):
    short = []
    write = False
    num_dangle = 0
    for val in ls:
        if val == "(":
            write = True
            num_dangle += 1
        elif val ==")":
            num_dangle -= 1
        if write:
            if num_dangle == 0:
                return short[1:]
            else:
                short.append(val)

def eval_s(exp_s):
    exp_s = reduce
eval_s = lambda x: reduce(lambda x,y: x+[y] if )

def eval(exp):


res = []
for exp in expressions:
