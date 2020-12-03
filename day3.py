with open("day3.txt", "r") as data_file:
    string_list= data_file.readlines()


count = 0 
pos = 0
for line in string_list:
    map_line = line.strip()
    N = len(map_line)
    if map_line[pos%N] == "#":
        count += 1
    pos += 3

print(count)

def count_slope(slope, data):
    count = 0 
    pos = 0
    for ind, line in enumerate(data):
        if ind%slope[1]:
            continue
        map_line = line.strip()
        N = len(map_line)
        if map_line[pos%N] == "#":
            count += 1
        pos += slope[0]
    return count

print(count_slope([3,1], string_list))

from functools import reduce

print("second part", reduce(lambda x,y: x*y, [count_slope(slope, string_list) for slope in [[1,1], [3,1],[5,1],[7,1],[1,2]]]))