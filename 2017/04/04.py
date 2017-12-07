#!/usr/bin/env python3

from sys import argv, exit

input_filename = "input"
if len(argv) > 1:
    input_filename = argv[1]

try:
    input = open(input_filename)
except OSError:
    exit(f'Cannot open file "{input_filename}"')

valid = 0

for passphrase in input:
    words = passphrase.split()
    if len(words) == len(set(words)):
        valid += 1

print(valid)

valid = 0
input = open(input_filename)
for passphrase in input:
    words = ["".join(sorted(word)) for word in passphrase.split()]
    if len(words) == len(set(words)):
        valid += 1

print(valid)
