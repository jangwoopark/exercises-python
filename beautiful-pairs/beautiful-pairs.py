#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

def beautifulPairs(A, B):
    diff = sum((Counter(A) - Counter(B)).values())
    return len(A) - diff +1 if diff else len(A) - 1
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    A = list(map(int, input().rstrip().split()))

    B = list(map(int, input().rstrip().split()))

    result = beautifulPairs(A, B)

    fptr.write(str(result) + '\n')

    fptr.close()
