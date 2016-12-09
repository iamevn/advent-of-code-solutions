#!/usr/bin/env python3

from sys import argv,exit,setrecursionlimit

input_filename = "input"
if len(argv) > 1:
    input_filename = argv[1]

try:
    input = open(input_filename)
except OSError:
    exit("Cannot open file \"{}\"".format(input_filename))

line = input.readline()[:-1] #chop off '\n'
linelen = len(line)
outlen = 0

i = 0
while i < linelen:
    if line[i] == '(':
        j = i
        while line[j] != ')':
            j += 1
        repLen, repCount = line[i+1:j].split('x')
        repLen = int(repLen)
        repCount = int(repCount)
        addedLen = repLen * repCount 
        outlen += addedLen
        i = j + repLen + 1
    else:
        outlen += 1
        i += 1

print(outlen)


# part 2

outlen = 0

setrecursionlimit(50)
# recursively find length of a section of line
def sectionLength(start, length):
    secLen = 0
    ii = start
    while ii < length + start:
        if line[ii] == '(':
            jj = ii
            while line[jj] != ')':
                jj += 1
            repLen, repCount = line[ii+1:jj].split('x')
            repLen = int(repLen)
            repCount = int(repCount)
            secLen += sectionLength(jj+1, repLen) * repCount
            ii = jj + repLen + 1
        else:
            secLen += 1
            ii += 1

    return secLen

i = 0
while i < linelen:
    if line[i] == '(':
        j = i
        while line[j] != ')':
            j += 1
        repLen, repCount = line[i+1:j].split('x')
        repLen = int(repLen)
        repCount = int(repCount)
        addedLen = sectionLength(j+1, repLen) * repCount 
        outlen += addedLen
        i = j + repLen + 1
    else:
        outlen += 1
        i += 1

print(outlen)
