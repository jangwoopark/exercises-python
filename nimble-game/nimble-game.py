#!/bin/python3

import math
import os
import random
import re
import sys
from functools import reduce
# Complete the nimbleGame function below.
def nimbleGame(s):
    a=[]
    for i in range(n):
        a+=[i]*(s[i]%2)
    if a==[]:
        return 'Second'
    else:
        return 'First' if reduce((lambda x,y:x^y),a) else 'Second'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        s = list(map(int, input().rstrip().split()))

        result = nimbleGame(s)

        fptr.write(result + '\n')

    fptr.close()
