#!/usr/bin/env python3

from hashlib import md5
import sys, random

print("\033[7mHACKING EASTER.EXE\033[0m")

doorid = b"abbhdwsy"
password = ""

GREEN   = '\033[92m'
NORMAL = '\033[0m'
RED    = '\033[91m'
BLINK  = '\033[5m'

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
        print('\r' + BLINK + 'hacking' + NORMAL + '...', end='')
        print(GREEN + password + NORMAL, end='')
        for j in range(8 - len(password)):
            c = hex(random.randint(0,15))[-1]
            print(RED + c + NORMAL, end='')
        timer = 10000
    else:
        timer -= 1

    i += 1

print('\rhacking...' + GREEN + password)

# part 2

def check2(i):
    m = md5(doorid + str(i).encode()).hexdigest()
    for c in m[0:5]:
        if c != '0':
            return False, False, False
    return True, int(m[5], base=16), m[6]

password = "________"
print('\r' + BLINK + 'almost' + NORMAL + '....' + password, end='')

i = 0
timer = 10000

def printHax(p):
    print('\r' + BLINK + 'almost' + NORMAL + '....', end='')
    for c in p:
        if c == '_':
            c = hex(random.randint(0,15))[-1]
            print(RED + c + NORMAL, end='')
        else:
            print(GREEN + c + NORMAL, end='')

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

print('\ralmost....' + GREEN + password + NORMAL)
print('\n*hacker voice* I\'m in')

