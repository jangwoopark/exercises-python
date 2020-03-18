#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

def minimumDistances(a):
    d = defaultdict( list )
    for i in range( len(a) ):
        d[ a[i] ].append( i )
    if len(d) == len(a) : return -1
    return min( j-i for k in d for i in d[k] for j in d[k] if i < j )

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    fptr.write(str(result) + '\n')

    fptr.close()
