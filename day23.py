
# with open("day13.txt", "r") as data_file:
#     sl= data_file.readlines()
from functools import reduce
import string
from collections import Counter
import copy
from itertools import product, permutations, combinations
from collections import deque


class Node:
    def __init__(self, data, parent=None):
        self.data = data
        self.next = None
        self.prev = parent
    def append(self, data):
        self.next = Node(data, parent=self)
        return self.next
    def __repr__(self):
        return self.data

class Llist:
    def __init__(self, llist = None, size = None):
        self.list = llist
        self.size = size   
    def fill(self, plist):
        head = Node(plist[0]) 
        me = head   
        for el in plist[1:]:
            me = me.append(el)
        self.list = head
        head.prev = me
        me.next = head
        self.size = len(plist)
        self.get_pos()
    def __repr__(self):
        node = self.list
        nodes = []
        for _ in range(self.size):
            nodes.append(str(node.data))
            node = node.next
        return "->".join(nodes)
    def __str__(self):
        return repr(self)
    def get_pos(self):
        self.pos = [0 for _ in range(self.size+1)]
        me = self.list
        for i in range(self.size):
            self.pos[me.data] = me
            me = me.next
    def to_list(self):
        node = self.list
        nodes = []
        for _ in range(self.size):
            nodes.append(node.data)
            node = node.next
        return nodes

def do_move_llist(llist):
    removed_objects = [llist.list]
    for _ in range(3):
        removed_objects.append(removed_objects[-1].next)
    removed_objects.pop(0)
    removed_vals = [x.data for x in removed_objects]
    end_point = (llist.list.data - 2)%llist.size +1
    i =2
    while True:
        if end_point in removed_vals:
            end_point = (end_point-i)%llist.size +1
        else:
            break
    to_check = llist.pos[end_point]
    left_connect = to_check
    right_connect = to_check.next
    left_disconect = removed_objects[0].prev
    right_disconect = removed_objects[-1].next
    left_disconect.next = right_disconect
    right_disconect.prev = left_disconect
    left_connect.next = removed_objects[0]
    right_connect.prev = removed_objects[-1]
    removed_objects[0].prev = left_connect
    removed_objects[-1]. next = right_connect

    llist.list = llist.list.next


def do_move(lst, current):
    N= len(lst)
    start_cup_val = lst[current]
    to_pop = [idx%N for idx in range(current+1, current +4)]
    picked_up = [lst[idx] for idx in to_pop]
    for idx in picked_up:
        lst.remove(idx)
    for i in range(2,6):
        dest_cup_val = (start_cup_val-i)%N+1
        if dest_cup_val in lst:
            dest_cup_idx = lst.index(dest_cup_val)
            break
    v = 0
    for idx in range(dest_cup_idx+1, dest_cup_idx+4):
        lst.insert(idx%N, picked_up[v])
        v+= 1
    return lst, (lst.index(start_cup_val)+1)%N

def get_one(pl):
    one_pos = pl.index(1)
    part_one = [pl[(one_pos+i)%len(pl)] for i in range(1,len(pl))]
    part_one = reduce(lambda x,y: x + str(y), part_one, "")  
    return [part_one] 

inp = "362981754"
inp = list(inp)
inp = [int(x) for x in inp]
cur = 0
res = inp.copy()

res2 = Llist()
res2.fill(inp)
#print(res2)
for move in range(100):
    res, cur = do_move(res, cur)
    print(get_one(res))
    do_move_llist(res2)
    print(get_one(res2.to_list()))
    assert(get_one(res) == get_one(res2.to_list()))
    


one_pos = res.index(1)
part_one = [res[(one_pos+i)%len(res)] for i in range(len(res))][1:]
part_one = reduce(lambda x,y: x + str(y), part_one, "")
print(part_one)


big_link_maker = inp + [x for x in range(10,1000000 +1)]
assert(len(big_link_maker) == 1000000)
res2 = Llist()
res2.fill(big_link_maker)

for move in range(10000000):
    do_move_llist(res2)
    if move%100000 ==0:
        print(move/10000000 *100, "%")





me = res2.list
while True:
    if me.data == 1:
        nn = me.next
        the_res = nn.data
        nn = nn.next
        the_res = the_res*nn.data
        break
    else:
        me = me.next


print(the_res)