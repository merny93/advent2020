import copy
with open("day4.txt", "r") as data_file:
    string_list= data_file.readlines()

needed = ["byr", "iyr","eyr", "hgt", "hcl", "ecl", "pid"]
count = 0 
vals = []
for line in string_list:
    if len(line.strip()) == 0:
        fields = [x for sub in vals for x in sub]
        tryy = needed.copy()
        for v in fields:
            if v.split(":")[0] in tryy:
                tryy.remove(v.split(":")[0])
        if tryy == []:
            count += 1
        vals = []
    vals.append(line.strip().split())

print(count)

def do_byr(num):
    num = int(num)
    rang = [1920,2002]
    if num >= rang[0] and num <= rang[1]:
        return True
    return False

def do_iyr(num):
    num = int(num)
    rang = [2010,2020]
    if num >= rang[0] and num <= rang[1]:
        return True
    return False

def do_eyr(num):
    rang = [2020,2030]
    num = int(num)
    if num >= rang[0] and num <= rang[1]:
        return True
    return False

def do_hgt(strin):
    if strin[-2:] == "cm" and int(strin[:-2]) >= 150 and int(strin[:-2]) <= 193:
        return True
    if strin[-2:] == "in" and int(strin[:-2]) >= 59 and int(strin[:-2]) <= 76:
        return True
    else:
        return False

def do_hcl(strin):
    if strin[0] != "#":
        return False
    if len(strin) != 7:
        return False
    char_list = list(strin[1:])
    for char in char_list:
        if char >= "0" and char <= "9" or char >= "a" and char <= "f":
            pass
        else:
            return False
    return True

def do_ecl(strin):
    if strin in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
        return True
    return False

def do_pid(strin):
    try:
        int(strin)
    except:
        return False
    if len(strin) == 9:
        return True 
    return False

needed = {"byr":do_byr, "iyr": do_iyr,"eyr": do_eyr, "hgt":do_hgt, "hcl": do_hcl, "ecl":do_ecl, "pid":do_pid}
count = 0 
vals = []
for line in string_list:
    if len(line.strip()) == 0:
        fields = [x for sub in vals for x in sub]
        trials = {"byr":False, "iyr": False,"eyr": False, "hgt":False, "hcl": False, "ecl":False, "pid":False}
        for v in fields:
            try:
                if needed[v.split(":")[0]](v.split(":")[-1]):
                    trials[v.split(":")[0]] = True
            except:
                pass
        check = [1 for x in trials if trials[x]]
        if len(check) == 7:
            count += 1
        vals = [] #the line that i forgot to copy
    vals.append(line.strip().split())

print(count)