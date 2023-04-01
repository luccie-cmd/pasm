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

class Error:
    def __code1__(self, addr):
        print("%s can not pe parsed at a integer for the addres" %addr)
        quit(1)
    def __code2__(self, m):
        print("%s Not all specifiers met for a good program\nexit code 2" %m)
        quit(2)

class Operations:
    def ldi(self, addr, data):
        try:
            register[int(addr)] = data
        except ValueError:
            Error().__code1__(addr)
    def read(self, addr):
        try:
            print(register[int(addr)])
        except ValueError:
            Error().__code1__(addr)
    def add(self, data):
        try:
            dst = data[1]
            addr1, addr2 = data[2], data[3]
            register[int(dst)] = int(register[int(addr1)]) + int(register[int(addr2)])
        except ValueError:
            Error().__code1__(data[1])
    def sub(self, data):
        try:
            dst = data[1]
            addr1, addr2 = data[2], data[3]
            register[int(dst)] = int(register[int(addr1)]) - int(register[int(addr2)])
        except ValueError:
            Error().__code1__(data[1])
    def jmp(self, data):
        try:
            return int(data[1])
        except ValueError:
            Error().__code1__(data[1])
    def jz(self, data, line):
        try:
            addr = data[1]
            if register[int(data[1])] == "0" or register[int(addr)] == 0:
                return int(data[2])
        except ValueError:
            Error().__code1__(data[1])
        return line+1
            
def logic(f_data, ops):
    line = 0
    stack = []
    for m in MUST:
        if m not in f_data:
            Error().__code2__(m)
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
        else:
            print("%s:%s: %s is not a valid instruction" %(sys.argv[1], line, op))
        line+=1
            

if __name__ == '__main__':
    ops = Operations()
    logic(read_file(sys.argv[1]), ops)