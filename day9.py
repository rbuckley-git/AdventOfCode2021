#!/usr/bin/python3
#
# https://adventofcode.com/
# 9/12/2021
#
# Day 9
#
# Nice little recurrsive puzzle. Knackered this evening so happy for a quick one.
#

# shorthand for up, down, left right - the four relative positions to move about
udlr = [ [0,-1], [0,1], [-1,0], [1,0] ]

# need to keep track of where we have been so we don't repeat visit
visited = set()

def is_local_min( grid, x, y ):
    for d in udlr:
        xx = x + d[0]
        yy = y + d[1]
        # are we still in the grid
        if xx >= 0 and xx < len( grid[y] ) and yy >= 0 and yy < len( grid ):
            if grid[y][x] >= grid[yy][xx]:
                return False
    return True

def find_basin_size( grid, x, y ):
    if (x,y) in visited:
        return 0

    size = 0
    # are we still in the grid
    if y >= 0 and y < len( grid ) and x >= 0 and x < len( grid[y] ):    
        if grid[y][x] != 9:
            # count this grid cell
            size += 1
            # now recurse for each point around this cell
            for d in udlr:
                visited.add( (x, y) )
                size += find_basin_size( grid, x + d[0], y + d[1] )
            return size
    return 0

if __name__ == '__main__':
   
    grid = []
    with open( '9.input.txt' ) as fp:
        for line in fp:
            line = line[:-1]
            row = []
            for c in line:
                row.append( int(c) )
            grid.append( row )

    mins = []
    for y in range( len( grid ) ):
        for x in range( len( grid[y] ) ):
            if is_local_min( grid, x, y):
                mins.append( grid[y][x] )

    print("1.",sum(mins) + len(mins))

    min_locs = []
    for y in range( len( grid ) ):
        for x in range( len( grid[y] ) ):
            if is_local_min( grid, x, y):
                min_locs.append( (x,y) )

    basin_sizes = []
    for loc in min_locs:
        basin_sizes.append(find_basin_size( grid, loc[0], loc[1] ))

    # need 3 largest so sort decending and slice of three
    basin_sizes = sorted( basin_sizes,reverse=True )[1:3]

    # answer is the product of the 3 largest basins
    result = 1
    for r in basin_sizes:
        result *= r

    print("2.",result )
    