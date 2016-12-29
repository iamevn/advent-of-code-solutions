#!/usr/bin/env python3.6

from sys import argv,exit,stdin,stdout

def getch():
    import tty, termios
    fd = stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(stdin.fileno())
        ch = stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

input_filename = "input"
if len(argv) > 1:
    input_filename = argv[1]

try:
    input = open(input_filename)
except OSError:
    exit("Cannot open file \"{}\"".format(input_filename))

board = {'elevator':1, 'microchip':{}, 'generator':{}}
elements = []

for line in input:
    split = line.split(',')
    # slice out the floor name from the rest
    preamble = split[0][:split[0].find(" a ")] # the first floor contains
    split[0] = split[0][split[0].find(" a "):] #  a ____ _____
    split[-1] = split[-1][:-2] # remove period
    # set floor up to be a number based on name
    floor = preamble.split()[1]
    if floor == 'first':
        floor = 1
    elif floor == 'second':
        floor = 2
    elif floor == 'third':
        floor = 3
    elif floor == 'fourth':
        floor = 4

    if len(preamble.split()) == 6:
        #nothing on this floor
        # print(f"nothing on floor {floor}")
        continue
    # else
    if len(split) == 1:
        split = split[0].split(" and")

    for obj in split:
        # print(obj)
        elem = obj.split()[-2]
        type = obj.split()[-1]
        if type == 'microchip':
            elem = elem.split('-')[0]
        if not elem in elements:
            elements.append(elem)
        board[type][elem] = floor



def playAroundWithTermStuff():
    i = 0
    print("\0337", end="")
    stdout.flush()
    while getch():
        if i % 3 == 0:
            print("\0338\033[2Khello " + str(i))
        else:
            print("\033[2Khello " + str(i))
        i += 1

        if i == 100:
            print("\n\n\n\n")
            return

print("\0337", end="\n\n\n\n")
stdout.flush()

def printBoard(board, convert=0):
    if convert > 0:
        board = int2ints(board)
        convert -= 1
    if convert > 0:
        board = ints2board(board)
        convert -= 1

    print("\0338", end="")
    stdout.flush()
    for f in [4,3,2,1]:
        # print the floor
        print(f"F{f} ", end = "")
        if board["elevator"] == f:
            print("E  ", end = "")
        else:
            print(".  ", end = "")
        for e in elements:
            if board['generator'][e] == f:
                print(e[0], end = "G ")
            else:
                print(".  ", end = "")
            if board['microchip'][e] == f:
                print(e[0], end = "M ")
            else:
                print(".  ", end = "")
        print("")

printBoard(board)
print(elements)

# helper functions
def board2ints(board):
    digits = [board['elevator']]
    for e in elements:
        digits.append(board['generator'][e])
        digits.append(board['microchip'][e])
    return digits

def ints2board(digits):
    board = {'elevator':digits[0], 'microchip':{}, 'generator':{}}
    for i in range(1, len(digits)):
        if i % 2 == 0:
            board['microchip'][elements[(i-1)//2]] = digits[i]
        else:
            board['generator'][elements[(i-1)//2]] = digits[i]
    return board

# could use base 4 but base 5 makes keeping the width consistent easy
def ints2int(ints):
    num = 0
    pow = 0
    for d in ints:
        num += (5 ** pow) * d
        pow += 1
    return num

def int2ints(i):
    digits = []
    while i > 0:
        digits.append(i % 5)
        i //= 5
    return digits
    
def board2int(board):
    return ints2int(board2ints(board))

def int2board(i):
    return ints2board(int2ints(i))

# the pathfinding stuff, mostly uses the base 5 integer representation internally

def heuristicLength(origin, destination):
    origin = int2ints(origin)
    destination = int2ints(destination)

    distance = 0
    for i in range(len(destination)):
        distance += abs(destination[i] - origin[i])

    return distance

def neighbors(state):
    # return set of neighboring states that are valid
    pass

from collections import defaultdict
# based on the wikipedia article on A* (adapted from advent13.py)
def shortestPath(origin, destination):
    # evaluated states
    closedSet = set()
    # discovered states yet to be evaluated
    openSet = set()
    openSet.add(origin)
    # probably don't need cameFrom or walkPath

    # the cost of getting from start to a state
    gScore = defaultdict(lambda: float('inf'))
    gScore[origin] = 0

    # the cost of getting from start to end through a state
    # start to state is known, state to goal is by heuristic
    fScore = defaultdict(lambda: float('inf'))
    fScore[origin] = heuristicLength(origin, destination)

    while len(openSet) > 0:
        # state in openSet with lowest fScore
        current = None
        for state in openSet:
            if (not current) or (fScore[state] < fScore[current]):
                current = state
        if current == destination:
            return gScore[current]

        openSet.remove(current)
        closedSet.add(current)

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
    return False # FAILED TO FIND PATH, shouldn't happen


# the goal is all 4s for each slot in my base 5 representation
goal = (5 ** len(board2ints(board))) - 1

print(shortestPath(board2int(board), goal))
