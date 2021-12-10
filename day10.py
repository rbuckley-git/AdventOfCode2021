#!/usr/bin/python3
#
# https://adventofcode.com/
# 10/12/2021
#
# Day 10
#
# Nice easy one for a Friday. I had chosen a stack of required closing characters for my initial 
# implementation which meant part 2 was simply a case of reversing the stack and doing the little
# score logic. Enjoyed that one.
#

test = False
day = 10
chunk_delimiters = [ ("[","]"),("<",">"),("{","}"),("(",")")]
part1_points = { ")": 3, "]": 57, "}": 1197, ">": 25137 }
part2_points = { ")": 1, "]": 2, "}": 3, ">": 4 }

def find_close_delimiter( c ):
    for cd in chunk_delimiters:
        if c == cd[0]:
            return cd[1]
    return None

def is_open( c ):
    for cd in chunk_delimiters:
        if c == cd[0]:
            return True
    return False


def invalid_line_score( line ):
    stack = []
    for c in line:
        cd = find_close_delimiter( c )
        if is_open( c ):
            stack.append( cd )
        else:
            if stack[-1] != c:
                return part1_points[c]
            stack.pop()
    return 0

def completion_sequence( line ):
    stack = []
    for c in line:
        cd = find_close_delimiter( c )
        if is_open( c ):
            stack.append( cd )
        else:
            stack.pop()

    return reversed(stack)

if __name__ == '__main__':
    filename = str(day) + ".input."
    if test:
        filename += "test.txt"
    else:
        filename += "txt"

    lines = []
    with open( filename ) as fp:
        for line in fp:
            lines.append( line[:-1] )

    score = 0
    valid_lines = []
    for line in lines:
        s = invalid_line_score( line )
        if s == 0:
            valid_lines.append( line )
        score += s
    print("1.",score)

    scores = []
    for line in valid_lines:
        completion = completion_sequence( line )
        score = 0
        for c in completion:
            score *= 5
            score += part2_points[c]
        scores.append( score )
    scores = sorted( scores )

    print("2.",scores[int(len(scores)/2)])
