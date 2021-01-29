#!/bin/python3

import os
import sys
from bisect import bisect_right, bisect_left


def solve(shots, players):
    start, end = [], []
    # separate starts and ends points...
    for shot in shots:
        i, j = shot
        start.append(i)
        end.append(j)
    # sort...
    start.sort()
    end.sort()
    res = 0
    # find with binary search how many intervals to consider...
    for player in players:
        i, j = player
        res += bisect_right(start, j) - bisect_left(end, i)
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    shots = []

    for _ in range(n):
        shots.append(list(map(int, input().rstrip().split())))

    players = []

    for _ in range(m):
        players.append(list(map(int, input().rstrip().split())))

    result = solve(shots, players)

    fptr.write(str(result) + '\n')

    fptr.close()
