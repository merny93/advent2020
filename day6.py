with open("day6.txt", "r") as data_file:
    sl= data_file.readlines()

from functools import reduce
import string
alpha = string.ascii_lowercase
print(alpha)
num_good = []

vals = []
for line in sl:
    if len(line.strip()) == 0:
        #we have a group
        long_string = reduce(lambda x,y: x+y, vals)
        long_string = reduce(lambda x,y: x+y, long_string)
        present = [1 for letter in alpha if letter in long_string]
        num_good.append(len(present))
        vals = []
    vals.append(line.strip().split())

print(sum(num_good))
print(len(num_good))
num_good = []

vals = []
for line in sl:
    if len(line.strip()) == 0:
        #we have a group
        long_string = reduce(lambda x,y: x+y, vals)
        total = len(long_string)
        long_string = reduce(lambda x,y: x+y, long_string)
        present = [1 for letter in alpha if long_string.count(letter) == total]
        num_good.append(len(present))
        vals = []
    vals.append(line.strip().split())

print(sum(num_good))

from collections import Counter

#
print("part 1:", sum([ len([1 for letter in alpha if letter in reduce(lambda x,y: x.strip() + y.strip(), sl[x[0] :  x[1]])]) for x in zip([0] + [ind for ind in range(len(sl)) if len(sl[ind].strip()) == 0],[ind for ind in range(len(sl)) if len(sl[ind].strip()) == 0] + [len(sl)])]))


count_list =list((list(filter(lambda z: False if not z else True, list(map(lambda x: dict(Counter(x.strip())), x)))) for x in [sl[x[0] :  x[1]] for x in zip([0] + [ind for ind in range(len(sl)) if len(sl[ind].strip()) == 0],[ind for ind in range(len(sl)) if len(sl[ind].strip()) == 0] + [len(sl)])]))[:-1]
#print(reduce(lambda a,b:[lette for lette in a if lette in b.keys() and lette in a], count_list[1], list(alpha)))
good = sum([len(reduce(lambda a,b:[lette for lette in a if lette in b.keys() and lette in a], group_ans, list(alpha))) for group_ans in count_list])
print("part2:", sum([len(reduce(lambda a,b:[lette for lette in a if lette in b.keys() and lette in a], group_ans, list(alpha))) for group_ans in list((list(filter(lambda z: False if not z else True, list(map(lambda x: dict(Counter(x.strip())), x)))) for x in [sl[x[0] :  x[1]] for x in zip([0] + [ind for ind in range(len(sl)) if len(sl[ind].strip()) == 0],[ind for ind in range(len(sl)) if len(sl[ind].strip()) == 0] + [len(sl)])]))[:-1]]))
#print("part 2:", list(filter(lambda z: True if not z[0] else False, (list(map(lambda x: dict(Counter(x.strip())), x)) for x in [sl[x[0] :  x[1]] for x in zip([0] + [ind for ind in range(len(sl)) if len(sl[ind].strip()) == 0],[ind for ind in range(len(sl)) if len(sl[ind].strip()) == 0] + [len(sl)])]))))
#print("part 2:", sum([ len([1 for letter in alpha if reduce(lambda x,y: x.strip() + y.strip(), sl[x[0] :  x[1]]).count(letter) == len([sl[x[0] :  x[1]] for x in zip([0] + [ind for ind in range(len(sl)) if len(sl[ind].strip()) == 0],[ind for ind in range(len(sl)) if len(sl[ind].strip()) == 0] + [len(sl)])])]) for x in zip([0] + [ind for ind in range(len(sl)) if len(sl[ind].strip()) == 0],[ind for ind in range(len(sl)) if len(sl[ind].strip()) == 0] + [len(sl)])]))