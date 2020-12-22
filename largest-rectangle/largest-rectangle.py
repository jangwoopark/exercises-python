#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the largestRectangle function below.
def largestRectangle(h):
    def helper(i,j,h):
        if j == i:
            return h[i]
        else:
            currMin = min(h[i:j+1])
            currArea = currMin * (j-i+1)
            m = h[i:j+1].index(currMin)+i
            print(f'{i} {m} {j}')
            return max(max(helper(i,m-1,h) if m-1>=i else h[i],currArea),max(helper(m+1,j,h) if m+1<=j else h[j],currArea))
    res = helper(0,len(h)-1,h)
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    h = list(map(int, input().rstrip().split()))

    result = largestRectangle(h)

    fptr.write(str(result) + '\n')

    fptr.close()
