#!/bin/python3

import math
import os
import random
import re
import sys

def jumpingOnClouds(c, k):
    e = 100
    p = 0
    while e != 0:
        p += k
        if p >= len(c) : p = p%len(c)
        e = e-1 - (c[p]*2)
        if p == 0 : break 
    return e

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c, k)

    fptr.write(str(result) + '\n')

    fptr.close()
