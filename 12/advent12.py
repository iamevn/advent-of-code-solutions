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
registers = {'a':0, 'b':0, 'c':0, 'd':0}

for line in input:
    program.append(line.split())

pc = 0

while pc < len(program):
    if pc < 0:
        pc = 0
    fetch = program[pc]

    if   fetch[0] == 'cpy':
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

print(registers)
