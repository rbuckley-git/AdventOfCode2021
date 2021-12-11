#!/usr/bin/python3
#
# https://adventofcode.com/
# 11/12/2021
#
# Day 11
#
# For me, part 1 was much trickier than part 2. I was trying a recusive solution for a while until I decided
# to just do loops till no more changes. The samples were certainly required to get the logic right.
#

test = False
day = 11

def increment_adjoining_cells( grid, x, y ):
    for d in [ [0,-1], [0,1], [-1,0], [1,0], [-1,-1], [-1,1], [1,1], [1,-1] ]:
        xx = x + d[0]
        yy = y + d[1]
        if xx >= 0 and xx < len(grid[0]) and yy >=0 and yy < len( grid[0] ):
            grid[yy][xx] += 1

# to ease debugging
def print_grid( grid ):
    for y in range( len( grid ) ):
        print(grid[y])  
    print()

if __name__ == '__main__':
    filename = str(day) + ".input."
    if test:
        filename += "test.txt"
    else:
        filename += "txt"

    grid = []
    with open( filename ) as fp:
        for line in fp:
            l = []
            for c in line[:-1]:
                l.append( int(c) )
            grid.append( l )


    octopuses = len(grid) * len(grid[0])
    steps = 1
    flashes = 0
    complete = False

    while not complete:
        print("step",steps)

        visited = set()

        # increase all cell values by 1
        for y in range( len(grid) ):
            for x in range( len(grid[0]) ):
                grid[y][x] += 1

        # ripple the increments over adjoining cells until no more changes
        done = False
        while not done:
            changes = 0
            for y in range( len(grid) ):
                for x in range( len(grid[0]) ):
                    if grid[y][x] > 9 and (x,y) not in visited:
                        # flash cell so add to map to avoid next time
                        visited.add( (x,y) )
                        increment_adjoining_cells( grid, x, y )
                        changes+=1

            if changes == 0:
                done = True

        # the number of flashes will be the same as the number of entries in our map
        flashes += len( visited )

        # finally reset flashed cells to 0
        for y in range( len(grid) ):
            for x in range( len(grid[0]) ):
                if grid[y][x] > 9:
                    grid[y][x] = 0

        if steps == 100:
            print_grid( grid )
            print("1.",flashes)

        if len(visited) == octopuses:
            print_grid( grid )
            print("2.",steps)
            complete = True

        steps+=1
