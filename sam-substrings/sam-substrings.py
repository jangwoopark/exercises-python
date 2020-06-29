#!/bin/python3

import math
import os
import random
import re
import sys

def substrings(n):
    s=str(n)
    sum_set=0
    psum=0
    for i in range(len(s)):
        psum=(psum*10)+(i+1)*int(s[i])
        sum_set+=psum
    return (sum_set)%((10**9)+7)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = input()

    result = substrings(n)

    fptr.write(str(result) + '\n')

    fptr.close()
