#!/usr/bin/env python3

from sys import argv, exit
from collections import defaultdict

input_filename = "input"
if len(argv) > 1:
    input_filename = argv[1]

try:
    input = open(input_filename)
except OSError:
    exit(f'Cannot open file "{input_filename}"')

input = [line for line in input]

# 16 bit ops (unsigned)
def NOT(a):
    return 65535 - a
def AND(a, b):
    return a & b
def OR(a, b):
    return a | b
def LSHIFT(a, b):
    return (a * (2 ** b)) & 65535
def RSHIFT(a, b):
    return a // (2 ** b)

class wire():
    def __init__(self, line, wireset):
        split = line.split()
        self.id = split[-1]
        self.expr = split[:-2]
        self.value = None
        self.wireset = wireset

    # self.expr is an {expression}
    # expression is one of the following:
    # - {number}
    # - {wire id}
    # - {unary op} {expression}
    # - {expression} {binary op} {expression}
    # unary op is
    # - NOT
    # binary op is
    # - AND
    # - OR
    # - LSHIFT
    # - RSHIFT

    def get(self, token):
        if token.isdigit():
            return int(token)
        else:
            return self.wireset[token].eval()

    def eval(self):
        expr = self.expr
        if self.value is None:
            if len(expr) == 1:
                self.value = self.get(expr[0])
            elif len(expr) == 2:
                self.value = NOT(self.get(expr[1]))
            else:
                self.value = {'AND': AND, 'OR': OR, 'LSHIFT': LSHIFT, 'RSHIFT': RSHIFT}[expr[1]](self.get(expr[0]), self.get(expr[2]))
        return self.value


def run(program, ivals = {}):
    wireset = {}
    for line in program:
        tmp = wire(line, wireset)
        wireset[tmp.id] = tmp
        if tmp.id in ivals:
            tmp.value = ivals[tmp.id]

    return {id: wireset[id].eval() for id in wireset}

testinput = ["123 -> x", "456 -> y", "x AND y -> d", "x OR y -> e", "x LSHIFT 2 -> f", "y RSHIFT 2 -> g", "NOT x -> h", "NOT y -> i"]
assert run(testinput) == {'d': 72, 'e': 507, 'f': 492, 'g': 114, 'h': 65412, 'i': 65079, 'x': 123, 'y': 456}

print(run(input)['a'])

print(run(input, {'b': run(input)['a']})['a'])
