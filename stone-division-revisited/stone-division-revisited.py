#!/bin/python3

import math
import os
import random
import re
import sys


def pathFinder(s, paths):
    if len(s) == 0:
        return paths
    else:
        for i in range(0,len(s)):
            path = []
            path.append(s[0])
            for m in s[1:i+1]:
                if m%path[-1] == 0 and path[-1] != m:
                    path.append(m)
            if path[::-1] not in paths:
                paths.append(path[::-1])
        return pathFinder(s[:-1], paths)
        
def maxPossibleMoves(dim, path, blocks):
    if len(path) == 0:
        return 0
    else:
        return blocks + maxPossibleMoves(path[0], path[1:], blocks*dim//path[0])

if __name__ == "__main__":
    q = int(input().strip())
    for a0 in range(q):
        n, m = input().strip().split(' ')
        n, m = [int(n), int(m)]
        S = list(map(int, input().strip().split(' ')))
        S = sorted(S)
        s = []
        for m in S:
            if n%m == 0 and n != m:
                s.append(m)
        paths = []
        paths = pathFinder(s, paths)
        result = 0
        for i in range(len(paths[:])):
            result_new = maxPossibleMoves(n, paths[i][:], 1)
            if result_new > result:
                result = result_new
        print(result)
