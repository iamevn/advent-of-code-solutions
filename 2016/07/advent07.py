#!/usr/bin/env python3

from sys import argv,exit

input_filename = "input"
if len(argv) > 1:
    input_filename = argv[1]

try:
    input = open(input_filename)
except OSError:
    exit("Cannot open file \"{}\"".format(input_filename))

tls_count = 0

def hasABBA(s):
    for i in range(len(s) - 3):
        if s[i] == s[i+3] and s[i+1] == s[i+2] and not s[i] == s[i+1]:
            return True
    return False

for line in input:
    sections = line.replace('[', '$').replace(']', '$').split('$')
    good = False
    bad = False
    for i in range(len(sections)):
        if i%2 == 0 and hasABBA(sections[i]):
            good = True
        if i%2 == 1 and hasABBA(sections[i]):
            bad = True
    if good and not bad:
        tls_count += 1


print('TLS: ' + str(tls_count))



# part 2

ssl_count = 0
input.seek(0)

def findABA(s):
    ABAs = []
    for i in range(len(s) - 2):
        if s[i] == s[i+2] and not s[i] == s[i+1]:
            ABAs.append(s[i] + s[i+1] + s[i+2])
    return ABAs

def findBAB(s):
    BABs = []
    for i in range(len(s) - 2):
        if s[i] == s[i+2] and not s[i] == s[i+1]:
            BABs.append(s[i+1] + s[i] + s[i+1])
    return BABs

for line in input:
    sections = line.replace('[', '$').replace(']', '$').split('$')
    nonhyper = []
    hypers = []
    for i in range(len(sections)):
        if i%2 == 0:
            nonhyper.append(sections[i])
        else:
            hypers.append(sections[i])

    ABAs = []

    done = False
    for e in nonhyper:
        for found in findABA(e):
            ABAs.append(found)
    for e in hypers:
        for found in findBAB(e):
            if found in ABAs:
                if not done:
                    ssl_count += 1
                done = True


print('SSL: ' + str(ssl_count))

