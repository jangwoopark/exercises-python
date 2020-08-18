#!/bin/python3

import math
import os
import random
import re
import sys

def flippingBits(n):
    aa = format(n, '032b')
    return int (''.join('1' if x == '0' else '0' for x in aa), 2)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        n = int(input())

        result = flippingBits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
