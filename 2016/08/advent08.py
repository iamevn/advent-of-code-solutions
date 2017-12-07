#!/usr/bin/env python3

from sys import argv,exit

input_filename = "input"
if len(argv) > 1:
    input_filename = argv[1]

try:
    input = open(input_filename)
except OSError:
    exit("Cannot open file \"{}\"".format(input_filename))

display = {}

WIDTH = 50
HEIGHT = 6

for x in range(WIDTH):
    for y in range(HEIGHT):
        display[x,y] = False

# rect AxB
def rect(A, B):
    for x in range(A):
        for y in range(B):
            display[x,y] = True

# rotate row y=A by B
def rowRot(y, B):
    new = {}
    for x in range(WIDTH):
        new[x] = display[(x - B) % WIDTH, y]
    for x in range(WIDTH):
        display[x, y] = new[x]
# rotate column x=A by B
def colRot(x, B):
    new = {}
    for y in range(HEIGHT):
        new[y] = display[x, (y - B) % HEIGHT]
    for y in range(HEIGHT):
        display[x, y] = new[y]

for line in input:
    words = line.split()
    if words[0] == 'rect':
        # rect AxB
        A, B = words[1].split('x')
        rect(int(A), int(B))
    elif words[1] == 'row':
        # rotate row y=A by B
        A = int(words[2][2:])
        B = int(words[4])
        rowRot(A, B)
    elif words[1] == 'column':
        # rotate column x=A by B
        A = int(words[2][2:])
        B = int(words[4])
        colRot(A, B)

count = 0
for x in range(WIDTH):
    for y in range(HEIGHT):
        if display[x,y]:
            count += 1

print(count)
# part 2

for y in range(HEIGHT):
    for x in range(WIDTH):
        if display[x,y]:
            print('#',end='')
        else:
            print('.',end='')
    print('')
input.seek(0)

