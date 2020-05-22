#!/bin/python3

import os
import sys

def solve(a, b):
    return pow(int(a),int(b),10**9+7)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        ab = input().split()

        a = ab[0]

        b = ab[1]

        result = solve(a, b)

        fptr.write(str(result) + '\n')

    fptr.close()
