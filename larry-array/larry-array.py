#!/bin/python3

import math
import os
import random
import re
import sys


def larrysArray(A):
    inv = sum(sum(A[i] > j for j in A[i + 1:]) for i in range(len(A) - 1))
    return('NO' if inv % 2 else 'YES')

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        A = list(map(int, input().rstrip().split()))

        result = larrysArray(A)

        fptr.write(result + '\n')

    fptr.close()
