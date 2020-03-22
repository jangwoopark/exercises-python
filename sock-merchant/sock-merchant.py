#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

def sockMerchant(n, ar):
    sum=0
    for values in Counter(ar).values():
        sum+=values//2
    return sum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
