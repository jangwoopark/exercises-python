#!/bin/python3

import os
import sys

MOD = 1000000007

def solve(n):
    e = (pow(2, n, MOD - 1) - n) % (MOD - 1)

    r = pow(2, e, MOD)

    return r

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = solve(n)

        fptr.write(str(result) + '\n')

    fptr.close()
