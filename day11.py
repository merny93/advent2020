with open("day11.txt", "r") as data_file:
    sl= data_file.readlines()
# with open("test11.txt", "r") as data_file:
#     sl= data_file.readlines()
from functools import reduce
import string
from collections import Counter
import copy
from itertools import product, permutations, combinations

def strip_list(data_strings):
    return [list((line.strip()).replace("L", "1").replace(".", "0")) for line in data_strings if len(line.strip()) != 0]

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

vals = strip_list(sl)
vals = [[int(x) for x in r] for r in vals]
import numpy as np
seats = np.array(vals)
seats = np.pad(seats, ([1,1],[1,1]))
seats = np.zeros_like(seats)
rez = seats.copy()
print(rez.shape)
for i in range(1000):
    template = np.array(vals)
    template = np.pad(template, ([1,1],[1,1]))


    for row in range(1, template.shape[0]-1):
        for col in range(1,template.shape[1]-1):
            if template[row,col] == 0:
                pass
            elif np.sum(seats[row-1:row+2, col-1:col+2]) - seats[row,col] >= 4:
                rez[row, col] = 0 
            elif np.sum(seats[row-1:row+2, col-1:col+2]) - seats[row,col]== 0:
                rez[row,col] = 1
            
    if (seats==rez).all():
        print("finished early")
        break
        

    seats = rez.copy()
    #print(np.sum(seats))
    # print(seats.size)
print(np.sum(seats))
#print(seats[-10:,-10:])


dirs = [[1,0],[-1,0],[0,1],[0,-1],[1,1],[-1,1],[1,-1],[-1,-1]]
for i in range(1000):
    template = np.array(vals)
    template = np.pad(template, ([1,1],[1,1]))


    for row in range(1, template.shape[0]-1):
        for col in range(1,template.shape[1]-1):
            if template[row,col] == 0:
                pass
            else:
                neighs = 0
                for d in dirs:
                    for depth in range(1,1000):
                        p_r = row + depth*d[0]
                        p_c = col + depth*d[1]
                        if p_r<0 or p_c<0 or p_r >= seats.shape[0] or p_c >= seats.shape[1]:
                            break
                        
                        xx = seats[p_r,p_c]
                        if xx ==1:
                            neighs += 1
                            break
                        if template[p_r,p_c] == 1:
                            break
                if neighs >=5:
                    rez[row, col] = 0
                elif neighs== 0:
                    rez[row,col] =1      
    #print(rez)            
    if (seats==rez).all():
        print("finished early")
        break
        


    seats = rez.copy()
    #print(np.sum(seats))
    # print(seats.size)
print(np.sum(seats))