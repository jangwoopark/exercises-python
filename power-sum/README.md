#!/bin/python3

import math
import os
import random
import re
import sys

def res(X, N, k):
    p = pow(k,N)
    if p == X:
        return 1
    elif p < X:
        return res(X-p, N,k+1) + res(X, N,k+1)
    else:
        return 0

# Complete the powerSum function below.
def powerSum(X, N):
    return res(X, N, 1)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    X = int(input())

    N = int(input())

    result = powerSum(X, N)

    fptr.write(str(result) + '\n')

    fptr.close()
