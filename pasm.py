import sys, time

register = [
    "0",
    "0",
    "0",
    "0",
    "0",
    "0",
    "0", 
    "0",
]
MUST = [
    'hlt',
]

def read_file(file: str):
    with open(file, "r") as f:
        return f.readlines()

class Operations:
    def ldi(self, addr, data):
        register[int(addr)] = data
    def read(self, addr):
        print(register[int(addr)])
    def add(self, data):
        dst = data[1]
        addr1, addr2 = data[2], data[3]
        register[int(dst)] = int(register[int(addr1)]) + int(register[int(addr2)])
    def sub(self, data):
        dst = data[1]
        addr1, addr2 = data[2], data[3]
        register[int(dst)] = int(register[int(addr1)]) - int(register[int(addr2)])
    def jmp(self, data):
        return int(data[1])
    def jz(self, data, line):
        addr = data[1]
        if register[int(data[1])] == "0" or register[int(addr)] == 0:
            return int(data[2])
        return line+1
            
def logic(f_data, ops):
    line = 0
    stack = []
    while line < len(f_data):
        data = f_data[line].strip().split()
        op = data[0]
        if op == '//':
            line+=1
            continue
        elif op == 'ldi':
            ops.ldi(data[1], data[2])
        elif op == 'read':
            ops.read(data[1])
        elif op == 'add':
            ops.add(data)
        elif op == 'sub':
            ops.sub(data)
        elif op == 'jmp':
            line = ops.jmp(data)
            continue
        elif op == 'jz':
            line = ops.jz(data, line)
            continue
        elif op == 'hlt':
            break
        line+=1
            

if __name__ == '__main__':
    ops = Operations()
    logic(read_file(sys.argv[1]), ops)