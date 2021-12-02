#!/usr/bin/python3
#
# https://adventofcode.com/
# 2/12/2021
#
# Day 2
#
# Simple.
#

if __name__ == '__main__':
    instructions = []
    with open( '2.input.txt' ) as fp:
        for line in fp:
            (action,x) = line.split(" ")
            instructions.append( [ action,int(x) ] )

    depth = 0
    horizontal = 0

    for instruction in instructions:
        if instruction[0] == "forward":
            horizontal += instruction[1]
        elif instruction[0] == "down":
            depth += instruction[1]
        elif instruction[0] == "up":
            depth -= instruction[1]

    print("1. ",depth * horizontal)

    depth = 0
    horizontal = 0
    aim = 0

    for instruction in instructions:
        if instruction[0] == "forward":
            horizontal += instruction[1]
            depth += instruction[1] * aim
        elif instruction[0] == "down":
            aim += instruction[1]
        elif instruction[0] == "up":
            aim -= instruction[1]

    print("2. ",depth * horizontal)

