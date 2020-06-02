#!/bin/python3

import os
import sys

def solve(n, p):
    a = 1

    n1 = n + 1
    while n >= p:
        n, r = divmod(n, p)
        a *= r + 1
    a *= n + 1
    a = n1 - a
    return a
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        np = input().split()

        n = int(np[0])

        p = int(np[1])

        result = solve(n, p)

        fptr.write(str(result) + '\n')

    fptr.close()
