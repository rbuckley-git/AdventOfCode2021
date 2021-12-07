#!/usr/bin/python3
#
# https://adventofcode.com/
# 7/12/2021
#
# Day 7
#
# Nice little puzzle, very similar to day 6 with a part 2 that needed a different optimisation to solve.
# Had to put youngest child in bath mid way through challenge which meant I lost a train of thought.
# Only getting evening time on AoC at present and it is only getting tougher.
#

# optimisation for part 2. Precalculate the fuel cost from each position and store in an array
# indexed by hops.
def calc_fuel_map( m ):
    fuel_map = [ 0 for i in range( m + 1) ]
    for p in range( len( fuel_map ) ):
        fuel = 0
        for y in range( 1, p + 1 ):
            fuel += y
        fuel_map[ p ] = fuel
    return fuel_map

def solve( part, pos ):
    # optimal position will be between 0 and max
    max_pos = max( pos )

    fuel_map = None
    if part == 2:
        fuel_map = calc_fuel_map( max_pos )

    # initialise array to hold calculated fuel values
    fuels = [ 0 for i in range( max_pos+1) ]
    for i in range( len( fuels ) ):
        for p in pos:
            if part == 1:
                fuels[ i ] += abs(p - i)
            else:
                fuels[ i ] += fuel_map[ abs(p - i) ]

    # get a starting point for finding lowest value
    min_fuel = max( fuels )

    # find lowest fuel value
    for i in range( len( fuels ) ):
        if fuels[ i ] < min_fuel:
            min_fuel = fuels[ i ]

    return min_fuel

if __name__ == '__main__':
    pos = []
    with open( '7.input.txt' ) as fp:
        line = fp.readline()
        for d in line.strip().split(","):
            pos.append(int(d))

    print("1.",solve(1,pos))
    print("2.",solve(2,pos))