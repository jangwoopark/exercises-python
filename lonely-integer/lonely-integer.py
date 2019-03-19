#!/bin/python3

import math
import os
import random
import re
import sys
from functools import reduce

# Complete the lonelyinteger function below.
def lonelyinteger(a):
    answer = reduce((lambda x, y: x^y), a)
    return answer
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    fptr.write(str(result) + '\n')

    fptr.close()
