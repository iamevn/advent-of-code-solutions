#!/usr/bin/env python3

from sys import argv,exit

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


print(len(out) - 1)
print(length - 1)
print(out)


# part 2
input.seek(0)

