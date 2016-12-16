#!/usr/bin/env python3

def next_iteration(data):
    a = data
    b = ""

    for c in data:
        if c == '1':
            b += '0'
        else:
            b += '1'

    return a + '0' + b[::-1]

assert(next_iteration('1') == '100')
assert(next_iteration('0') == '001')
assert(next_iteration('11111') == '11111000000')
assert(next_iteration('111100001010') == '1111000010100101011110000')

def cksum(data):
    hash = ""
    i = 1

    while i < len(data):
        if data[i] == data[i-1]:
            hash += '1'
        else:
            hash += '0'
        i += 2

    return hash

assert(cksum('110010110100') == '110101')
assert(cksum('110101') == '100')

def solve(disk_size, initial_state):
    data = initial_state

    while len(data) < disk_size:
        data = next_iteration(data)

    hash =  cksum(data[:disk_size])

    while len(hash) % 2 == 0:
        hash = cksum(hash)

    return hash

assert(solve(20, '10000') == '01100')

disk_size = 272
initial_state = "10001001100000001"

print(solve(disk_size, initial_state))
# part 2

disk_size = 35651584
initial_state = "10001001100000001"

print(solve(disk_size, initial_state))
