with open("day14.txt", "r") as data_file:
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

striped = strip_list(sl)
address = {}
for line in striped:
    if line[:4] == "mask":
        mask = line.split(" ")[-1]
    else:
        ad = line.split("[")[-1].split("]")[0]
        if ad in address:
            cur = address[ad]
            #print(cur)
            for i in range(len(mask)):
                if mask[i] != "X":
                    cur[i] = mask[i]
                else:
                    temp = list(bin(int(line.split(" ")[-1]))[2:])
                    temp = ["0" for x in range(36- len(temp))] + temp
                    cur[i] = temp[i]
            address[ad] = cur
                    
        else:
            cur = list(bin(int(line.split(" ")[-1]))[2:])
            cur = ["0" for x in range(36- len(cur))] + cur
            for i in range(len(mask)):
                if mask[i] != "X":
                    cur[i] = mask[i]
            address[ad] = cur
                
total = 0
for key in address:
    bins = reduce(lambda x,y: x+y, address[key])
    #print(bins)
    total += int(bins,2)

print(total)

address = {}
for line in striped:
    if line[:4] == "mask":
        mask = line.split(" ")[-1]
    else:
        ad = line.split("[")[-1].split("]")[0]
        ad_bin = list(bin(int(ad))[2:])
        ad_bin = [["0" for x in range(36- len(ad_bin))] + ad_bin]
        for i in range(len(mask)):
            if mask[i] == "X":
                ad_bin = copy.deepcopy(ad_bin) + copy.deepcopy(ad_bin)
                for j in range(len(ad_bin)//2):
                    #print(j,i)
                    ad_bin[j][i] = "1"
                for j in range(len(ad_bin)//2, len(ad_bin)):
                    ad_bin[j][i] = "0"
            elif mask[i] == "1":
                for j in range(len(ad_bin)):
                    ad_bin[j][i] = "1"
            else:
                pass
        
        for adr in ad_bin:
            #print(adr)
            adr = int(reduce(lambda x,y: x+ y,adr), 2)
            address[str(adr)] = int(line.split(" ")[-1])
        print("skip")

        


#print(address)
total = 0
for key in address:
    total += address[key]
print(total)