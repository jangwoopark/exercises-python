#!/bin/python3

import math
import os
import random
import re
import sys

def sumXor(n):
    if n==0:
        return 1
    return 2**bin(n).split('b')[1].count('0')

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = sumXor(n)

    fptr.write(str(result) + '\n')

    fptr.close()
