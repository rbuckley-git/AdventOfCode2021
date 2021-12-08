#!/usr/bin/python3
#
# https://adventofcode.com/
# 8/12/2021
#
# Day 8
#
# This was a late effort as needing to put kids to bed. Part 1 was easy. Part 2 required a lot of thinking.
# eventually the approach of distinguishing the 2 from the 5 and the 0 from the 9 took shap by carefully
# subtracting more than one digit from each in turn and seeing how many segments remained. It was useful to 
# sort the parts alphabetically too.

def sort_entries( pattern ):
    p = []
    for d in pattern:
        p.append( ''.join(sorted(d)))
    return p

def find_digit( data, pattern, digit ):
    for a in data:
        if len(a) == len(pattern[digit]):
            return a

def find_with_length( data, l ):
    s = {}
    for a in data:
        if len(a) == l and a not in s:
            s[ a ] = 1
    return list(s.keys())


if __name__ == '__main__':
    pos = []

    # this was useful for storing lengths but it could have been simpler as the actual text is not used.
    pattern = ["bacefg","cf","acdeg","acdfg","bcdf","abdfg","abdefg","acf","abcdefg","abcdfg"]

    data = []
    with open( '8.input.txt' ) as fp:
        for line in fp:
            (l,r) = line[:-1].split(" | ")
            inputs = l.strip().split(" ")
            outputs = r.strip().split(" ")
            rec = {}
            # order of letters does not matter so it makes it easier to match later if they are sorted
            rec["input"] = sort_entries(inputs)
            rec["output"] = sort_entries(outputs)
            data.append( rec )

    # part 1 is just a simple look for the specific unique length cases and add them up
    count = 0
    for d in data:
        e = d["output"]
        for a in e:
            for i in [1,4,7,8]:
                if len(a) == len(pattern[i]):
                    count+=1
    print("1.",count)

    answer = 0
    for d in data:
        input = d["input"]

        digits = [None for i in range(10) ]

        # simple unique length digits
        digits[1] = find_digit( input, pattern, 1 )
        digits[4] = find_digit( input, pattern, 4 )
        digits[7] = find_digit( input, pattern, 7 )
        digits[8] = find_digit( input, pattern, 8 )

        # get some arrays containing these lengths
        len5 = find_with_length( input, 5 )
        len6 = find_with_length( input, 6 )

        # 6 will be one of the 6 character lengths missing one of the digit 1 characters
        for b in len6:
            for a in digits[1]:
                if a not in b:
                    digits[6] = b
        len6.remove( digits[6] )

        # 3 will be the 5 character length that includes both digit1 chatacters
        for b in len5:
            if digits[1][0] in b and digits[1][1] in b:
                digits[3] = b
        len5.remove( digits[3] )

        # find 0 and 9 by subtract 3 then 4 from each 6 chatacter
        for b in len6:
            dd = b
            for a in digits[3]:
                b = b.replace(a,"")
            for a in digits[4]:
                b = b.replace(a,"")
            if len(b) == 1:
                digits[0] = dd
            if len(b) == 0:
                digits[9] = dd

        # find 2 and 5 by subtract 3 then 4 from each 5 chatacter
        for b in len5:
            dd = b
            for a in digits[3]:
                b = b.replace(a,"")
            for a in digits[4]:
                b = b.replace(a,"")
            if len(b) == 1:
                digits[2] = dd
            if len(b) == 0:
                digits[5] = dd

        result = ""
        for a in d["output"]:
            result += str(digits.index( a ))
        answer += int(result)

    print("2",answer)