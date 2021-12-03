#!/usr/bin/python3
#
# https://adventofcode.com/
# 3/12/2021
#
# Day 3
#
# Code is a little brute force but it did the job.
#

def filter_list_by_common_bit( list, pos ):
    count = 0
    for line in list:
        if line[ pos ] == "1":
            count+=1

    sub_list = []
    match = "0"
    if count >= len(list)/2:
        match = "1"
    
    for line in list:
        if line[ pos ] == match:
            sub_list.append( line )

    return sub_list

def filter_list_by_least_common_bit( list, pos ):
    count = 0
    for line in list:
        if line[ pos ] == "1":
            count+=1

    sub_list = []
    match = "0"
    if count < len(list)/2:
        match = "1"
    
    for line in list:
        if line[ pos ] == match:
            sub_list.append( line )

    return sub_list

if __name__ == '__main__':
    report = []
    with open( '3.input.txt' ) as fp:
        for line in fp:
            report.append( line[:-1] )

    counts = [0 for i in range( len( report[0] ) ) ]
    for line in report:
        for i in range( len( counts ) ):
            counts[ i ] += int( line[i] )

    rows = len( report )
    gbits = ""
    ebits = ""
    for i in range( len( counts ) ):
        if counts[i] > rows/2:
            gbits += "1"
            ebits += "0"
        elif counts[i] < rows/2:
            gbits += "0"
            ebits += "1"
        else:
            gbits += "0"
            ebits += "0"

    gamma = int(gbits,2)
    epsilon = int(ebits,2)

    print("1. ",gamma * epsilon)

    sub_list = report
    for i in range( len( counts ) ):
        sub_list = filter_list_by_common_bit( sub_list, i )
        if len( sub_list ) == 1:
            break
    oxygen = int(sub_list[0],2)

    sub_list = report
    for i in range( len( counts ) ):
        sub_list = filter_list_by_least_common_bit( sub_list, i )
        if len( sub_list ) == 1:
            break
    co2 = int(sub_list[0],2)

    print("2. ",co2 * oxygen)
