with open("day12.txt", "r") as data_file:
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


pos = [0,0]
directs = ["E", "N", "W", "S"]
direct = 0
inst_list = strip_list(sl)
for inst in inst_list:
    if inst[0] == "N":
        pos[0] += int(inst[1:])
    if inst[0] == "S":
        pos[0] -= int(inst[1:])
    if inst[0] == "E":
        pos[1] += int(inst[1:])
    if inst[0] == "W":
        pos[1] -= int(inst[1:])
    if inst[0] == "R":
        if int(inst[1:]) == 90:
            direct -= 1
        if int(inst[1:]) == 180:
            direct -= 2
        if int(inst[1:]) == 270:
            direct -= 3
    if inst[0] == "L":
        if int(inst[1:]) == 90:
            direct += 1
        if int(inst[1:]) == 180:
            direct += 2
        if int(inst[1:]) == 270:
            direct += 3
    if inst[0] == "F":
        dire = directs[direct%4]
        if dire == "N":
            pos[0] += int(inst[1:])
        if dire == "S":
            pos[0] -= int(inst[1:])
        if dire == "E":
            pos[1] += int(inst[1:])
        if dire == "W":
            pos[1] -= int(inst[1:])

print(pos)

way = [1,10]
pos = [0,0]

import numpy as np


for inst in inst_list:
    if inst[0] == "N":
        way[0] += int(inst[1:])
    if inst[0] == "S":
        way[0] -= int(inst[1:])
    if inst[0] == "E":
        way[1] += int(inst[1:])
    if inst[0] == "W":
        way[1] -= int(inst[1:])
    if inst[0] == "F":
        pos[0] += (way[0])*int(inst[1:])
        pos[1] += (way[1])*int(inst[1:])
    if inst[0] == "R":
        rot_mat = np.array([[np.cos(np.deg2rad(int(inst[1:]))), - np.sin(np.deg2rad(int(inst[1:])))],[np.sin(np.deg2rad(int(inst[1:]))), np.cos(np.deg2rad(int(inst[1:])))]], dtype=int)
        way = np.array(way)
        pos = np.array(pos)
        way = np.dot(rot_mat, way)
        way = list(way)
        pos = list(pos)
    if inst[0] == "L":
        rot_mat = np.array([[np.cos(np.deg2rad(-int(inst[1:]))), - np.sin(np.deg2rad(-int(inst[1:])))],[np.sin(np.deg2rad(-int(inst[1:]))), np.cos(np.deg2rad(-int(inst[1:])))]], dtype=int)
        way = np.array(way)
        pos = np.array(pos)
        way = np.dot(rot_mat, way) 
        way = list(way)
        pos = list(pos)

print(pos)