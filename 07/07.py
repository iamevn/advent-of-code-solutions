#!/usr/bin/env python3

from sys import argv, exit

input_filename = "input"
if len(argv) > 1:
    input_filename = argv[1]

try:
    input = open(input_filename)
except OSError:
    exit(f'Cannot open file "{input_filename}"')

input = [line for line in input]

def findroot(descr):
    nodes = set()
    children = set()
    for line in descr:
        ids = line.split()
        nodes.add(ids[0])
        if len(ids) > 2:
            [children.add(node.strip(",")) for node in ids[3:]]
    root = nodes - children
    return root.pop()

testinput ="""pbga (66)
xhth (57)
ebii (61)
havc (66)
ktlj (57)
fwft (72) -> ktlj, cntj, xhth
qoyq (66)
padx (45) -> pbga, havc, qoyq
tknk (41) -> ugml, padx, fwft
jptl (61)
ugml (68) -> gyxo, ebii, jptl
gyxo (61)
cntj (57)""".split("\n")

assert findroot(testinput) == "tknk"

print(findroot(input))


def buildandfixtree(descr):
    class Node():
        def __init__(self, id, weight, children=[]):
            "string args for id and weight, list of strings for children"
            self.id = id
            self.weight = int(weight[1:-1])
            self.children = children
            self.totalweight = None

        def fixchildren(self, tree):
            self.children = [tree[cid] for cid in self.children]

        def fillweight(self):
            self.totalweight = self.weight + sum([child.fillweight() for child in self.children])
            return self.totalweight

    tree = {}
    for line in descr:
        ids = [foo.strip(",") for foo in line.split()]
        if len(ids) > 3:
            tree[ids[0]] = Node(ids[0], ids[1], ids[3:])
        else:
            tree[ids[0]] = Node(ids[0], ids[1])

    def findroot(tree):
        nodes = set()
        children = set()
        for node in tree.values():
            nodes.add(node.id)
            for child in node.children:
                children.add(child.id)
        root = nodes - children
        return tree[root.pop()]

    for node in tree.values():
        node.fixchildren(tree)

    root = findroot(tree)
    root.fillweight()

    # find unbalanced part
    # start at root and follow unbalanced branch until one is balanced
    checkqueue = [root] # should be highest level unbalanced node
    foundunbalance = False
    wfound = None
    wdesired = None
    cfound = None
    while len(checkqueue) > 0:
        check = checkqueue.pop()
        childWeights = {child: child.totalweight for child in check.children}
        weightCounts = {}
        for c in childWeights:
            w = childWeights[c]
            if w in weightCounts:
                weightCounts[w] += 1
            else:
                weightCounts[w] = 1
        if len(weightCounts) > 1:
            foundunbalance = True
            # unbalanced
            # find weight with 1 count
            for w in weightCounts:
                c = weightCounts[w]
                if c == 1:
                    wfound = w
                else:
                    wdesired = w

            for child in childWeights:
                if child.totalweight == wfound:
                    # ia m bvery tired
                    cfound = child
            checkqueue.append(cfound)
        elif foundunbalance:
            break
        else:
            # really shouldn't be here
            # uhhh
            panic()
            # yeah
            [checkqueue.append(child) for child in check.children]
    return cfound.weight + (wdesired - wfound)


assert buildandfixtree(testinput) == 60

print(buildandfixtree(input))
