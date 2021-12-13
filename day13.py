#!/usr/bin/python3
#
# https://adventofcode.com/
# 13/12/2021
#
# Day 13
#
# That was fun. Part 1 was easy as it just involved one fold x. Unfornately for me, part 2 took a little longer
# as I had a indexing error in the y which took a short while to fine. I enjoyed it as it is so obvious then
# the answer pops out looking right.
#

import copy

test = False
day = 13

max_x = 0
max_y = 0

def draw_dots( dots ):
    for y in range( max_y ):
        line = ""
        for x in range( max_x ):
            if (x,y) in dots:
                line += "#"
            else:
                line += " "
        print( line )
    print()

def fold_up(dots, y_fold):
    folded_dots = set()
    n = 1
    for y in range( y_fold-1,-1,-1 ):
        yy = y_fold + n
        for x in range( max_x ):
            if (x,y) in dots:
                folded_dots.add((x,y))
            if (x,yy) in dots:
                folded_dots.add((x,y))
        n+=1
    return folded_dots

def fold_left(dots, x_fold):
    folded_dots = set()
    for y in range(max_y):
        for x in range( x_fold-1,-1,-1 ):
            xx = max_x - x - 1
            if (x,y) in dots:
                folded_dots.add((x,y))
            if (xx,y) in dots:
                folded_dots.add((x,y))
    return folded_dots

if __name__ == '__main__':
    filename = str(day) + ".input."
    if test:
        filename += "test.txt"
    else:
        filename += "txt"

    dots = set()
    folds = []
    with open( filename ) as fp:
        for line in fp:
            line = line[:-1]
            if len(line) > 0:
                if line.startswith("fold along"):
                    line = line.replace("fold along ","")
                    (d,n) = line.split("=")
                    folds.append( (d,int(n)) )
                else:
                    (xx,yy) = line.split(",")
                    x = int(xx)
                    y = int(yy)
                    if x > max_x:
                        max_x = x
                    if y > max_y:
                        max_y = y
                    dots.add((x,y))
    max_x += 1
    max_y += 1

    n = 0
    for fold in folds:
        if fold[0] == "x":
            dots = fold_left( dots, fold[1] )
            max_x = fold[1]
        else:
            dots = fold_up(dots,fold[1])
            max_y = fold[1]
        if n == 0:
            print("1.",len(dots))
            n+=1
    print("2.")
    draw_dots( dots )
