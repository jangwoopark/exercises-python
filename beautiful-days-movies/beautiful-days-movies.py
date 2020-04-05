#!/bin/python3

import math
import os
import random
import re
import sys

def beautifulDays(i, j, k):
    return sum ([1 for i in range(i, j + 1) if (int(str(i)[::-1]) - i) % k == 0])
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ijk = input().split()

    i = int(ijk[0])

    j = int(ijk[1])

    k = int(ijk[2])

    result = beautifulDays(i, j, k)

    fptr.write(str(result) + '\n')

    fptr.close()
