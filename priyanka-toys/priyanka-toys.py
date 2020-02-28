#!/bin/python3

import math
import os
import random
import re
import sys

def toys(w):
    w = set(w)
    a = 0
    while len(w) >0:
        z = min(w)
        a += 1
        w = list(filter(lambda x: x > z + 4, w))
    return a

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    w = list(map(int, input().rstrip().split()))

    result = toys(w)

    fptr.write(str(result) + '\n')

    fptr.close()
