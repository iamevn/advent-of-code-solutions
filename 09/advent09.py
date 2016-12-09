#!/usr/bin/env python3

from sys import argv,exit,setrecursionlimit

input_filename = "input"
if len(argv) > 1:
    input_filename = argv[1]

try:
    input = open(input_filename)
except OSError:
    exit("Cannot open file \"{}\"".format(input_filename))

out = ""
length = 0

inParen = False
firstArg = False
count = ""
repeats = ""
subject = ""
marker = False
for line in input:
    for c in line:
        if not marker:
            if not inParen:
                if c == '(':
                    inParen = True
                    firstArg = True
                else:
                    out += c
                    length += 1
            else:
                if firstArg:
                    if not c == 'x':
                        count += c
                    else:
                        count = int(count)
                        firstArg = False
                else:
                    if not c == ')':
                        repeats += c
                    else:
                        repeats = int(repeats)
                        inParen = False
                        marker = True
                        subject = ""
                        length += count * repeats
        else:
            if count > 0:
                subject += c
                count -= 1
            if count == 0:
                while repeats > 0:
                    out += subject
                    repeats -= 1
                inParen = False
                firstArg = False
                count = ""
                repeats = ""
                subject = ""
                marker = False


print(length - 1) # minus the newline


# part 2
input.seek(0)

line = input.readline()[:-1] #chop off '\n'
linelen = len(line)
outlen = 0

setrecursionlimit(999999999)
# recursively find length of a section of line
def sectionLength(start, length):
    secLen = 0
    ii = start
    while ii < length + start:
        # secLen += 1
        # ii += 1
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
