#!/usr/bin/env python3

from hashlib import md5
import functools

input = b"ahsbgdzn"
# test 
# should result in 22728 and 22551
# input = b"abc"

@functools.lru_cache(maxsize=1000)
def genHash(index):
    return md5(input + str(index).encode()).hexdigest()

@functools.lru_cache(maxsize=1000)
def checkReps(hash):
    for i in range(2, len(hash)):
        c = hash[i]
        if hash[i - 1] == c and hash[i - 2] == c:
            return c
    return False

def isKey(index, hash_fn = genHash):
    hash = hash_fn(index)

    c = checkReps(hash)
    if c:
        for i in range(1, 1001):
            if "{0}{0}{0}{0}{0}".format(c) in hash_fn(index + i):
                return True
    return False

def find64th(hash_fn=genHash):
    i = -1
    found_count = 0
    while found_count < 64:
        i += 1
        if isKey(i, hash_fn):
            found_count += 1
            # this is silly but I like it
            print("found key number {} at {}".format(found_count, i), end="\r")
    print("")
    return i

i = find64th(genHash)
print(genHash(i))
print("")

# part 2

@functools.lru_cache(maxsize=1000)
def stretch(hash):
    for i in range(2016):
        hash = md5(hash.encode()).hexdigest()
    return hash

i = find64th(lambda i: stretch(genHash(i)))
print(stretch(genHash(i)))
