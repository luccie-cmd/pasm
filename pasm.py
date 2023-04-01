import sys, time

register = [
    0,
    0,
    0,
    0,
    0,
    0,
    0, 
    0,
]
MUST = [
    'hlt',
]

def read_file(file: str):
    try:
        with open(file, "r") as f:
            return f.readlines()
    except FileNotFoundError:
        Error().__code3__(file)

class Error:
    def __code1__(self, addr):
        print("%s can not pe parsed at a integer for the addres" %addr)
        quit(1)
    def __code2__(self, m):
        print("Not all specifiers met for a good program\nexit code 2")
        quit(2)
    def __code3__(self, file):
        print("pasm: fatal: unable to open input file `%s` No such file or directory" %file)
        quit(3)

class Operations:
    def ldi(self, addr, data):
        try:
            register[int(addr)] = int(data)
        except ValueError:
            register[int(addr)] = hex(data)
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
    def inc(self, addr):
        try:
            register[int(addr)] += 1
        except ValueError:
            Error().__code1__(addr)
    def dec(self, addr):
        try:
            register[int(addr)] -= 1
        except ValueError:
            Error().__code1__(addr)
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
            Error().__code2__()
    while line < len(f_data):
        data = f_data[line].strip().split()
        op = data[0]
        if op == '//':
            line+=1
            continue
        elif op == 'ldi':
            ops.ldi(data[1], int(data[2], base=0))
        elif op == 'read':
            ops.read(data[1])
        elif op == 'add':
            ops.add(data)
        elif op == 'sub':
            ops.sub(data)
        elif op == 'inc':
            ops.inc(data[1])
        elif op == 'dec':
            ops.dec(data[1])
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