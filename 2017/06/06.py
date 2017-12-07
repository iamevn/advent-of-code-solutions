#!/usr/bin/env python3

from sys import argv, exit

input_filename = "input"
if len(argv) > 1:
    input_filename = argv[1]

try:
    input = open(input_filename)
except OSError:
    exit(f'Cannot open file "{input_filename}"')

seq = [int(n) for n in input.readline().split()]

def maxindex(seq):
    i = 0
    max = -1
    max_i = -1

    while i < len(seq):
        if seq[i] > max:
            max = seq[i]
            max_i = i
        i += 1
    return max_i

def step(seq):
    seq = seq.copy()
    i = maxindex(seq)
    count = seq[i]
    seq[i] = 0
    while count > 0:
        i = (i + 1) % len(seq)
        seq[i] += 1
        count -= 1
    return seq

def findloop(seq):
    steps = 0
    found = [seq]
    while True:
        seq = step(seq)
        steps += 1
        if seq in found:
            return steps
        found.append(seq)

assert findloop([0, 2, 7, 0]) == 5
print(findloop(seq))

def looplen(seq):
    steps = 0
    found = [seq]
    while True:
        seq = step(seq)
        steps += 1
        if seq in found:
            break
        found.append(seq)
    lookingfor = seq.copy()
    steps = 0
    while True:
        seq = step(seq)
        steps += 1
        if seq == lookingfor:
            return steps

assert looplen([0, 2, 7, 0]) == 4
print(looplen(seq))
