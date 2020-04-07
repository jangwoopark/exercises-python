#!/bin/python3

import math
import os
import random
import re
import sys

def countingSort(arr):
    c = [0] * 100
    output = []
    for a in arr:
        c[a] += 1
    for v in range(100):
        output += [v] * c[v]
    return output
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
