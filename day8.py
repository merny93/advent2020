with open("day8.txt", "r") as data_file:
    sl= data_file.readlines()
# with open("input_dec_8.txt", "r") as data_file:
#     sl= data_file.readlines()
from functools import reduce
import string
from collections import Counter
import copy

##read in if the seperator is enters
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
#get rid of pesky new lines
def strip_list(data_strings):
    return [line.strip() for line in data_strings if len(line.strip()) != 0]

##write here
code_strip = strip_list(sl)

instruction_set = [x.split(" ")  for x in code_strip]

acc = 0
pos = 0
vist = []
while True:
    vist.append(pos)
    if instruction_set[pos][0] == "acc":
        acc += int(instruction_set[pos][1])
        pos += 1
    elif instruction_set[pos][0] == "jmp":
        pos += int(instruction_set[pos][1])
    else:
        pos += 1
    if pos in vist:
        break

print(acc)
from ass_tools import Program
test = Program(instruction_set)
print("test", test.run_program())
N = len(instruction_set)

for i in range(N):
    swap_try = copy.deepcopy(instruction_set)
    if swap_try[i][0] =="jmp":
        swap_try[i][0] = "nop"
    elif swap_try[i][0] =="nop":
        swap_try[i][0] = "jmp"
    #print(swap_try[i][0])
    acc = 0
    pos = 0
    vist = []
    while True:
        vist.append(pos)
        if swap_try[pos][0] == "acc":
            acc += int(swap_try[pos][1])
            pos += 1
        elif swap_try[pos][0] == "jmp":
            pos += int(swap_try[pos][1])
        else:
            pos += 1

        if pos in vist:
            break
        if pos == N:
            print(acc)
            print(i)
            exit()