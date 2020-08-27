#!/bin/python3

import math
import os
import random
import re
import sys

def theGreatXor(x):
    value = 1
    while value <= x:
        value *= 2
    return value -1 -x

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        x = int(input())

        result = theGreatXor(x)

        fptr.write(str(result) + '\n')

    fptr.close()
