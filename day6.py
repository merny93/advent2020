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


#
print("part 1:", sum([ len([1 for letter in alpha if letter in reduce(lambda x,y: x.strip() + y.strip(), sl[x[0] :  x[1]])]) for x in zip([0] + [ind for ind in range(len(sl)) if len(sl[ind].strip()) == 0],[ind for ind in range(len(sl)) if len(sl[ind].strip()) == 0] + [len(sl)])]))

print("part 2:", sum([ len([1 for letter in alpha if reduce(lambda x,y: x.strip() + y.strip(), sl[x[0] :  x[1]]).count(letter) == len([sl[x[0] :  x[1]] for x in zip([0] + [ind for ind in range(len(sl)) if len(sl[ind].strip()) == 0],[ind for ind in range(len(sl)) if len(sl[ind].strip()) == 0] + [len(sl)])])]) for x in zip([0] + [ind for ind in range(len(sl)) if len(sl[ind].strip()) == 0],[ind for ind in range(len(sl)) if len(sl[ind].strip()) == 0] + [len(sl)])]))