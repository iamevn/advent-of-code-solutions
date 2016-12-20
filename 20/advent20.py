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

lowest_allowed = 0
for line in input:
    low, high = map(int, line.split('-'))
    if low <= lowest_allowed <= high:
        lowest_allowed = high + 1
        input.seek(0)

print(lowest_allowed)
