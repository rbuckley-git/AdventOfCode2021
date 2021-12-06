#!/usr/bin/python3
#
# https://adventofcode.com/
# 5/12/2021
#
# Day 5
#
# Part 1 was simple.
# Part 2 required a little thinking to make sure the diagonals ran the right length. As is typical in these
# puzzles, it is the format used to represent the data that is quite interesting. I chose a map keyed on 
# coordinate. This allows a coordinate to be found and incremented when drawing a line. 
# Plotting the grid in ascii art only useful for test data.
#

import re

def get_key( x, y ):
    return str(x) + "-" + str(y)

def plot_grid( grid, max_x, max_y ):
    for y in range(0,max_y + 1):
        line = ""
        for x in range(0,max_x + 1):
            key = get_key( x, y )
            if key not in grid:
                line = line + "."
            else:
                line = line + str(grid[key])

        print(line)

if __name__ == '__main__':
    grid = {}
    max_x = 0
    max_y = 0
    with open( '5.input.txt' ) as fp:
        for line in fp:
            line = line[:-1]
            (a,b) = line.split( " -> " )
            (x1,y1) = a.split(",")
            (x2,y2) = b.split(",")

            x1 = int(x1)
            x2 = int(x2)
            y1 = int(y1)
            y2 = int(y2)

            if x1 > max_x:
                max_x = x1
            if x2 > max_x:
                max_x = x2
            if y1 > max_y:
                max_y = y1
            if y2 > max_y:
                max_y = y2

            if (x1 == x2) or (y1 == y2):
                if x1 > x2:
                    d = x2
                    x2 = x1
                    x1 = d
                if y1 > y2:
                    d = y2
                    y2 = y1
                    y1 = d

                for x in range( x1,x2+1 ):
                    for y in range( y1,y2+1 ):
                        key = get_key( x, y )
                        if key in grid:
                            grid[key] += 1
                        else:
                            grid[key] = 1
            else:
                xi = 1
                yi = 1
                if x1 > x2:
                    xi = -1
                if y1 > y2:
                    yi = -1
                y = y1
                for x in range( x1,x2+xi, xi ):
                    key = get_key( x, y )
                    if key in grid:
                        grid[key] += 1
                    else:
                        grid[key] = 1
                    y += yi
                

    #plot_grid( grid, max_x, max_y )

    count = 0
    for g in grid:
        if grid[g] >= 2:
            count+=1

    print(count)
