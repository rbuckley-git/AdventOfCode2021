#!/usr/bin/python3
#
# https://adventofcode.com/
# 6/12/2021
#
# Day 6
#
# Part 1 was a quick implementation in a brute force style.
# Part 2 required some rework as it was clear a brute force was not going to complete in a hurry. Pivoted to an
# array of days. Shift the array to the left and pick up the zeroth element for a new fish and recycling.
# Quite pleased with the final solution which also works for part 1. My final answer was 1605400130036.
#

import re

def calc_sum( fish ):
    sum = 0
    for d in days_fish:
        sum += d
    return sum

if __name__ == '__main__':
    lf = []
    with open( '6.input.txt' ) as fp:
        line = fp.readline()
        for d in line.strip().split(","):
            lf.append(int(d))
    
    # pivot input into array of days with number of fish at a specific age as a number
    # in the array element for that day
    days_fish = [0 for i in range(9) ]
    for d in lf:
        days_fish[ d ] += 1

    for day in range(256):
        # take a copy of the zeroth element for use later
        hatching = days_fish[0]
        # shift the array to the left to decrement all fish ages
        days_fish = days_fish[1:]
        # add in the last element following the shift
        days_fish.append(0)
        # take the zeroth element values and allow new fish to flourish
        days_fish[6] += hatching
        days_fish[8] += hatching

    print("A. ",calc_sum(days_fish))