#!/bin/python3

import math
import os
import random
import re
import sys

def andProduct(a, b):
    if a == b: return(a)
    zl = len(bin(a ^ b)[2:])
    return(int(('1'*(32-zl)) + ('0'*zl), 2) & a)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    for n_itr in range(n):
        ab = input().split()

        a = int(ab[0])

        b = int(ab[1])

        result = andProduct(a, b)

        fptr.write(str(result) + '\n')

    fptr.close()
