#!/bin/python3

import math
import os
import random
import re
import sys

def fairRations(B):
    counting = False
    count = 0
    for b in B:
        if counting:
            count += 2
        if b % 2:
            counting = not counting
    else:
        if counting:
            return "NO"

    return count
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    N = int(input())

    B = list(map(int, input().rstrip().split()))

    result = fairRations(B)

    fptr.write(str(result) + '\n')

    fptr.close()
