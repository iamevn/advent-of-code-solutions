#!/usr/bin/env python3

from sys import argv,exit,setrecursionlimit

input_filename = "input"
if len(argv) > 1:
    input_filename = argv[1]

try:
    input = open(input_filename)
except OSError:
    exit("Cannot open file \"{}\"".format(input_filename))

bots = {}
outputs = {}
for line in input:
    if line[:5] == "value": # "value {} goes to bot {}"
        split_line = line.split()
        the_val = int(split_line[1])
        the_bot = int(split_line[5])
        if the_bot in bots:
            bots[the_bot]['has'].append(the_val)
        else:
            bots[the_bot] = {}
            bots[the_bot]['has'] = [the_val]
    else: # "bot {} gives low to {} {} and high to {} {}"
        split_line = line.split()
        the_bot = int(split_line[1])
        low_type = split_line[5]
        low_target = int(split_line[6])
        high_type = split_line[10]
        high_target = int(split_line[11])
        if not the_bot in bots:
            bots[the_bot] = {}
            bots[the_bot]['has'] = []
        bots[the_bot]['low'] = {}
        bots[the_bot]['low']['type'] = low_type
        bots[the_bot]['low']['target'] = low_target
        bots[the_bot]['high'] = {}
        bots[the_bot]['high']['type'] = high_type
        bots[the_bot]['high']['target'] = high_target


done = False

while not done:
    done = True #maybe
    for id in bots:
        bot = bots[id]
        if len(bot['has']) == 2:
            done = False
            if 61 in bot['has'] and 17 in bot['has']:
                # done = True
                print("bot {} compares 61 and 17".format(id))
            bot['has'].sort()
            # exit(0)
            if bot['low']['type'] == 'bot':
                bots[bot['low']['target']]['has'].append(bot['has'][0])
            if bot['low']['type'] == 'output':
                outputs[bot['low']['target']] = bot['has'][0]

            if (bot['high']['type'] == 'bot'):
                bots[bot['high']['target']]['has'].append(bot['has'][1])
            if (bot['high']['type'] == 'output'):
                outputs[bot['high']['target']] = bot['has'][1]
            bot['has'] = []

print(outputs[0] * outputs[1] * outputs[2])
