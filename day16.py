with open("day16.txt", "r") as data_file:
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

import numpy as np



starting = strip_list(sl)
starting = [list(x.replace("#", "1").replace(".","0")) for x in starting]
print(starting)
starting = np.array(starting, dtype=int)

N = starting.shape[0] + 20
grid = np.zeros((N,N,N,N), dtype=int)

grid[7:7+starting.shape[0], 7:7+starting.shape[0], N//2, N//2] = starting
print(np.sum(grid))
conv_mat = np.zeros_like(grid, dtype= int)
conv_mat[:3,:3,:3,:3] = 1
conv_mat = np.roll(conv_mat, -1, axis=0)
conv_mat = np.roll(conv_mat, -1, axis=1)
conv_mat = np.roll(conv_mat, -1, axis=2)
conv_mat = np.roll(conv_mat, -1, axis=3)
conv_mat[0,0,0,0] = 0
print(np.sum(conv_mat))
#print(conv_mat)
for turn in range(6):
    grid_n = np.asarray(np.round(np.fft.ifftn(np.fft.fftn(grid) * np.fft.fftn(conv_mat))), dtype=int)
    new_grid = np.zeros_like(grid, dtype=int)
    new_grid[grid_n==3] = 1
    new_grid[(grid==1)&(grid_n==2)] = 1
    grid = new_grid
    print(np.sum(grid))


print(np.sum(grid))

