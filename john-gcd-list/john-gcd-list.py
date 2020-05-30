#!/bin/python3

import os
import sys
import math

def solve(a):
    b = []
    x = a[0]
    for item in a:
        b.append((x*item)//math.gcd(x,item))
        x = item
    b.append(a[-1])
    return b

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        a_count = int(input())

        a = list(map(int, input().rstrip().split()))

        result = solve(a)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
