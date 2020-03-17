#!/bin/python3

import math
import os
import random
import re
import sys

def beautifulTriplets(d, arr):
    bt = 0
    for i in arr:
        if (i+d) in arr and (i+d)+d in arr:
            bt += 1
    return bt

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    arr = list(map(int, input().rstrip().split()))

    result = beautifulTriplets(d, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
