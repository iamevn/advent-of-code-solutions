#!/usr/bin/env python3

from hashlib import md5
import sys

doorid = b"abbhdwsy"
password = ""

print("________\r", end='')

def check(i):
    m = md5(doorid + str(i).encode()).digest()
    if m[0] & b'\xFF'[0] == 0 \
    and m[1] & b'\xFF'[0] == 0\
    and m[2] & b'\xF0'[0] == 0:
        return True, toChar(m[2] & b'\x0F'[0])
    else:
        return False, False

def toChar(i):
    return hex(i)[-1]

i = 0
while len(password) < 8:
    found, g = check(i)
    if found:
        print("{}".format(g), end='')
        sys.stdout.flush()

        password = password + g
    i += 1

print('')

# part 2

def check2(i):
    m = md5(doorid + str(i).encode()).digest()
    if m[0] & b'\xFF'[0] == 0 \
    and m[1] & b'\xFF'[0] == 0\
    and m[2] & b'\xF0'[0] == 0:
        return True, int(m[2] & b'\x0F'[0]), toChar(m[3] >> 4)
    else:
        return False, False, False

password = "________\r"
print(password, end='')

i = 0
while '_' in password:
    found, index, char = check2(i)
    if found \
    and index >= 0 \
    and index < 8 \
    and password[index] == '_':
        password = password[:index] + char + password[index+1:]
        print(password, end='')
    i += 1

print('')

