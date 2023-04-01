# PASM

### It's a asm in python named pasm
----------------------------------------
### FUCTIONS
```
    ldi <addr> <data> = load the register at the addres with the data
    mov <addr1> <addr2> = moves addr2 into addr1
    read <addr> = prints the data at the register of addres
    print <str> = prints the str
    add <dst> <addr1> <addr2> = sets the register at dst to addres1 plus addres2
    sub <dst> <addr1> <addr2> = sets the register at dst to addres1 minus addres2
    dec <addr> = decrements the addreses
    inc <addr> = increments the addreses
    jmp <line> = sets the line to the line
    jz <addr> <line> = checks if the register at addres is 0 then it will jump to the line if it is anything else it will jump to the next line
    hlt = stops the program (duh)
```
##### in the examples folder there are examples that you can check out

---------------------------------------
### NOTES
##### The line at jmp and jz are 0 based indexes same for the register it is 8 bit with the first one being register zero and the last being 7