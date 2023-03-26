import sys

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
            
def logic(f_data):
    stack = []
    pc = 0
    for m in MUST:
        if m not in f_data:
            print("%s, is not found in file" %m)
            exit(1)
    while pc < len(f_data):
        ip = pc
        op = f_data[pc]
        if op == 'ldi':
            addr = f_data[ip+1]
            data = f_data[ip+2]
            register[int(addr)] = data
            pc += 1
        elif op == 'read':
            addr = f_data[ip+1]
            print(register[int(addr)])
            pc += 1
        elif op == 'add':
            dst = f_data[ip+1]
            addr1, addr2 = f_data[ip+2], f_data[ip+3]
            register[int(dst)] = int(register[int(addr1)]) + int(register[int(addr2)])
            pc += 1
        elif op == 'sub':
            dst = f_data[ip+1]
            addr1, addr2 = f_data[ip+2], f_data[ip+3]
            register[int(dst)] = int(register[int(addr1)]) - int(register[int(addr2)])
            pc += 1
        elif op == 'hlt':
            pc = len(f_data)
        else:
            try:
                stack.append(int(op))
                pc += 1
            except ValueError:
                if op in MUST:
                    pc += 1
                    continue
                print("Invalid word: %s" %op)
                break
            
with open("main.pasm", "r") as f:
    f_data = f.read().split()
    logic(f_data)