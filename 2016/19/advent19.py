#!/usr/bin/env python3
def part1(input):
    hasPresents = []
    #initial population
    for i in range(1, input + 1):
        hasPresents.append(i)

    # remove every other elf until there's only one elf
    while len(hasPresents) > 1:
        nextRound = []
        if len(hasPresents) % 2 == 0:
            for i in range(0, len(hasPresents), 2):
                nextRound.append(hasPresents[i])
        else:
            for i in range(2, len(hasPresents), 2):
                nextRound.append(hasPresents[i])
        hasPresents = nextRound

    return hasPresents[0]

assert part1(1) == 1
assert part1(2) == 1
assert part1(3) == 3
assert part1(4) == 1
assert part1(5) == 3
assert part1(6) == 5

print(part1(3018458))

from math import floor
def part2(input, doprint=False):
    hasPresents = []
    def across(elfindex, circle):
        circlesize = len(circle)
        return (elfindex + floor(circlesize / 2)) % circlesize


    #initial population
    for i in range(1, input + 1):
        hasPresents.append(i)
    assert len(hasPresents) == input

    i = 0
    while len(hasPresents) > 1:
        if doprint:
            if len(hasPresents) % 100 == 0:
                print("elves left: {}".format(len(hasPresents)), end="\r")
        toRemove = across(i, hasPresents)

        del hasPresents[toRemove]
        if toRemove > i:
            i += 1
        i %= len(hasPresents)

    if doprint:
        print("")
    return hasPresents[0]
    
assert part2(1) == 1
assert part2(2) == 1
assert part2(5) == 2
assert part2(22) == 17
assert part2(55) == 29

print(part2(3018458, doprint=True))
