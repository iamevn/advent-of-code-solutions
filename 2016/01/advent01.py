#!/usr/bin/env python3
from sys import argv,exit

input_filename = "input"
if len(argv) > 1:
    input_filename = argv[1]

try:
    directions = open(input_filename)
except OSError:
    exit("Cannot open file \"{}\"".format(input_filename))

pos = {'x':0, 'y':0, 'heading':'N'}

for line in directions:
    for token in line.split(', '):
        dir = token[0]
        dist = int(token[1:])

        if dir == 'L':
            pos['heading'] = {'N':'W', 'E':'N', 'S':'E', 'W':'S'}[pos['heading']]
        else:
            pos['heading'] = {'N':'E', 'E':'S', 'S':'W', 'W':'N'}[pos['heading']]
            
        if pos['heading'] == 'N':
            pos['y'] -= dist
        elif pos['heading'] == 'S':
            pos['y'] += dist
        elif pos['heading'] == 'E':
            pos['x'] += dist
        elif pos['heading'] == 'W':
            pos['x'] -= dist

print("These directions take you {} blocks away from here!".format(abs(pos['x']) + abs(pos['y'])))


# part 2
directions.seek(0)

pos = {'x':0, 'y':0, 'heading':'N'}
visited = {}
visited[(0,0)] = True

for line in directions:
    for token in line.split(', '):
        dir = token[0]
        dist = int(token[1:])

        if dir == 'L':
            pos['heading'] = {'N':'W', 'E':'N', 'S':'E', 'W':'S'}[pos['heading']]
        else:
            pos['heading'] = {'N':'E', 'E':'S', 'S':'W', 'W':'N'}[pos['heading']]
        
        for i in range(dist):
            if pos['heading'] == 'N':
                pos['y'] -= 1
            elif pos['heading'] == 'S':
                pos['y'] += 1
            elif pos['heading'] == 'E':
                pos['x'] += 1
            elif pos['heading'] == 'W':
                pos['x'] -= 1

            current_pos = (pos['x'], pos['y'])

            if current_pos in visited:
                print("It looks like HQ is {} blocks away".format(abs(pos['x']) + abs(pos['y'])))
                exit()
            else:
                visited[current_pos] = True

print("I'm really lost")
