from functools import reduce
from numba import njit
import time

#report = [1721, 979, 366, 299, 675 ,1456] #for testion 
with open("day1.txt", "r") as data_file:
    report = data_file.readlines()
report = [int(line.strip()) for line in report]


#report = [1721, 979, 366, 299, 675 ,1456] #for testion 


def bs_worker(try_list, target_rel):
    N = len(try_list)
    if N == 1 and try_list[0] != target_rel:
        return False 
    center_val = try_list[N//2]
    if center_val == target_rel:
        return center_val
    elif center_val < target_rel:
        return bs_worker(try_list[N//2:], target_rel)
    elif center_val > target_rel:
        return bs_worker(try_list[:N//2], target_rel)

def bs_master(trial_vals_sorted, prev_vals, target):
    part_sum = reduce(lambda x,y: x+y, prev_vals)
    return bs_worker(trial_vals_sorted, target-part_sum)


#function returns the two values which add up to target
def get_sum(vals, target, do_bs = True):
    vals.sort()
    my_sum = 0
    for a in range(len(vals)):
        if vals[a] >= target//2:
            return "no value found"
        
        if do_bs:
            val = bs_master(vals[a+1:],[vals[a]], target)
            if val:
                return [vals[a]] + [val]
            else:
                continue
        else:
            for b in range(a+1, len(vals)):
                my_sum = vals[a] + vals[b]
                if my_sum == target:
                    return vals[a], vals[b]
                elif my_sum > target:
                    break


#function returns the product of the two values which sum up to 2020

solve_puzzle = lambda vals: reduce(lambda x,y: x*y, get_sum(vals,2020))
print(get_sum(report,2020))
print(solve_puzzle(report))


def get_triple_sum(vals, target, do_bs=True):
    vals.sort()
    for a in range(len(vals)):
        if vals[a] >= target//3:
            return "no value found"
        for b in range(a+1, len(vals)):
            if vals[a] + vals[b] >= target:
                break
            if do_bs:
                val = bs_master(vals[a+1:],[vals[a], vals[b]], target)
                if val:
                    return [vals[a], vals[b]] + [val]
                else:
                    continue
            else:
                for c in range(b+1, len(vals)):
                    my_sum = vals[a] + vals[b] + vals[c]
                    if my_sum == target:
                        return vals[a], vals[b], vals[c]
                    elif my_sum > target:
                        break

solve_puzzle_3 = lambda vals: reduce(lambda x,y: x*y, get_triple_sum(vals,2020))

print(get_triple_sum(report,2020))
print(solve_puzzle_3(report))

t1 = time.time()
solve_puzzle(report)
t2 = time.time()
print("time", t2-t1)

t1 = time.time()
solve_puzzle_3(report)
t2 = time.time()
print("time", t2-t1)