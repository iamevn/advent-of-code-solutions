#!/usr/bin/env python3.6

from sys import argv,exit

input_filename = "input"
the_string = "abcdefgh"
if len(argv) > 1:
    input_filename = argv[1]

try:
    input = open(input_filename)
except OSError:
    exit("Cannot open file \"{}\"".format(input_filename))

def make_node(x, y, size, used, avail, pct=None):
    x = int(x[1:])
    y = int(y[1:])
    size = int(size[:-1])
    used = int(used[:-1])
    avail = int(avail[:-1])
    pct = int(pct[:-1])
    return {'coord':(x, y), 'size':size, 'used':used, 'avail':avail, 'pct':pct}

all_nodes = []
for line in input:
    splitted = line.split()
    if splitted[0][:5] != '/dev/':
        # on one of the header lines
        continue
    coords = splitted[0].split('-')[1:]
# node = { 'coord':(x, y), 'size':_, 'used':_, 'avail':_, 'pct':_ }
    node = make_node(coords[0], coords[1], splitted[1], splitted[2], splitted[3], splitted[4])
    all_nodes.append(node)


def is_viable(A, B):
    # A not empty (used not 0)
    # A and B are not the same node
    # A's data would fit on B (A['used'] <= B['avail])
    return A['used'] != 0 and A['coord'] != B['coord'] and A['used']  <= B['avail']

def viable_pairs(node_table):
    viable_ct = 0
    for A in node_table:
        for B in node_table:
            if is_viable(A, B):
                viable_ct += 1
    return viable_ct

print("{} viable pairs".format(viable_pairs(all_nodes)))

# print out nodes in used/free grid (home in parens, goal in brackets)
# widest numbers are three wide
node_grid = {}
for node in all_nodes:
    node_grid[node['coord']] = node

home = (0, 0)
max_x = 0
max_y = 0
for coord in node_grid:
    if coord[0] > max_x:
        max_x = coord[0]
    if coord[1] > max_y:
        max_y = coord[1]

goal = (max_x, 0)
print(f"home: {home}, goal {goal}")

def sizes_grid():
    str = ""
    for y in range(max_y + 1):
        for x in range(max_x + 1):
            node = node_grid[(x, y)]
            u = node['used']
            s = node['size']
            str += f"{u:4}/{s:3} "
        str += '\n'
    return str
# print(sizes_grid())

# based on visual inspection of the data, all nodes I might need to move through are friendly to the only empty node: (4, 25)
the_empty_node = node_grid[(4, 25)]
print(f"empty spot is {the_empty_node['coord']}")
def simplify(node):
    if len(node) == 2:
        return simplify(sizes_grid[node])
    elif node['used'] == 0:
        return '_'
    elif node['used'] <= the_empty_node['avail']:
        return '.'
    elif node['used'] > the_empty_node['avail']:
        return '#'

def simplified_grid():
    str = ""
    for y in range(max_y + 1):
        for x in range(max_x + 1):
            symbol = simplify(node_grid[(x, y)])
            if (x, y) == goal:
                symbol = 'G'

            if (x, y) == (0, 0):
                symbol = f'({symbol})'
            else:
                symbol = f' {symbol} '
            str += symbol
        str += '\n'
    return str

print(simplified_grid())

print("28 moves to get empty to (1, 0)")
print("32 more to move empty to the (33, 0)")
print("5 to move G 1 to the left")
print("do that 32 times")
print(f"32 * 5 + 32 + 28 = {32 * 5 + 32 + 28}" )
print("")
period_count = 0
for c in simplified_grid():
    if c == '.' or c == 'G':
        period_count += 1
print(f"oh and a neat thing:\nthe amount of period spaces (counting goal) in the grid: {period_count}, which is the number of viable pairs")
