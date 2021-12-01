#!/usr/bin/python3
#
# https://adventofcode.com/
# 1/12/2021
#
# Day 1
#
# Straightforward challenge. Out all day so doing it on my return.
#

if __name__ == '__main__':
    depths = []
    with open( '1.input.txt' ) as fp:
        for line in fp:
            depths.append( int( line[:-1] ) )


    increments = 0
    n = 0
    prev = 0
    for depth in depths:
        if n > 0 and depth > prev:
            increments+=1
        prev = depth
        n+=1

    print( "1. increments: ", increments )

    increments = 0
    prev = -1
    for i in range( 2, len( depths ) ):
        sum = depths[i-2] + depths[i-1] + depths[i]
        if prev > -1 and sum > prev:
            increments+=1
        prev = sum

    print( "2. increments: ", increments )

