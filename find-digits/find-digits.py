#!/bin/python3

import math
import os
import random
import re
import sys

def findDigits(n):
    return sum([not n % i for i in map(int, str(n)) if i != 0])
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = findDigits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
