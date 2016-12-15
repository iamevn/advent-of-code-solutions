#!/usr/bin/env python3

from sys import argv,exit

input_filename = "input"
if len(argv) > 1:
    input_filename = argv[1]

try:
    input = open(input_filename)
except OSError:
    exit("Cannot open file \"{}\"".format(input_filename))

# discs[N] = fn of one int that returns True if disc #N is aligned for that start time and false otherwise
discs = set()
for line in input:
    # Disc #N has P positions; at time=T, it is at position I.
    split = line.split()
    N = int(split[1][1:])
    P = int(split[3])
    T = int(split[6][5:-1])
    I = int(split[11][:-1])
    discs.add(lambda x, N=N, P=P, T=T, I=I: (x + N + I - T) % P == 0)
    # I dislike this but it's a neat hack

def search():
    i = -1
    done = False
    while not done:
        i += 1
        done = True # maybe
        for disc in discs:
            if not disc(i):
                done = False
    return i

print(search())

# part 2
discs.add(lambda x, N=len(discs)+1, P=11, T=0, I=0: (x + N + I - T) % P == 0)
print(search())
