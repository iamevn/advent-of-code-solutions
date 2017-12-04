#!/usr/bin/env python3

from sys import argv, exit

input_filename = "input"
if len(argv) > 1:
    input_filename = argv[1]

try:
    input = open(input_filename)
except OSError:
    exit(f'Cannot open file "{input_filename}"')

seq = []
for line in input:
    for c in line:
        if not c in "0123456789":
            pass
        else:
            seq.append(int(c))


def part1(sequence):
    """add each number in sequence if they match the next number in sequence"""
    sum = 0
    for i in range(len(sequence)):
        if sequence[i] == sequence[(i + 1) % len(sequence)]:
            sum += sequence[i]
    return sum


assert part1([1, 1, 2, 2]) == 3
assert part1([1, 1, 1, 1]) == 4
assert part1([1, 2, 3, 4]) == 0
assert part1([9, 1, 2, 1, 2, 1, 2, 9]) == 9

print(part1(seq))

def part2(sequence):
    """add each number in sequence if they match the number halfway around the sequence"""
    sum = 0
    L = len(sequence)
    for i in range(L):
        if sequence[i] == sequence[(i + int(L / 2)) % L]:
            sum += sequence[i]
    return sum

assert(part2([1, 2, 1, 2]) == 6)
assert(part2([1, 2, 2, 1]) == 0)
assert(part2([1, 2, 3, 4, 2, 5]) == 4)
assert(part2([1, 2, 3, 1, 2, 3]) == 12)
assert(part2([1, 2, 1, 3, 1, 4, 1, 5]) == 4)

print(part2(seq))
