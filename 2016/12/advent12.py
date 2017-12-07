#!/usr/bin/env python3

from sys import argv,exit

input_filename = "input"
if len(argv) > 1:
    input_filename = argv[1]

try:
    input = open(input_filename)
except OSError:
    exit("Cannot open file \"{}\"".format(input_filename))

program = []

for line in input:
    program.append(line.split())

def execute(program, initA=0, initB=0, initC=0, initD=0):
    registers = {'a':initA, 'b':initB, 'c':initC, 'd':initD}
    pc = 0

    while pc < len(program):
        if pc < 0:
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
            registers[dst] = src
            pc += 1
        elif fetch[0] == 'inc':
            reg = fetch[1]
            registers[reg] += 1
            pc += 1
        elif fetch[0] == 'dec':
            reg = fetch[1]
            registers[reg] -= 1
            pc += 1
        elif fetch[0] == 'jnz':
            src = fetch[1]
            if src in registers:
                src = registers[src]
            else:
                src = int(src)
            tgt = int(fetch[2])
            if src != 0:
                pc += tgt
            else:
                pc += 1
    return registers

# part one
registers = execute(program)
print(registers['a'])
# part two
registers = execute(program, initC=1)
print(registers['a'])
