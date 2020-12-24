
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


with open("day22p1.txt", "r") as data_file:
    sl= data_file.readlines()

player1 = strip_list(sl)
player1 = [int(x) for x in player1]
player1_copy = player1.copy()
with open("day22p2.txt", "r") as data_file:
    sl= data_file.readlines()

player2 = strip_list(sl)
player2 = [int(x) for x in player2]
player2_copy = player2.copy()
# while True:
#     p1 = player1.pop(0)
#     p2 = player2.pop(0)
#     if p1 > p2:
#         player1.append(p1)
#         player1.append(p2)
#     elif p2>p1:
#         player2.append(p2)
#         player2.append(p1)
#     else:
#         print("equal")
#         exit()
#     if len(player1)==0 or len(player2)==0:
#         break

# print("we have winner") 
# if len(player1)==0:
#     score = sum([(i+1)*player2[::-1][i] for i in range(len(player2))])
# else:
#     score = sum([(i+1)*player1[::-1][i] for i in range(len(player1))])

# print(score)

player1 = player1_copy
player2 = player2_copy



def play_game(player1, player2):
    games = {}
    while True:    
        if hash(tuple(player1)) + 1j * hash(tuple(player2)) in games:
            p1 = player1.pop(0)
            p2 = player2.pop(0)
            player1.append(p1)
            player1.append(p2)
            return True, player1

        else:
            games[hash(tuple(player1)) + 1j * hash(tuple(player2))] = 1

        p1 = player1.pop(0)
        p2 = player2.pop(0)
        if p1 <= len(player1) and p2 <= len(player2):
            res, _ = play_game(player1[:p1], player2[:p2])
            if res:
                player1.append(p1)
                player1.append(p2)
            else:
                player2.append(p2)
                player2.append(p1)
        elif p1 > p2:
            player1.append(p1)
            player1.append(p2)
        elif p2>p1:
            player2.append(p2)
            player2.append(p1)
        else:
            print("equal")
            exit()

        if len(player1)==0:
            return False, player2
        elif len(player2)==0:
            return True, player1

_, win_deck = play_game(player1, player2)

score = sum([(i+1)*win_deck[::-1][i] for i in range(len(win_deck))])
print(score)