#!/bin/python3

import os
import sys
import itertools

def solve(n):
    p = itertools.permutations(str(n), min(len(str(n)), 3))
    for i in p:
        val = int("".join(i))
        if val % 8 == 0:
            return 'YES'
    return 'NO'
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = input()

        result = solve(n)

        fptr.write(result + '\n')

    fptr.close()
