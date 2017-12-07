#!/usr/bin/env python3

from sys import argv, exit

input_filename = "input"
if len(argv) > 1:
    input_filename = argv[1]

try:
    input = open(input_filename)
except OSError:
    exit(f'Cannot open file "{input_filename}"')

table = []

for line in input:
    table.append([int(n) for n in line.split()])

def checksum(table):
    """sum of the max-min for each line"""
    sum = 0
    for line in table:
        min = line[0]
        max = line[0]

        for n in line:
            if n < min:
                min = n
            if n > max:
                max = n

        sum += max - min
    return sum

assert checksum([[5, 1, 9, 5], [7, 5, 3], [2, 4, 6, 8]]) == 18

print(checksum(table))

def divsum(table):
    """sum of m/n for each line where m is divisible by n"""
    sum = 0
    for line in table:
        found = None
        for i in range(len(line)):
            for j in range(len(line)):
                if i != j:
                    if line[i] % line[j] == 0:
                        found = int(line[i]/line[j])
            if found != None:
                break
        sum += found
    return sum

assert divsum([[5, 9, 2, 8], [9, 4, 7, 3], [3, 8, 6, 5]]) == 9

print(divsum(table))
