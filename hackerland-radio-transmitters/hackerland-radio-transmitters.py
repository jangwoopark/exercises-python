#!/bin/python3

import math
import os
import random
import re
import sys

def hackerlandRadioTransmitters(x, k):
    count_sort = [0] * (max(x)+1)
    for i in x:
        count_sort[i] = 1
    
    left = None
    right = 0
    transmitters = 0
    for i, c in enumerate(count_sort):
        if i < right:
            continue
        
        if c:
            right = i
            if left is None:
                left = i
                continue
            
        if left is not None:
            if i - left == k:
                right += k + 1
                left = None
                transmitters += 1
    else:
        if right < len(count_sort):
            transmitters += 1
    return transmitters

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    x = list(map(int, input().rstrip().split()))

    result = hackerlandRadioTransmitters(x, k)

    fptr.write(str(result) + '\n')

    fptr.close()
