# with open("day12t.txt", "r") as data_file:
#     sl= data_file.readlines()
from functools import reduce
import string
from collections import Counter
import copy
from itertools import product, permutations, combinations

def strip_list(data_strings):
    return [line.strip() for line in data_strings if len(line.strip()) != 0]

with open("19in.txt", "r") as data_file:
    sl= data_file.readlines()

messages = strip_list(sl)

with open("19rules.txt", "r") as data_file:
    sl= data_file.readlines()

rules = strip_list(sl)

rules.sort(key = lambda x: int(x.split(":")[0]))
print(rules)
missing  = list(range(int(rules[-1].split(":")[0])+1))
for rule in rules:
    if int(rule.split(":")[0]) in missing:
        missing.remove(int(rule.split(":")[0]))

missing = [str(x) + ": 1" for x in missing]
rules = rules + missing
rules.sort(key = lambda x: int(x.split(":")[0]))
#print(rules)
rules = [x.split(": ")[-1] for x in rules]


def check_legal(rule_try, rule_book, string, place):
    #print(place)
    if '"' in rule_try:
        if place == len(string):
            #print("overload")
            return False, place
        elif rule_try[1] ==string[place]:
            return True, place+1
        else:
            return False, place
    elif "|" in rule_try:
        t1, place =check_legal(rule_try.split(" | ")[0], rule_book, string, place)
        if t1:
            return True, place
        t2, place = check_legal(rule_try.split(" | ")[1], rule_book, string, place)
        if t2:
            return True, place
        return False, place
    else:
        to_call = rule_try.split(" ")
        starting_place = place
        for call in to_call:
            res, place = check_legal(rule_book[int(call)], rule_book, string, place)
            if not res:
                if place == len(string):
                    pass
                    #detected overload 
                return False, starting_place
        return True, place

the_good_good = []
for message in messages:
    good, ze_len = check_legal(rules[0], rules, message, 0)
    if good:
        print("hello")
    if good and ze_len==len(message):
        the_good_good.append(message)
        print(message)
print(len(the_good_good))