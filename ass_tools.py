class Program:
    def __init__(self, instruction):
        from copy import deepcopy
        self.inst = deepcopy(instruction)
        
    
    def step(self, start_pos, break_func):
        if break_func(start_pos):
            print(start_pos)
            return False
        pos = start_pos
        acc = 0
        if self.inst[pos][0] == "jmp":
            pos += int(self.inst[pos][1])
        elif self.inst[pos][0] == "acc":
            acc = int(self.inst[pos][1])
            pos += 1
        else:
            pos += 1
        return {"pos": pos, "acc": acc}
    
    def run_program(self):
        visited = list()
        pos = 0
        acc = 0
        loop_check = lambda x: True if x in visited else False
        end_check = lambda x: True if x >= len(self.inst) else False
        total_check = lambda x: True if loop_check(x) or end_check(x) else False
        while True:
            res = self.step(pos, total_check)
            if res is False:
                break
            visited.append(pos)
            pos = res["pos"]
            acc += res["acc"]
        return acc            

