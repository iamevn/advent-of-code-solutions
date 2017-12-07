#!/usr/bin/env python3

from sys import argv

input = 277678

if len(argv) > 1:
    input = int(argv[1])

"""
37  36  35  34  33  32  31
38  17  16  15  14  13  30
38  18   5   4   3  12  29
40  19   6   1   2  11  28
41  20   7   8   9  10  27
42  21  22  23  24  25  26
43  44  45  46  47  48  49 

down to the right diagonal is odd squares,
up to the left is even squares + 1

idea: use sqrt to find which ring n is in
    ring(n):
        if sqrt(n) is odd, in bottom right diagonal of ((sqrt(n) - 1) / 2)th ring
        if floor(sqrt(n)) is even, in bottom left side of (floor(sqrt(n)) / 2)th ring
        if floor(sqrt(n)) is odd, in top right side of (ceil(sqrt(n)) / 2)th ring
find how far from nearest diagonal and from that how far from nearest straight path
for a ring, n, diagonals are:
    bottom right: (n * 2) + 1 ** 2
    top left: (n * 2) ** 2 + 1
    bottom left: avg(bottom right, top left)
"""

def shortest_path(n):
    def ring(n):
        from math import sqrt, floor, ceil
        if sqrt(n) % 2 == 1:
            return (sqrt(n) - 1) // 2
        elif floor(sqrt(n)) % 2 == 0:
            return floor(sqrt(n)) // 2
        else:
            return ceil(sqrt(n)) // 2

    r = ring(n)
    BR = ((r * 2) + 1) ** 2
    TL = ((r * 2) ** 2) + 1
    BL = (BR + TL) // 2
    TR = BL - (BR - TL)
    BR0 = TR - (BR - BL)
    R = (BR0 + TR) // 2
    T = (TR + TL) // 2
    L = (TL + BL) // 2
    B = (BL + BR) // 2

    if n < TR:
        return r + abs(n - R)
    elif n < TL:
        return r + abs(n - T)
    elif n < BL:
        return r + abs(n - L)
    else:
        return r + abs(n - B)



assert shortest_path(1) == 0
assert shortest_path(12) == 3
assert shortest_path(23) == 2
assert shortest_path(1024) == 31

print(shortest_path(input))

# part 2
"""
147  142  133  122   59
304    5    4    2   57
330   10    1    1   54
351   11   23   25   26
362  747  806--->   ...

start from center with a 1. spiral outward setting each cell to the sum of its neighbors (only the neighbors which have values yet)
spiral by moving 1 right, 1 up, 2 left, 2 down, 3 right, 3 up, 4 left, 4 down etc
get neighbors the usual way

if we cared about memory we could free up rings as we move past them by 2 rings but this should grow fast enough to not be a problem
"""
from collections import defaultdict
d = defaultdict(lambda: 0)
d[(0, 0)] = 1


def nextspace():
    # yield spiral coords forever
    def dir():
        while True:
            yield lambda space: (space[0] + 1, space[1]) # right
            yield lambda space: (space[0], space[1] + 1) # up
            yield lambda space: (space[0] - 1, space[1]) # left
            yield lambda space: (space[0], space[1] - 1) # down
    def distance():
        d = 1
        while True:
            yield d
            yield d
            d += 1
    D = dir()
    M = distance()
    space = (0, 0)
    steps = 0
    nextspace = lambda x: x
    while True:
        if steps == 0:
            steps = next(M)
            nextspace = next(D)
        space = nextspace(space)
        steps -= 1
        yield space


def neighbors(space):
    # yield neighbors of given space tuple
    ns = [(-1, -1), (0, -1), (1, -1),
          (-1,  0),          (1,  0),
          (-1,  1), (0,  1), (1,  1)]
    for n in ns:
        yield (space[0] + n[0], space[1] + n[1])

for space in nextspace():
    sum = 0
    for n in neighbors(space):
        sum += d[n]
    d[space] = sum
    if sum > input:
        print(sum)
        break
