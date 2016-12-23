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

    while pc < len(program):
        if pc < 0:
            print("below 0")
            pc = 0
            # this may be wrong. it's not in the spec so this is my interpretation.
            # the given input probably doesn't even jump to a negetive position. 
        fetch = program[pc]

        if fetch[0] == 'cpy':
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
