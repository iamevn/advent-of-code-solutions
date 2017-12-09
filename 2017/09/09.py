#!/usr/bin/env python3

from sys import argv, exit
from collections import defaultdict

input_filename = "input"
if len(argv) > 1:
    input_filename = argv[1]

try:
    input = open(input_filename)
except OSError:
    exit(f'Cannot open file "{input_filename}"')

stream = input.readline()

def filtergarbage(stream):
    output = ""
    escaped = False
    commented = False
    cancelled = 0
    for c in stream:
        if escaped:
            escaped = False
        elif not commented:
            if c == '<':
                commented = True
            else:
                output += c
        elif commented:
            if escaped:
                pass
            elif c == '>':
                commented = False
            elif c == '!':
                escaped = True
            else:
                cancelled += 1
    return (output, cancelled)

assert filtergarbage('{}')[0] == '{}'
assert filtergarbage('{{{}}}')[0] == '{{{}}}'
assert filtergarbage('{{},{}}')[0] == '{{},{}}'
assert filtergarbage('{{{},{},{{}}}}')[0] == '{{{},{},{{}}}}'
assert filtergarbage('{<{},{},{{}}>}')[0] == '{}'
assert filtergarbage('{<a>,<a>,<a>,<a>}')[0] == '{,,,}'
assert filtergarbage('{{<ab>},{<ab>},{<ab>},{<ab>}}')[0] == '{{},{},{},{}}'
assert filtergarbage('{{<a>},{<a>},{<a>},{<a>}}')[0] == '{{},{},{},{}}'
assert filtergarbage('{{<!>},{<!>},{<!>},{<a>}}')[0] == '{{}}'

def scoregroups(stream):
    stream = filtergarbage(stream)[0]
    sum = 0
    depth = 0
    for c in stream:
        if c == '{':
            depth += 1
            sum += depth
        elif c == '}':
            depth -= 1
    return sum

assert scoregroups('{}') == 1
assert scoregroups('{{{}}}') == 6
assert scoregroups('{{},{}}') == 5
assert scoregroups('{{{},{},{{}}}}') == 16
assert scoregroups('{<{},{},{{}}>}') == 1
assert scoregroups('{<a>,<a>,<a>,<a>}') == 1
assert scoregroups('{{<ab>},{<ab>},{<ab>},{<ab>}}') == 9
assert scoregroups('{{<a>},{<a>},{<a>},{<a>}}') == 9
assert scoregroups('{{<!>},{<!>},{<!>},{<a>}}') == 3

print(scoregroups(stream))

assert filtergarbage('<>')[1] == 0
assert filtergarbage('<random characters>')[1] == 17
assert filtergarbage('<<<<>')[1] == 3
assert filtergarbage('<{!>}>')[1] == 2
assert filtergarbage('<!!>')[1] == 0
assert filtergarbage('<!!!>>')[1] == 0
assert filtergarbage('<{o"i!a,<{i<a>')[1] == 10

print(filtergarbage(stream)[1])
