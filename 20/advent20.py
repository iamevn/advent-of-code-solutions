#!/usr/bin/env python3

# IP RANGE [0 , 4294967295] inclusive

from sys import argv,exit

input_filename = "input"
if len(argv) > 1:
    input_filename = argv[1]

try:
    input = open(input_filename)
except OSError:
    exit("Cannot open file \"{}\"".format(input_filename))

# list of tuples representing disjoint, inclusive, ranges
allowed_ranges = [(0, 4294967295)]

def split_ranges(allowed_ranges, rlow, rhigh):
    new_ranges = []
    for low, high in allowed_ranges:

        # subrange starts in remove range
        if rlow <= low <= rhigh < high:
            new_ranges.append((rhigh + 1, high))

        # subrange ends in remove range
        elif low < rlow <= high <= rhigh:
            new_ranges.append((low, rlow - 1))

        # subrange contains range to remove
        elif low < rlow <= rhigh < high:
            new_ranges.append((low, rlow - 1))
            new_ranges.append((rhigh + 1, high))

        # subrange completely in range to remove 
        elif rlow <= low <= high <= rhigh:
            pass

        # range to remove not in subrange
        else:
            new_ranges.append((low, high))

    return new_ranges

for line in input:
    low, high = map(int, line.split('-'))
    allowed_ranges = split_ranges(allowed_ranges, low, high)

# part 1, lowest allowed
print(allowed_ranges[0][0])

# part 2, how many allowed
count = 0

for r in allowed_ranges:
    count += r[1] - r[0] + 1

print(count)
