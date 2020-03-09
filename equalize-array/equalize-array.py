#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

def equalizeArray(arr):
    d=Counter(arr).values()
    deletion=len(arr)-max(d)

    return deletion
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
