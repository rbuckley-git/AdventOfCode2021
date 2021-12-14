#!/usr/bin/python3
#
# https://adventofcode.com/
# 14/12/2021
#
# Day 14
#
# Part 1 was easy but given up (for now) on part 2.
#

import copy
from collections import Counter

test = False
day = 14

max_x = 0
max_y = 0

def expand_seed( seed ):
    tree = {}
    done = False
    i = 0
    while not done:
        pair = seed[i:i+2]
        if pair in rules:
            tree[pair] = pair[0] + rules[pair] + pair[1]
        i+=1

        if i >= len(seed) - 1   :
            done = True

    return tree

if __name__ == '__main__':
    filename = str(day) + ".input."
    if test:
        filename += "test.txt"
    else:
        filename += "txt"

    rules = {}
    seed = None
    with open( filename ) as fp:
        for line in fp:
            line = line[:-1]
            if seed == None:
                seed = line
            elif line != "":
                (a,b) = line.split(" -> ")
                rules[a] = b

    original_seed = seed

    for loop in range(10):
        done = False
        i = 0
        while not done:
            pair = seed[i:i+2]
            if pair in rules:
                pair = pair[0] + rules[pair] + pair[1]
                seed = seed[0:i] + pair + seed[i+2:]
                i+=1
            i+=1

            if i >= len(seed) - 1   :
                done = True

    freq = {}
    for c in seed:
        if c in freq:
            freq[c] += 1
        else:
            freq[c] = 1
    ordered = Counter(freq).most_common()
    print("1.",ordered[0][1]-ordered[len(ordered)-1][1])

