#!/usr/bin/env python3

from sys import argv, exit
from collections import defaultdict

input_filename = "input"
if len(argv) > 1:
    input_filename = argv[1]

try:
    input = open(input_filename)
except OSError:
    exit(f'Cannot open file "{input_filename}"')

input = [line for line in input]
testinput = ["b inc 5 if a > 1", "a inc 1 if b < 5", "c dec -10 if a >= 1", "c inc -20 if c == 10"]

def run(program):
    registers = defaultdict(lambda: 0)
    max = 0
    def checkcond(left, cond, right):
        fns = {'>' : lambda l, r: l > r,
               '<' : lambda l, r: l < r,
               '>=': lambda l, r: l >= r,
               '<=': lambda l, r: l <= r,
               '==': lambda l, r: l == r,
               '!=': lambda l, r: l != r}
        if left.isdigit() or (left[0] == '-' and left[1:].isdigit()):
            left = int(left)
        else:
            left = registers[left]
        if right.isdigit() or (right[0] == '-' and right[1:].isdigit()):
            right = int(right)
        else:
            right = registers[right]

        return fns[cond](left, right)

    for line in program:
        split = line.split()
        if checkcond(*split[-3:]):
            reg = split[0]
            amt = int(split[2])
            if split[1] == 'inc':
                registers[reg] += amt
            elif split[1] == 'dec':
                registers[reg] -= amt

            if registers[reg] > max:
                max = registers[reg]
    return (registers, max)

def part1(input):
    registers = run(input)[0]
    max = 0
    for v in registers.values():
        if v > max:
            max = v
    return max
assert part1(testinput) == 1

print(part1(input))

def part2(input):
    return run(input)[1]

assert part2(testinput) == 10

print(part2(input))
