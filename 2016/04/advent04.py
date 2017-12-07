#!/usr/bin/env python3

from sys import argv,exit

input_filename = "input"
if len(argv) > 1:
    input_filename = argv[1]

try:
    input = open(input_filename)
except OSError:
    exit("Cannot open file \"{}\"".format(input_filename))

sum = 0

def matches(letters, cksum):
    #if any letters not in cksum are greater than those in cksum, false
    #else true
    for c in cksum:
        if not c in letters:
            return False
    for l in letters:
        if not l in cksum:
            for c in cksum:
                if letters[l] > letters[c]:
                    return False
                if letters[l] == letters[c] and ord(l) < ord(c):
                    return False
    return True

for line in input:
    words = line.split("-")
    end = words[-1]
    number, cksum = end.split("[")
    number = int(number)
    cksum = cksum[0:-2]
    words = words[0:-1]
    lettercounts = {}
    for word in words:
        for c in word:
            if c in lettercounts:
                lettercounts[c] += 1
            else:
                lettercounts[c] = 1
    if matches(lettercounts, cksum):
        sum += number


print(sum)
# part 2

input.seek(0)

def incChar(ch, n):
    new = ord(ch) + (n % 26)
    if new > ord('z'):
        new -= 26
    return chr(new)

def decode(words, number):
    line = ""
    for word in words:
        str = ""
        for char in word:
            str = str + incChar(char, number)
        line = line + str + " "
    print("{} : {}".format(line, number))
        


for line in input:
    words = line.split("-")
    end = words[-1]
    number, cksum = end.split("[")
    number = int(number)
    cksum = cksum[0:-2]
    words = words[0:-1]
    lettercounts = {}
    for word in words:
        for c in word:
            if c in lettercounts:
                lettercounts[c] += 1
            else:
                lettercounts[c] = 1
    if matches(lettercounts, cksum):
        decode(words, number)
