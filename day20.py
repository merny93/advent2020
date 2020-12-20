with open("day20.txt", "r") as data_file:
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

tiles = get_enter(sl)
seen = {}

for tile in tiles:
    tile_num = tile[0].split(" ")[-1][:-1]
    top_border = tile[1].replace("#","1").replace(".", "0")
    bot_border = tile[-1].replace("#","1").replace(".", "0")
    left_border = reduce(lambda x,y: x+y,[x[0] for x in tile[1:]]).replace("#","1").replace(".", "0")
    right_border = reduce(lambda x,y: x+y,[x[-1] for x in tile[1:]]).replace("#","1").replace(".", "0")
    borders = [top_border, top_border[::-1], bot_border, bot_border[::-1], right_border, right_border[::-1], left_border, left_border[::-1]]
    borders = [int(x,2) for x in borders]
    for bord in borders:
        if bord in seen:
            seen[bord].append(tile_num)
        else:
            seen[bord] = [tile_num]

another_one = {}
ar = []
for key in seen:
    if len(seen[key]) == 1:
        if seen[key][0] in another_one:
            another_one[seen[key][0]] += 1
        else:
            another_one[seen[key][0]] = 1 
for key in another_one:
    if another_one[key] == 4:
        ar.append(int(key))

print(reduce(lambda x,y: x*y, ar))

corners = ar.copy()

ar = []
for key in another_one:
    if another_one[key] == 2:
        ar.append(int(key))

edges = ar.copy()

remaining = [int(x[0].split(" ")[-1][:-1]) for x in tiles]
remaining = set(remaining)
edges_set = set(edges)
corn_set = set(corners)
remaining = remaining - corn_set
remaining = remaining - edges_set
remaining = list(remaining)

print(len(corners))
print(len(edges))

def get_edges(piece_id):
    for tile in tiles:
        if int(tile[0].split(" ")[-1][:-1]) == piece_id:
            break
    top_border = tile[1].replace("#","1").replace(".", "0")
    bot_border = tile[-1].replace("#","1").replace(".", "0")
    left_border = reduce(lambda x,y: x+y,[x[0] for x in tile[1:]]).replace("#","1").replace(".", "0")
    right_border = reduce(lambda x,y: x+y,[x[-1] for x in tile[1:]]).replace("#","1").replace(".", "0")
    borders = [right_border, top_border, left_border, bot_border]
    #borders = [int(x,2) for x in borders]
    return borders

import numpy as np

class Tile:
    def __init__(self, p_id):
        self.edges = get_edges(p_id)
        self.id = p_id
        self.o = 0
    def try_next(self):
        if self.o < 3:
            self.rotate()
            #rotatae
        elif self.o == 3:
            self.rotate()
            self.flip()
        elif self.o <7:
            self.rotate()
        elif self.o == 7:
            self.rotate()
            self.flip()
            #rotate
        self.o += 1
        self.o = self.o%8
    def rotate(self):
        edges = [self.edges[3][::-1], self.edges[0], self.edges[1][::-1], self.edges[2]]
        self.edges = edges.copy()
    def flip(self):
        edges = [self.edges[2] ,self.edges[1][::-1] , self.edges[0], self.edges[3][::-1] ]
        self.edges = edges.copy()
    def __str__(self):
        return str(self.id)
    def get_inner(self):
        for tile in tiles:
            if int(tile[0].split(" ")[-1][:-1]) == self.id:
                break
        inner = np.zeros([8,8], dtype= int)
        for row in range(inner.shape[0]):
            for col in range(inner.shape[1]):
                if tile[row+2][col+1] == "#":
                    inner[row,col] = 1
                else:
                    inner[row,col] = 0
        flips =0
        while flips < self.o:
            if flips < 3:
                inner = np.rot90(inner)
                #rotatae
            elif flips == 3:
                inner = np.rot90(inner)
                inner = np.fliplr(inner)
            elif flips <7:
                inner = np.rot90(inner)
            flips += 1
        return inner

# test = Tile(corners[0])
# test2 = Tile(corners[0])
# for i in range(4):
#     test2.try_next()


##create the puzzle
import math
N = int(math.sqrt(len(tiles)))
puzzle = [[None for x in range(N)] for y in range(N)]

##set first piece
puzzle[0][0] = Tile(corners.pop(0))

##orienteate first piece
while True:
    top = puzzle[0][0].edges[1]
    left = puzzle[0][0].edges[2]
    if len(seen[int(top,2)]) == 1 and len(seen[int(left,2)]) == 1:
        break
    else:
        puzzle[0][0].try_next()

print(edges)

