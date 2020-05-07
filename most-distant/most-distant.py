#!/bin/python3

import os
import sys
import itertools

def solve(coordinates):
    yc = lambda c: c[1]
    xc = lambda c: c[0]

    top = max(coordinates, key=yc)
    bottom = min(coordinates, key=yc)
    right = max(coordinates, key=xc)
    left = min(coordinates, key=xc)

    extremes = [top, bottom, right, left]

    max_dist = 0
    for i, j in itertools.combinations(extremes, 2):
        dist = ((i[0] - j[0])**2 + (i[1] - j[1])**2) ** 0.5
        max_dist = max(dist, max_dist)

    return max_dist
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    coordinates = []

    for _ in range(n):
        coordinates.append(list(map(int, input().rstrip().split())))

    result = solve(coordinates)

    fptr.write(str(result) + '\n')

    fptr.close()
