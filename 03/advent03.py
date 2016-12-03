#!/usr/bin/env python3

from sys import argv,exit

input_filename = "input"
if len(argv) > 1:
    input_filename = argv[1]

try:
    input = open(input_filename)
except OSError:
    exit("Cannot open file \"{}\"".format(input_filename))

def check(a, b, c):
    return int(a) + int(b) > int(c)

def checktri(sides):
    return check(sides[0], sides[1], sides[2]) \
       and check(sides[0], sides[2], sides[1]) \
       and check(sides[1], sides[0], sides[2]) \
       and check(sides[1], sides[2], sides[0])

possible_count = 0

for line in input:
    if checktri(line.split()):
        possible_count += 1

print(str(possible_count))

# part 2

input.seek(0)
possible_count = 0

# i hate this
for line1 in input:
    line2 = input.readline()
    line3 = input.readline()
    sidesA = line1.split()
    sidesB = line2.split()
    sidesC = line3.split()

# so much
    sides1 = [sidesA[0], sidesB[0], sidesC[0]]
    sides2 = [sidesA[1], sidesB[1], sidesC[1]]
    sides3 = [sidesA[2], sidesB[2], sidesC[2]]

    if checktri(sides1):
        possible_count += 1
    if checktri(sides2):
        possible_count += 1
    if checktri(sides3):
        possible_count += 1

print(str(possible_count))
