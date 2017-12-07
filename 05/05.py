#!/usr/bin/env python3

from sys import argv, exit

input_filename = "input"
if len(argv) > 1:
    input_filename = argv[1]

try:
    input = open(input_filename)
except OSError:
    exit(f'Cannot open file "{input_filename}"')

sequence = [int(n) for n in input]

def steps_until_out(seq):
    seq = seq.copy()
    bounds = (0, len(seq))
    ptr = 0
    steps = 0
    while ptr >= bounds[0] and ptr < bounds[1]:
        offset = seq[ptr]
        seq[ptr] += 1
        ptr += offset
        steps += 1

    return steps

assert steps_until_out([0, 3, 0, 1, -3]) == 5

print(steps_until_out(sequence))

def steps_until_out_mod(seq):
    seq = seq.copy()
    bounds = (0, len(seq))
    ptr = 0
    steps = 0
    while ptr >= bounds[0] and ptr < bounds[1]:
        offset = seq[ptr]
        if offset >= 3:
            seq[ptr] -= 1
        else:
            seq[ptr] += 1
        ptr += offset
        steps += 1

    return steps

assert steps_until_out_mod([0, 3, 0, 1, -3]) == 10

print(steps_until_out_mod(sequence))
