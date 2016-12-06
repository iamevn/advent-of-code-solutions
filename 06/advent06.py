#!/usr/bin/env python3

from sys import argv,exit

input_filename = "input"
if len(argv) > 1:
    input_filename = argv[1]

try:
    input = open(input_filename)
except OSError:
    exit("Cannot open file \"{}\"".format(input_filename))

lineLen = len(input.readline()) - 1
input.seek(0)

slots = {}
for i in range(lineLen):
    slots[i] = {}

for line in input:
    for i in range(lineLen):
        if line[i] in slots[i]:
            slots[i][line[i]] += 1
        else:
            slots[i][line[i]] = 1

def mostCommonIn(dict):
    guess = ''
    count = 0
    for key in dict:
        if dict[key] > count:
            guess = key
            count = dict[key]
    return guess

for i in range(lineLen):
    print(mostCommonIn(slots[i]), end='')

print("")



# part 2
def leastCommonIn(dict):
    guess = ''
    count = float('inf')
    for key in dict:
        if dict[key] < count:
            guess = key
            count = dict[key]
    return guess

for i in range(lineLen):
    print(leastCommonIn(slots[i]), end='')

print("")
