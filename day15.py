starting_nums =[2,20,0,4,1,17]

spoken = []
import time
t1 = time.time()
for turn in range(2020):
    try:
        spoken.append(starting_nums[turn])
    except:
        if spoken[-1] in spoken[:-1]:
            #we have seen it before
            temp = spoken[:-1]
            pos = temp[::-1].index(spoken[-1]) + 1
            spoken.append(pos)
        else:
            spoken.append(0)
t2  = time.time()
print((t2-t1)/100000 * 30000000)
print(spoken[-1])

spoken = {}
starting_nums =[2,20,0,4,1,17]
last = starting_nums[0]
starting_nums = starting_nums[1:]
for turn in range(30000000-1):
    if turn < len(starting_nums):
        spoken[last] = turn -1
        last = starting_nums[turn]
    else:
        if last in spoken:
            #we have seen it before
            pos = spoken[last]
            spoken[last] = turn -1
            last = turn - pos -1
        else:
            spoken[last] = turn -1
            last = 0

print(last)