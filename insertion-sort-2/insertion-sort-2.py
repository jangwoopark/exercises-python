#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the insertionSort2 function below.
def insertionSort2(n, arr):
    for i in range(1, n):
        j = 0
        key = arr[i]
        del arr[i]
        while j < i and arr[j] < key:
            j += 1
        arr.insert(j, key)
        print(*arr)
if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)
