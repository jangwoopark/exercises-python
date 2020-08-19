#!/bin/python3

import math
import os
import random
import re
import sys

def sansaXor(arr):
    result = 0
    n = len(arr)
    if n%2!=0:
        arr = arr[0::2]
        for x in arr:result^=x 
        return result
    else:
        return 0

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = sansaXor(arr)

        fptr.write(str(result) + '\n')

    fptr.close()
