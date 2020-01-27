#!/bin/python3

import os
import sys
from collections import Counter

def solve(a):
    return sum([i * (i - 1) for i in a.values()])
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        a_count = int(input())

        a = Counter(map(int, input().rstrip().split()))

        result = solve(a)

        fptr.write(str(result) + '\n')

    fptr.close()
