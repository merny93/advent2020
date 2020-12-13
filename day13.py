with open("day13.txt", "r") as data_file:
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

data = strip_list(sl)

start = int(data[0])

bus = [int(x) for x in data[1].split(",") if x != "x"]
print(bus)
# import numpy as np

# bus = np.array(bus)
# for i in range(1000):

#     leave = (start+i)%(bus)
#     if np.min(leave) == 0:
#         print("hey")
#         break

# print(leave)
# print(bus[np.argmin(leave)] * i)

# # depart = 1068700
# # while True:
# #     depart += 1
# #     won = True
# #     for idx, cond in enumerate(data[1].split(",")):
# #         if cond == "x":
# #             pass
# #         else:
# #             cond = int(cond)
# #             if (depart+idx)%cond!=0:
# #                 won = False
# #                 break
# #     if won:
# #         print(depart)
# #         exit()
# #     print(depart)

# Python 3.6
from functools import reduce
def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod
 
 
 
def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1
 
 
n = list(bus)
a = reduce(lambda x, y: x + [int(y) - len(x)] if y != "x" else x + ["x"], data[1].split(","), [])
a = list(filter(lambda x: False if x == "x" else True, a))
print(a)
print(chinese_remainder(n, a))