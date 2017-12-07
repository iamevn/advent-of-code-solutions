#!/usr/bin/env python3.6

from sys import argv,exit
from math import sqrt
from collections import defaultdict

input_filename = "input"
if len(argv) > 1:
    input_filename = argv[1]

try:
    input = open(input_filename)
except OSError:
    exit("Cannot open file \"{}\"".format(input_filename))

map = {}
goals = {}
# read map into board thing
y = 0
for line in input:
    x = 0
    for c in line:
        if c == '\n':
            continue
        elif c == '.' or c == '#':
            pass
        else:
            goals[int(c)] = (x,y)
            c = '.'
        map[(x,y)] = c
        x += 1
    y += 1

print(f"goals: {goals}")
max_x = 0
max_y = 0
for coord in map:
    if coord[0] > max_x:
        max_x = coord[0]
    if coord[1] > max_y:
        max_y = coord[1]
print(f"max (x, y): ({max_x}, {max_y})")


def isWall(coord):
    if coord in map:
        return map[coord] == '#'
    else:
        return True

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

# based on the wikipedia article on A* (adapted from advent13.py)
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
    return False #FAILED TO FIND PATH

# find shortest paths between each pair of locations to form a graph.
# this graph's paths may pass through other locations. for use with rough guess
path_graph = {}
# (if shortest path between A and B travels through another location,
# then A and B are not connected on this graph)
filtered_graph = {}
# filtered_graph looks something like (from example)
# {
#   0: {1: 2, 4: 2},
#   1: {0: 2, 2: 6},
#   2: {1: 6, 3: 2},
#   4: {0: 2, 3: 8},
#   3: {2: 2, 4: 8}
# }
def noGoalsAlong(path):
    for node in path[1:-1]:
        if node in goals.values():
            return False
    return True
for A in goals:
    path_graph[A] = {}
    filtered_graph[A] = {}
    for B in goals:
        if A != B:
            found = shortestPath(goals[A], goals[B])
            if found:
                path_graph[A][B] = len(found) - 1
                if noGoalsAlong(found):
                    filtered_graph[A][B] = len(found) - 1
for orig in path_graph:
    print(f"{orig}: {path_graph[orig]}")

# find smallest path through this graph

# length of path from 0 to 1, 1 to 2, 2 to 3, etc
upper_bound = 0
for i in range(len(goals) - 1):
    upper_bound += path_graph[i][i+1]

print(f"upper bound on path length: {upper_bound}")

location = 0
nodesToDiscover = set(goals.keys())
nodesToDiscover.remove(0)

def softRemove(s, rem):
    tmp = set()
    for key in s:
        if key != rem:
            tmp.add(key)
    return tmp
# recursively search
def travel(location=0, steps=0, nodesLeft=nodesToDiscover, bestSoFar=upper_bound):
    attempt = None
    if len(nodesLeft) == 0:
        return steps
    if steps > bestSoFar:
        return upper_bound + 1
    for neighbor in filtered_graph[location]:
        dist = filtered_graph[location][neighbor]
        attempt = travel(neighbor, dist + steps, softRemove(nodesLeft, neighbor), bestSoFar)
        if attempt < bestSoFar:
            bestSoFar = attempt
            print(f"best so far: {bestSoFar}", end="          \r")
    return bestSoFar
print(f"\nPart 1: {travel()}")


# part 2
# return to 0 again
# length of path from 0 to 1, 1 to 2, 2 to 3, ..., n-1 to n, n to 0
upper_bound = 0
for i in range(len(goals) - 1):
    upper_bound += path_graph[i][i+1]

upper_bound += path_graph[len(path_graph) - 1][0]

print(f"upper bound on path length: {upper_bound}")

location = 0
nodesToDiscover = set(goals.keys())
nodesToDiscover.remove(0)
# recursively search
def travel2(location=0, steps=0, nodesLeft=nodesToDiscover, bestSoFar=upper_bound):
    attempt = None
    if len(nodesLeft) == 0 and location == 0:
        return steps
    if steps > bestSoFar:
        return upper_bound + 1
    for neighbor in filtered_graph[location]:
        dist = filtered_graph[location][neighbor]
        attempt = travel2(neighbor, dist + steps, softRemove(nodesLeft, neighbor), bestSoFar)
        if attempt < bestSoFar:
            bestSoFar = attempt
            print(f"best so far: {bestSoFar}", end="      \r")
    return bestSoFar

print(f"\nPart 2: {travel2()}")
