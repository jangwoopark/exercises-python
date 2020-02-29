#!/bin/python3

import math
import os
import random
import re
import sys

def largestPermutation(k, arr):
    lenA = len(arr)
    sorted_arr = list(i+1 for i in range(lenA))
    sorted_arr.reverse()

    arr_dict = {}
    for j, item in enumerate(arr):
        arr_dict[item] = j  # no duplicates of nums
    for i, item in enumerate(sorted_arr):
        if arr[i] != item:
            k -= 1
            j = arr_dict[item]
            arr[i], arr[j] = item, arr[i]
            # update the dictionary after swapping
            arr_dict[item] = i
            arr_dict[arr[j]] = j
            if 0 == k:
                return arr
    return arr

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = largestPermutation(k, arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
