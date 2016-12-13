#!/usr/bin/env python3

from sys import argv,exit
from math import sqrt
from collections import defaultdict
import functools

input = 1364
target = (31, 39)
if len(argv) > 1:
    input = int(argv[1])

@functools.lru_cache()
def isWall(coord):
    x = coord[0]
    y = coord[1]
    if x < 0 or y < 0:
        return True #let's make negative coords walled off
    check = x*x + 3*x + 2*x*y + y + y*y
    check += input
    # count number of 1 bits in binary representaion of check.
    # even -> False
    # odd  -> True
    check = "{0:b}".format(check)
    count = 0
    for c in check:
        if c == '1':
            count += 1
    return count % 2 == 1

def heuristicLength(origin, destination):
    return sqrt( (destination[0] - origin[0]) ** 2\
               + (destination[1] - origin[1]) ** 2)
def neighbors(node):
    # return set of neighbors to a node that are not walls
    x = node[0]
    y = node[1]
    theSet = set()
    for i in {-1, 1}:
        if not isWall((x + i, y)):
            theSet.add((x + i, y))
    for j in {-1, 1}:
        if not isWall((x, y + j)):
            theSet.add((x, y + j))
    return theSet

# based on the wikipedia article on A*
def shortestPath(origin, destination):
    # evaluated spaces
    closedSet = set()
    # discovered nodes to be evaluated
    openSet = set()
    openSet.add(origin)
    # for each node, which node it can be most efficiently reached from 
    # will contain the most efficient previous step for each node in this set
    cameFrom = {}
    def walkPath(current):
        path = [current]
        while current != origin:
            current = cameFrom[current]
            path.append(current)
        path.reverse()
        return path

    # the cost of getting from start to a node
    gScore = defaultdict(lambda: float('inf'))
    gScore[origin] = 0

    # the cost of getting from start to end through a node
    # start to node is known, node to goal is by heuristic
    fScore = defaultdict(lambda: float('inf'))
    fScore[origin] = heuristicLength(origin, destination)

    while len(openSet) > 0:
        #node in openSet with lowest fScore
        current = None
        for node in openSet:
            if (not current) or (fScore[node] < fScore[current]):
                current = node
        if current == destination:
            return walkPath(current)

        openSet.remove(current)
        closedSet.add(current)
        # for each neighbor of current
        for neighbor in neighbors(current):
            if neighbor in closedSet:
                continue # neighbor is already evaluated
            tentative_gScore = gScore[current] + 1
            if not neighbor in openSet:
                openSet.add(neighbor)
            elif tentative_gScore >= gScore[neighbor]:
                continue # not a better path
            # on best path so far
            cameFrom[neighbor] = current
            gScore[neighbor] = tentative_gScore
            fScore[neighbor] = gScore[neighbor] + heuristicLength(neighbor, destination)
    return "FAILED TO FIND PATH"

path = shortestPath((1, 1), target)
print("")
print("             111111111122222222223333")
print("   0123456789012345678901234567890123")
for j in range(42):
    if (j < 10):
        print(j, end="  ")
    else:
        print(j, end=" ")
    for i in range(34):
        if isWall((i, j)):
            print("#", end="")
        elif (i, j) in path:
            print("o", end="")
        else:
            print(".", end="")
    print("")
print("")
print("Shortest path from {} to {}:".format((1, 1), target))
print(len(path) - 1)

# part 2
def walk(start, distance):
    reachable = {0:{start}}
    nodes = {start}
    for i in range(1, distance + 1):
        reachable[i] = set()
        for node in reachable[i - 1]:
            for neighbor in neighbors(node):
                if not neighbor in nodes:
                    reachable[i].add(neighbor)
                    nodes.add(neighbor)
    return nodes

reachable = walk((1, 1), 50)

print("")
print("             111111111122222")
print("   0123456789012345678901234")
for j in range(27):
    if (j < 10):
        print(j, end="  ")
    else:
        print(j, end=" ")
    for i in range(25):
        if isWall((i, j)):
            print("#", end="")
        elif (i, j) in reachable:
            print("o", end="")
        else:
            print(".", end="")
    print("")


print("")
print("Spaces reachable within 50 steps:")
print(len(reachable))
