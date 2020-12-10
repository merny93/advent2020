with open("day9.txt", "r") as data_file:
    sl= data_file.readlines()
from functools import reduce
import string
from collections import Counter
import copy
from itertools import product

def strip_list(data_strings):
    return [line.strip() for line in data_strings if len(line.strip()) != 0]


num_list = strip_list(sl)

def gen_legal(arr):
    per = list(product(arr, repeat=2))
    for el in arr:
        per.remove((el,el))
    legal = [reduce(lambda x,y: int(x) + int(y), ar) for ar in per]
    return list(set(legal))

legal = gen_legal(num_list[:25])
for i in range(25, len(num_list)):
    N = int(num_list[i])
    legal = gen_legal(num_list[i-25:i])
    if N in legal:
        pass
    else:
        # print(i)
        
        # print(legal)
        # print(num_list[i-25:i])
        print(N)
        break

# nums = [int(x) for x in num_list[i-25:i]]
# nums.sort()
# nums = list(filter(lambda x: True if x < N else False, nums))
# print(nums)
# print(nums[0] + nums[0])

contig_list = [reduce(lambda x,y: x + [int(y)] if sum(x)<N else x , num_list[i:], []) for i in range(len(num_list))]
list_o_sums = [sum(seg) for seg in contig_list]
the_one = list_o_sums.index(N)
print(min(contig_list[the_one]) + max(contig_list[the_one]))
