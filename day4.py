#!/usr/bin/python3
#
# https://adventofcode.com/
# 4/12/2021
#
# Day 4
#
# Code is a little brute force but it did the job.
#

import re


def play_board( board, n, b ):
    for y in range(len(board)):
        for x in range(len(board[y])):
            if board[y][x] == n:
                board[y][x] = "*"

def has_board_won( board ):
    # check each row for a complete row
    for y in range(len(board)):
        row_wins = 0
        for x in range(len(board[y])):
            if board[y][x] == "*":
                row_wins += 1
        if row_wins == len(board[y]):
            return True
    # check each column for a complete column
    for x in range(len(board[0])):
        col_wins = 0
        for y in range(len(board)):
            if board[y][x] == "*":
                col_wins += 1
        if col_wins == len(board):
            return True

    return False
    
def sum_board( board ):
    sum = 0
    for y in range(len(board)):
        for x in range(len(board[y])):
            if board[y][x] != "*":
                sum += int(board[y][x])
    return sum

if __name__ == '__main__':
    boards = []
    picking = []
    n = 0
    with open( '4.input.txt' ) as fp:
        board = []
        for line in fp:
            line = line[:-1]
            if n == 0:
                picking = line.split(",")
            else:
                if line == "":
                    if len(board) > 0:
                        boards.append( board )
                        board = []
                else:
                    line = re.sub("^\s+","",line )
                    line = re.sub("\s+",",",line )
                    board.append( line.split(",") )
            n+=1
    
    if len(board) > 0:
        boards.append( board )    

    part1_won = False
    board_set = set()
    for b in range(len(boards)):
        board_set.add( b )

    done = False
    last_board = None
    for n in picking:
        if len( board_set ) == 1:
            for a in board_set:
                last_board = a

        for b in range(len(boards)):
            play_board( boards[b], n, b )
            if not part1_won:
                if has_board_won( boards[b] ):
                    part1_won = True
                    sum = sum_board( boards[b] )
                    print("1.",sum * int(n))
                    break
            else:
                if has_board_won( boards[b] ):
                    if b in board_set:
                        board_set.remove( b )

                    if b == last_board:
                        sum = sum_board( boards[a] )
                        print("2.",sum * int(n))
                        done = True
                        break
        if done:
            break
