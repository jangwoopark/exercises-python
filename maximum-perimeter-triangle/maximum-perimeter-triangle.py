#!/bin/python3

import math
import os
import random
import re
import sys

def maximumPerimeterTriangle(sticks):
    sSticks = sorted(sticks)
    for i in range(len(sticks) - 1, 1, -1):
        if sSticks[i] < sSticks[i-1] + sSticks[i-2]:
            return [sSticks[i-2], sSticks[i-1], sSticks[i]]
    return [-1]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    sticks = list(map(int, input().rstrip().split()))

    result = maximumPerimeterTriangle(sticks)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
