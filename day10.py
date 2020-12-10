with open("day10.txt", "r") as data_file:
    sl= data_file.readlines()
from functools import reduce
import string
from collections import Counter
import copy
from itertools import product, permutations, combinations

def strip_list(data_strings):
    return [int(line.strip()) for line in data_strings if len(line.strip()) != 0]

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
data.append(0)
data.append(max(data)+3)
data.sort()
import numpy as np
data_n = np.array(data)
diffs = np.diff(data_n)
print(np.max(diffs))
print(np.min(diffs))
print(np.count_nonzero(diffs == 1) * (np.count_nonzero(diffs == 3)))


##part 2

keep = []
for i in range(1,len(data)-1):
    if data[i] - data[i-1] == 3  or data[i+1] - data[i] ==3:
        keep.append(data[i])

data_set = set(data)
options = data_set - set(keep)
options = list(options)
print(keep)
keep.append(0)
keep.append(max(data))
keep.sort()
print(keep)
print(data)
def its(start, stop, nums):
    ways = [list(combinations(nums, i)) for i in range(0,len(nums)+1)] ##that plus one man god damn it
    w = [list(x) for sub in ways for x in sub]
    #print(w)
    good = 0
    for l in w:
        l.append(start)
        l.append(stop)
        l.sort()
        l = np.array(l)
        l = np.diff(l)
        if np.max(l) <= 3:
            good += 1
    if good == 0:
        print(w)
    print(good)
    return good

cut_left = 0
print("hel")
ways = 1
for val in keep:
    cut_right = data.index(val)
    if len(data[cut_left+1:cut_right]) <2:
        print("hello")
        pass
    print("hey")
    ways = ways * its(data[cut_left] , data[cut_right], data[cut_left+1:cut_right])
    cut_left = cut_right

print(ways)