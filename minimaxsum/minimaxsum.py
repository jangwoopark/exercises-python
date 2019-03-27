#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):

    tot = sum(arr)
    res = []
    for i in arr:
        res.append(tot - i)
    
    print("{} {}".format(min(res), max(res)))
    
if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
