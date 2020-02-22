#!/bin/python3

import math
import os
import random
import re
import sys

def getMinimumCost(k, c):
    return sum((v * (i // k + 1) for i, v in enumerate(sorted(c, reverse=True))))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    minimumCost = getMinimumCost(k, c)

    fptr.write(str(minimumCost) + '\n')

    fptr.close()
