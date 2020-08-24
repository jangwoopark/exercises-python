#!/bin/python3

import math
import os
import random
import re
import sys

def f(a):
    r=[a,a,2,2,a+2,a+2,0,0]
    return r[a%8]

def xorSequence(l, r):
    return f(r)^f(l-1)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        lr = input().split()

        l = int(lr[0])

        r = int(lr[1])

        result = xorSequence(l, r)

        fptr.write(str(result) + '\n')

    fptr.close()
