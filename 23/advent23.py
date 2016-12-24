#!/usr/bin/env python3.6

from sys import argv,exit

input_filename = "input"
if len(argv) > 1:
    input_filename = argv[1]


def execute(initA=0, initB=0, initC=0, initD=0):
    try:
        input = open(input_filename)
    except OSError:
        exit("Cannot open file \"{}\"".format(input_filename))

    program = []

    for line in input:
        program.append(line.split())

    registers = {'a':initA, 'b':initB, 'c':initC, 'd':initD}
    pc = 0

    def findMul(pc):
        if  pc + 5 < len(program)    \
        and program[pc][0] == 'cpy'  \
        and program[pc+1][0] == 'inc'\
        and program[pc+2][0] == 'dec'\
        and program[pc+3][0] == 'jnz'\
        and program[pc+4][0] == 'dec'\
        and program[pc+5][0] == 'jnz':
            m = program[pc][1]
            c = program[pc][2]
            a = program[pc+1][1]
            n = program[pc+4][1]
            # only going to optimize if they're all unique and don't overlap
            if (not c in registers)         \
            or (not a in registers)         \
            or (not n in registers)         \
            or (c == m or c == n or c == a) \
            or (a == m or a == n)           \
            or (m == n):
                return False
            #check that args are in the right place to match a mul
            return m == program[pc][1]      \
               and c == program[pc][2]      \
               and a == program[pc+1][1]    \
               and c == program[pc+2][1]    \
               and c == program[pc+3][1]    \
               and "-2" == program[pc+3][2] \
               and n == program[pc+4][1]    \
               and n == program[pc+5][1]    \
               and "-5" == program[pc+5][2]
        else:
            return False
    def doMul(pc):
        b = program[pc][1]
        c = program[pc][2]
        a = program[pc+1][1]
        d = program[pc+4][1]
        # m can be a bare value, n can't
        if b in registers:
            m = registers[b]
        else:
            m = int(b)
        n = registers[d]
        registers[a] += m * n
        registers[c] = 0
        registers[d] = 0

            
    while pc < len(program):
        if pc < 0:
            print("below 0")
            pc = 0
            # this may be wrong. it's not in the spec so this is my interpretation.
            # the given input probably doesn't even jump to a negetive position. 
        fetch = program[pc]

        if fetch[0] == 'cpy':
            if findMul(pc):
                doMul(pc)
                pc += 6
            else:
                src = fetch[1]
                if src in registers:
                    src = registers[src]
                else:
                    src = int(src)
                dst = fetch[2]
                if dst in registers:
                    registers[dst] = src
                else:
                    print("invalid cpy")
                pc += 1

        elif fetch[0] == 'inc':
            reg = fetch[1]
            if reg in registers:
                registers[reg] += 1
            pc += 1
        elif fetch[0] == 'dec':
            reg = fetch[1]
            if reg in registers:
                registers[reg] -= 1
            pc += 1
        elif fetch[0] == 'jnz':
            src = fetch[1]
            if src in registers:
                src = registers[src]
            else:
                src = int(src)
            tgt = fetch[2]
            if tgt in registers:
                tgt = registers[tgt]
            else:
                tgt = int(tgt)

            if src != 0:
                pc += tgt
            else:
                pc += 1
        elif fetch[0] == 'tgl':
            # print("toggling " + str(fetch) + ", c = " + str(registers['c']))
            x = fetch[1]
            if x in registers:
                x = registers[x]
            else:
                x = int(x)
            if 0 <= pc + x < len(program):
                tgt = program[pc + x]
                if len(tgt) == 2:
                    if tgt[0] == 'inc':
                        tgt[0] = 'dec'
                    else:
                        tgt[0] = 'inc'
                elif len(tgt) == 3:
                    if tgt[0] == 'jnz':
                        tgt[0] = 'cpy'
                    else:
                        tgt[0] = 'jnz'
                program[pc + x] = tgt
            pc += 1

    return registers

# part one
registers = execute(initA=7)
print(registers['a'])

# part two
registers = execute(initA=12)
print(registers['a'])

# findMul searches for lines of code that match this pattern:
""" cpy b c
    inc a
    dec c
    jnz c -2
    dec d
    jnz d -5
 -> a += b * d, c = 0, d = 0
 """
 # a b c and d must be distinct and a, c and d must be registers. b may just be a number
