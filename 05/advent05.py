#!/usr/bin/env python3

from hashlib import md5
import sys, random

print("HACKING EASTER.EXE")

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
timer = 10000
while len(password) < 8:
    found = check(i)
    if found:
        password = password + found
    if timer == 0:
        print('\rhacking...', end='')
        print(password, end='')
        for j in range(8 - len(password)):
            c = hex(random.randint(0,15))[-1]
            print(c, end='')
        timer = 10000
    else:
        timer -= 1

    i += 1

print('\rhacking...' + password)

# part 2

def check2(i):
    m = md5(doorid + str(i).encode()).hexdigest()
    for c in m[0:5]:
        if c != '0':
            return False, False, False
    return True, int(m[5], base=16), m[6]

password = "________"
print('\ralmost....' + password, end='')

i = 0
timer = 10000

def printHax(p):
    print('\ralmost....', end='')
    for c in p:
        if c == '_':
            c = hex(random.randint(0,15))[-1]
        print(c, end='')

while '_' in password:
    found, index, char = check2(i)
    if  found \
    and index in range(8) \
    and password[index] == '_':
        password = password[:index] + char + password[index+1:]
    i += 1
    if timer == 0:
        printHax(password)
        timer = 10000
    else:
        timer -= 1

print('\ralmost....' + password)
print('\n*hacker voice* I\'m in')

