with open("day5.txt", "r") as data_file:
    string_list= data_file.readlines()


score = 0
Ids = []
for seat in string_list:
    bit_str = seat[:7]
    assert(len(bit_str) == 7)
    bit_str = bit_str.replace("F", "0")
    bit_str = bit_str.replace("B", "1")
    print(bit_str)
    row_n = int(bit_str,2)
    print(row_n)
    bit_str = (seat[7:]).strip()
    assert(len(bit_str) == 3)
    print(bit_str)
    bit_str =bit_str.replace("R", "1")
    bit_str =bit_str.replace("L", "0") 
    seat_n = int(bit_str,2)
    print(seat_n)
    Ids.append(row_n*8 +seat_n)
    score = max(score, row_n*8 +seat_n)
    print(score)


print(score)

from itertools import product

all_seats = list(product(["F","B"],["F","B"],["F","B"],["F","B"],["F","B"],["F","B"],["F","B"],["L","R"],["L","R"],["L","R"]))

seat_list = [list(seat.strip()) for seat in string_list]
count = 0 
for seat in all_seats:
    if list(seat) in seat_list:
        pass
    else:
        #check if neigbors are there:
        seat = ' '.join([str(elem) for elem in list(seat)])
        seat = seat.replace(" ", "")
        bit_str = seat[:7]
        assert(len(bit_str) == 7)
        bit_str = bit_str.replace("F", "0")
        bit_str = bit_str.replace("B", "1")
        row_n = int(bit_str,2)
        bit_str = (seat[7:]).strip()
        assert(len(bit_str) == 3)
        bit_str =bit_str.replace("R", "1")
        bit_str =bit_str.replace("L", "0") 
        seat_n = int(bit_str,2)
        scr = (row_n*8 +seat_n)
        if scr+1 in Ids and scr-1 in Ids:
            print(seat)
            print("win")
            print(scr)

