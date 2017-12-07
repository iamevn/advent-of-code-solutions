#!/usr/bin/env python3

from sys import argv,exit

input_filename = "input"
the_string = "abcdefgh"
if len(argv) > 1:
    input_filename = argv[1]

def scramble(st, dbg=False):
    try:
        input = open(input_filename)
    except OSError:
        exit("Cannot open file \"{}\"".format(input_filename))

    # swap pos X with pos Y (0 indexed)
    def swap_pos(s, X, Y):
        tmp = ""
        for i in range(len(s)):
            if i == X:
                tmp += s[Y]
            elif i == Y:
                tmp += s[X]
            else:
                tmp += s[i]
        return tmp
    # swap letter X with letter Y
    def swap_letter(s, X, Y):
        tmp = ""
        for c in s:
            if c == X:
                tmp += Y
            elif c == Y:
                tmp += X
            else:
                tmp += c
        return tmp
    # rotate left/right X steps
    def rotate_right(s, X):
        for i in range(X):
            s = s[-1] + s[:-1]
        return s
    def rotate_left(s, X):
        for i in range(X):
            s = s[1:] + s[0]
        return s
    # rotate based on position of letter X (r rotate 1 + index of X times + (index >= 4 ? 1 : 0)
    def rotate_pos(s, X):
        pos = s.find(X)
        rotations = 1 + pos
        if pos >= 4:
            rotations += 1
        return rotate_right(s, rotations)
    # reverse positions X through Y (inclusive)
    def reverse(s, X, Y):
        tmp = s[:X]
        for i in range(Y, X - 1, -1):
            tmp += s[i]
        tmp += s[Y+1:]
        return tmp
    # move position X to position Y
    def move(s, X, Y):
        tmp = ""
        for i in range(len(s)):
            if i == X:
                pass
            elif i == Y and Y > X:
                tmp += s[i]
                tmp += s[X]
            elif i == Y and Y < X:
                tmp += s[X]
                tmp += s[i]
            else:
                tmp += s[i]
        return tmp

    for line in input:
        if dbg:
            print(st)
        spline = line.split()
        if spline[0] == 'swap' and spline[1] == 'position':
            st = swap_pos(st, int(spline[2]), int(spline[5]))
        elif spline[0] == 'swap' and spline[1] == 'letter':
            st = swap_letter(st, spline[2], spline[5])
        elif spline[0] == 'rotate' and spline[1] == 'right':
            st = rotate_right(st, int(spline[2]))
        elif spline[0] == 'rotate' and spline[1] == 'left':
            st = rotate_left(st, int(spline[2]))
        elif spline[0] == 'rotate' and spline[1] == 'based':
            st = rotate_pos(st, spline[6])
        elif spline[0] == 'reverse':
            st = reverse(st, int(spline[2]), int(spline[4]))
        elif spline[0] == 'move':
            st = move(st, int(spline[2]), int(spline[5]))

    return st

print('scrambling..... ' + scramble(the_string, dbg=False))

def unscramble(st, dbg=False):
    try:
        input = open(input_filename)
    except OSError:
        exit("Cannot open file \"{}\"".format(input_filename))

    # REVERSED FUNCTIONS
    # swap pos X with pos Y (0 indexed)
    def swap_pos(s, X, Y):
        tmp = ""
        for i in range(len(s)):
            if i == X:
                tmp += s[Y]
            elif i == Y:
                tmp += s[X]
            else:
                tmp += s[i]
        return tmp
    # swap letter X with letter Y
    def swap_letter(s, X, Y):
        tmp = ""
        for c in s:
            if c == X:
                tmp += Y
            elif c == Y:
                tmp += X
            else:
                tmp += c
        return tmp
    # rotate left/right X steps
    def rotate_right(s, X):
        for i in range(X):
            s = s[1:] + s[0]
        return s
    def rotate_left(s, X):
        for i in range(X):
            s = s[-1] + s[:-1]
        return s
    # rotate based on position of letter X (r rotate 1 + index of X times + (index >= 4 ? 1 : 0)
    def rotate_pos(s, X):
        pos = s.find(X)
        if pos == 0:
            pos = len(s) - 1
        elif pos % 2 == 0:
            pos += len(s) - 2
            pos /= 2
        else:
            pos -= 1
            pos /= 2

        desired = int(pos)
        return rotate_right(s, len(s) - desired + s.find(X))
    # reverse positions X through Y (inclusive)
    def reverse(s, X, Y):
        tmp = s[:X]
        for i in range(Y, X - 1, -1):
            tmp += s[i]
        tmp += s[Y+1:]
        return tmp
    # move position X to position Y
    def move(s, X, Y):
        tmp = ""
        for i in range(len(s)):
            if i == Y:
                pass
            elif i == X and X > Y:
                tmp += s[i]
                tmp += s[Y]
            elif i == X and X < Y:
                tmp += s[Y]
                tmp += s[i]
            else:
                tmp += s[i]
        return tmp

    # reverse it
    lines = []
    for line in input:
        lines.append(line)
    lines.reverse()

    for line in lines:
        if dbg:
            print(st)
        spline = line.split()
        if spline[0] == 'swap' and spline[1] == 'position':
            st = swap_pos(st, int(spline[2]), int(spline[5]))
        elif spline[0] == 'swap' and spline[1] == 'letter':
            st = swap_letter(st, spline[2], spline[5])
        elif spline[0] == 'rotate' and spline[1] == 'right':
            st = rotate_right(st, int(spline[2]))
        elif spline[0] == 'rotate' and spline[1] == 'left':
            st = rotate_left(st, int(spline[2]))
        elif spline[0] == 'rotate' and spline[1] == 'based':
            st = rotate_pos(st, spline[6])
        elif spline[0] == 'reverse':
            st = reverse(st, int(spline[2]), int(spline[4]))
        elif spline[0] == 'move':
            st = move(st, int(spline[2]), int(spline[5]))

    return st

print('unscrambling... ' + unscramble('fbgdceah'))
assert(unscramble(scramble(the_string)) == the_string)
assert(scramble(unscramble(the_string)) == the_string)
