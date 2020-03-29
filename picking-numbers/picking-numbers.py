#!/bin/python3

import math
import os
import random
import re
import sys

def pickingNumbers(a):
    count = [0] * (max(a) + 1)
    for i in a:
        count[i] += 1
        count[i - 1] += 1

    return max(count)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
