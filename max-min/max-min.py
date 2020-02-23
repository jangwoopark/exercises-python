#!/bin/python3

import math
import os
import random
import re
import sys

def maxMin(k, arr):
    ans = 10**9
    arr_s = sorted(arr)
    for i in range(len(arr) - k + 1):
            sub_arr_min = arr_s[i]
            sub_arr_max = arr_s[i+k-1]
            ans = min(sub_arr_max - sub_arr_min, ans)
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    k = int(input())

    arr = []

    for _ in range(n):
        arr_item = int(input())
        arr.append(arr_item)

    result = maxMin(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
