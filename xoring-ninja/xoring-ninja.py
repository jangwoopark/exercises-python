#!/bin/python3

import os
import sys

def xoringNinja(arr):
    ans = 0
    for x in arr:
        ans |= x

    ans <<= len(arr) - 1
    return ans % 1000000007

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        arr_count = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = xoringNinja(arr)

        fptr.write(str(result) + '\n')

    fptr.close()
