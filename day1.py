#report = [1721, 979, 366, 299, 675 ,1456] #for testion 
with open("day1.txt", "r") as data_file:
    report = data_file.readlines()
report = [int(line.strip()) for line in report]


#report = [1721, 979, 366, 299, 675 ,1456] #for testion 

#function returns the two values which add up to target
def get_sum(vals, target):
    vals.sort()
    my_sum = 0
    for a in range(len(vals)):
        if vals[a] >= target//2:
            return "no value found"
        for b in range(a+1, len(vals)):
            my_sum = vals[a] + vals[b]
            if my_sum == target:
                return vals[a], vals[b]
            elif my_sum > target:
                break

#function returns the product of the two values which sum up to 2020
from functools import reduce
solve_puzzle = lambda vals: reduce(lambda x,y: x*y, get_sum(vals,2020))
print(get_sum(report,2020))
print(solve_puzzle(report))


def get_triple_sum(vals, target):
    vals.sort()
    for a in range(len(vals)):
        if vals[a] >= target//3:
            return "no value found"
        for b in range(a+1, len(vals)):
            if vals[a] + vals[b] >= target:
                break
            for c in range(b+1, len(vals)):
                my_sum = vals[a] + vals[b] + vals[c]
                if my_sum == target:
                    return vals[a], vals[b], vals[c]
                elif my_sum > target:
                    break

solve_puzzle_3 = lambda vals: reduce(lambda x,y: x*y, get_triple_sum(vals,2020))

print(get_triple_sum(report,2020))
print(solve_puzzle_3(report))