##fill top row minus last corener
for top_row_ind in range(1,N-1):
    print(top_row_ind)
    for try_piece in edges:
        found= False
        puzzle[0][top_row_ind] = Tile(try_piece)
        for oo in range(8):
            #print("hiii")
            if puzzle[0][top_row_ind-1].edges[0] == puzzle[0][top_row_ind].edges[2]:
                print("found match")
                edges.remove(puzzle[0][top_row_ind].id)
                found = True
                break
            else:
                puzzle[0][top_row_ind].try_next()
        if found:
            break

print(corners)
#top right corner
for corner_id in corners:
    puzzle[0][-1] = Tile(corner_id)
    for oo in range(8):
        if puzzle[0][-2].edges[0] == puzzle[0][-1].edges[2]:
            print("found corner")
            corners.remove(puzzle[0][-1].id)
            break
        else:
            puzzle[0][-1].try_next()

##fit the right edge
for right_row_ind in range(1,N-1):
    for try_piece in edges:
        found= False
        puzzle[right_row_ind][-1] = Tile(try_piece)
        for oo in range(8):
            #print("hiii")
            if puzzle[right_row_ind-1][-1].edges[3] == puzzle[right_row_ind][-1].edges[1]:
                print("found match")
                edges.remove(puzzle[right_row_ind][-1].id)
                found = True
                break
            else:
                puzzle[right_row_ind][-1].try_next()
        if found:
            break

#fit bottom right corner
for corner_id in corners:
    puzzle[-1][-1] = Tile(corner_id)
    for oo in range(8):
        if puzzle[-2][-1].edges[3] == puzzle[-1][-1].edges[1]:
            print("found corner")
            corners.remove(puzzle[-1][-1].id)
            break
        else:
            puzzle[-1][-1].try_next()

##fit the right edge
for left_row_ind in range(1,N-1):
    for try_piece in edges:
        found= False
        puzzle[left_row_ind][0] = Tile(try_piece)
        for oo in range(8):
            #print("hiii")
            if puzzle[left_row_ind-1][0].edges[3] == puzzle[left_row_ind][0].edges[1]:
                print("found match")
                edges.remove(puzzle[left_row_ind][0].id)
                found = True
                break
            else:
                puzzle[left_row_ind][0].try_next()
        if found:
            break

#fit bottom left corner
for corner_id in corners:
    puzzle[-1][0] = Tile(corner_id)
    for oo in range(8):
        if puzzle[-2][0].edges[3] == puzzle[-1][0].edges[1]:
            print("found corner")
            corners.remove(puzzle[-1][0].id)
            break
        else:
            puzzle[-1][0].try_next()

##fill bot row minus last corener
for bot_row_ind in range(1,N-1):
    for try_piece in edges:
        found= False
        puzzle[-1][bot_row_ind] = Tile(try_piece)
        for oo in range(8):
            #print("hiii")
            if puzzle[-1][bot_row_ind-1].edges[0] == puzzle[-1][bot_row_ind].edges[2]:
                print("found match")
                edges.remove(puzzle[-1][bot_row_ind].id)
                found = True
                break
            else:
                puzzle[-1][bot_row_ind].try_next()
        if found:
            break

assert(len(corners) == 0)
assert(len(edges) == 0)

##Now for the middle
print(remaining)
for row in range(1,N-1):
    for col in range(1, N-1):
        for piece_id in remaining:
            found = False
            puzzle[row][col] = Tile(piece_id)
            for oo in range(8):
                if puzzle[row-1][col].edges[3] == puzzle[row][col].edges[1] and puzzle[row][col-1].edges[0] == puzzle[row][col].edges[2]:
                    print("found match")
                    remaining.remove(puzzle[row][col].id)
                    found = True
                    break
                else:
                    puzzle[row][col].try_next()
            if found:
                break

##oke we solved puzzle now lets make the picture 

picture = np.zeros((8*N, 8*N), dtype=int)
for row in range(0,picture.shape[0], 8):
    for col in range(0,picture.shape[1], 8):
        picture[row:row+8, col:col+8] = puzzle[row//8][col//8].get_inner()

print(picture)

picture = np.pad(picture, ((picture.shape[0], picture.shape[0]), (picture.shape[1], picture.shape[1])), "constant")

print(picture)
with open("day20monster.txt", "r") as data_file:
    sl= data_file.readlines()

monster = strip_list(sl)
monster_img = np.zeros_like(picture, dtype =int)
for row_n, row in enumerate(monster):
    for col_n, val in enumerate(row):
        if val == "#":
            #print(row_n, col_n)
            monster_img[row_n, col_n] = 1

print(monster_img[:5,:11])

conv = np.array(np.round(np.fft.ifft2(np.fft.fft2(picture) *np.conj(np.fft.fft2(monster_img))))+0.1, dtype= int)
num_monster = np.count_nonzero(conv == np.sum(monster_img))
print(np.max(conv))
print(num_monster)



for j in puzzle:
    stre = ""
    for i in j:
        stre += str(i) + " "    
    print(stre)

print(np.sum(picture) - num_monster *np.sum(monster_img))