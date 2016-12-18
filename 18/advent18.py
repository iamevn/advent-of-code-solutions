#!/usr/bin/env python3

from sys import argv, exit

input_filename = "input"
if len(argv) > 1:
    input_filename = argv[1]

try:
    input = open(input_filename)
except OSError:
    exit("Cannot open file \"{}\"".format(input_filename))

first_line = input.readline()
# get rid of newline character
if first_line[-1] == '\n':
    first_line = first_line[:-1]

# tile is trap iff
# Its left and center tiles are traps, but its right tile is not.
# Its center and right tiles are traps, but its left tile is not.
# Only its left tile is a trap.
# Only its right tile is a trap.
def trapCheck(L, C, R):
    if (L == C == '^' and R == '.')\
    or (C == R == '^' and L == '.')\
    or (C == R == '.' and L == '^')\
    or (L == C == '.' and R == '^'):
        return '^'
    else:
        return '.'

def nextRow(prev):
    # first edge tile
    new = trapCheck('.', prev[0], prev[1])
    # middle tiles
    for i in range(1, len(prev) - 1):
        new += trapCheck(prev[i - 1], prev[i], prev[i + 1])
    # last edge tile
    new += trapCheck(prev[-2], prev[-1], '.')
    return new

assert nextRow("..^^.") == ".^^^^"
assert nextRow(".^^^^") == "^^..^"

def countSafe(start, rows):
    safes = 0
    current_row = start
    while rows > 0:
        for c in current_row:
            if c == '.':
                safes += 1
        rows -= 1
        current_row = nextRow(current_row)
    return safes

assert countSafe(".^^.^.^^^^", 10) == 38
print(countSafe(first_line, 40))

# part 2
print(countSafe(first_line, 400000))
