#!/usr/bin/env python3

from hashlib import md5
import sys

doorid = b"abbhdwsy"
password = ""

print("________\r", end='')

def check(i):
    m = md5(doorid + str(i).encode()).hexdigest()
    for c in m[0:5]:
        if c != '0':
            return False
    return m[5]

i = 0
while len(password) < 8:
    found = check(i)
    if found:
        print(found, end='')
        sys.stdout.flush()

        password = password + found
    i += 1

print('')

# part 2

def check2(i):
    m = md5(doorid + str(i).encode()).hexdigest()
    for c in m[0:5]:
        if c != '0':
            return False, False, False
    return True, int(m[5], base=16), m[6]

password = "________\r"
print(password, end='')

i = 0
while '_' in password:
    found, index, char = check2(i)
    if  found \
    and index in range(8) \
    and password[index] == '_':
        password = password[:index] + char + password[index+1:]
        print(password, end='')
    i += 1

print('')

