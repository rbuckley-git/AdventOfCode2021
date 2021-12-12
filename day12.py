#!/usr/bin/python3
#
# https://adventofcode.com/
# 12/12/2021
#
# Day 12
#
# That took longer than it should have. Lots of interruptions from children along the way.
# Part 2 logic for can_we_enter_small_cave() took a while to think through. Not simple. Got the answer in the end.
#

import copy

test = False
day = 12

solutions = []

def is_cave_small( c ):
    if c == c.lower() and c not in ["end","start"]:
        return True
    return False

def can_we_enter_small_cave( path, cave ):
    # simple case, quick exit
    if cave not in path:
        return True

    # populate a map of occurences of each small cave
    d = {}
    for p in path:
        if is_cave_small( p ):
            if p in d:
                d[p]+=1
            else:
                d[p]=1
    
    for p in d.keys():
        if d[p] > 1:
            return False

    # if this cave has only been visited once then allow a second
    if d[cave] < 2:
        return True

    return False


def find_path_part1( s, path ):
    path.append(s)

    if s == "end":
        solutions.append( copy.deepcopy( path ) )
        return True

    if s not in map:
        return False

    for a in map[s]:
        if a != "start":
            if is_cave_small( a ):
                if a not in path:
                    if find_path_part1( a, copy.deepcopy( path ) ):
                        path.pop()
            else:
                if find_path_part1( a, path ):
                    path.pop()
            
    return False

def find_path_part2( s, path ):
    path.append(s)

    if s == "end":
        solutions.append( copy.deepcopy( path ) )
        return True

    if s not in map:
        return False

    for a in map[s]:
        if a != "start":
            if is_cave_small( a ):
                if can_we_enter_small_cave( path, a ):
                    if find_path_part2( a, copy.deepcopy( path ) ):
                        path.pop()
            else:
                if find_path_part2( a, path ):
                    path.pop()
            
    return False

if __name__ == '__main__':
    filename = str(day) + ".input."
    if test:
        filename += "test.txt"
    else:
        filename += "txt"

    map = {}
    with open( filename ) as fp:
        for line in fp:
            
            (l,r) = line[:-1].split("-")
            if l in map:
                map[l].append( r )
            else:
                map[l] = [r]

    map_copy = copy.deepcopy( map )

    # add a reverse map to make the logic easier later
    for s in map_copy:
        for a in map_copy[s]:
            if s != "start" and a != "end":
                if a in map:
                    map[a].append( s )
                else:
                    map[a] = [s]

    for start in map["start"]:
        find_path_part1(start,["start"])
        
    print("1.",len( solutions ))

    solutions = []
    for start in map["start"]:
        find_path_part2(start,["start"])
        
    print("2.",len( solutions ))
