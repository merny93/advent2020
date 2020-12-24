with open("day24.txt", "r") as data_file:
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

N = 150
grid = np.zeros((N,N), dtype=int)

instruction = strip_list(sl)
inst_set = {"e": [0,1], "ne": [-1,0], "nw": [-1,-1], "w": [0,-1], "sw": [1,0], "se": [1,1]}

for inst in instruction:
    inst = list(inst)
    pos = [N//2,N//2]
    while True:
        cur = ""
        while True:
            #print(cur)
            cur = cur + inst.pop(0)
            if cur in inst_set:
                break
        pos = [pos[i] + inst_set[cur][i] for i in range(2)]
        if len(inst) == 0:
            break
    
    grid[tuple(pos)] = (grid[tuple(pos)] + 1)%2
    # print(np.sum(grid))

print(np.sum(grid))
import matplotlib.pyplot as plt
plt.ion()
for step in range(100):
    new_grid = np.array(grid, dtype=int)
    #print(np.sum(new_grid))
    for x in range(N-1):
        for y in range(N-1):
            num = 0
            for key in inst_set:
                pos = [[x,y][i] + inst_set[key][i] for i in range(2)]
                #print(pos)
                num += grid[tuple(pos)]
            if new_grid[x,y] == 1 and (num ==0 or num >2):
                #print("death")
                new_grid[x,y] = 0
            elif new_grid[x,y] == 0 and num==2:
                #print("birth")
                new_grid[x,y] = 1
    grid = new_grid
    plt.clf()
    plt.imshow(grid)
    plt.show()
    plt.pause(0.1)
    print(np.sum(grid))
            
