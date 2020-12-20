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

tickets = strip_list(sl)
invalid  = []
with open("rules.txt", "r") as data_file:
    sl= data_file.readlines()
rules = strip_list(sl)
rule_list = []
for rule in rules:
    rule = rule.split(":")[-1][1:]
    rule = rule.split(" or ")
    vals = list(range(int(rule[0].split("-")[0]), int(rule[0].split("-")[1])+1)) + list(range(int(rule[1].split("-")[0]), int(rule[1].split("-")[1])+1))
    rule_list += vals



for ticket in tickets:
    ticket_clone = str(ticket)
    remove = False
    ticket = ticket.split(",")
    ticket = [int(field) for field in ticket]
    for field in ticket:
        if int(field) in rule_list:
            pass
        else:
            invalid.append(int(field))
            remove = True
    if remove:
        tickets.remove(ticket_clone)

print(len(tickets))
print(sum(invalid))

with open("rules.txt", "r") as data_file:
    sl= data_file.readlines()
rules = strip_list(sl)
rule_list = []
for rule in rules:
    rule = rule.split(":")[-1][1:]
    rule = rule.split(" or ")
    vals = list(range(int(rule[0].split("-")[0]), int(rule[0].split("-")[1])+1)) + list(range(int(rule[1].split("-")[0]), int(rule[1].split("-")[1])+1))
    rule_list.append(vals)

field_work = [[0 for rule in rule_list] for i in range(20)]
for ticket in tickets:
    ticket_clone = str(ticket)
    remove = False
    ticket = ticket.split(",")
    ticket = [int(field) for field in ticket]
    for f_num,field in enumerate(ticket):
        for r_num, rule in enumerate(rule_list):
            if int(field) in rule:
                field_work[f_num][r_num] += 1
                #this field works for this rule
            else:
                pass
good = []
print("hello")
tries = {}
for f,row in enumerate(field_work):
    #print(max(field))
    for r in range(len(row)):
        if row[r] == len(tickets):
            if f in tries:
                tries[f] += 1
            else
                tries[f] = 1
            print("field",f)
            print("rule", r)
            good.append(f)

for key in tries:
    

good = list(set(good))
mine = [157,73,79,191,113,59,109,61,103,101,67,193,97,179,107,89,53,71,181,83]
the_ones = [mine[x] for x in good]
print(reduce(lambda x,y:x*y, the_ones))