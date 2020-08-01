#!/bin/python3

import math
import os
import random
import re
import sys

def highestValuePalindrome(s, n, k):
    if (n == 1):
        if (k == 1):
            return '9'
        else:
            return '-1'
    arr = list(s)
    changes = [0 for _ in range(n)]
    for i in range(int(n / 2) + (n & 1)):
        if (arr[i] != arr[n - 1 - i]):
            arr[i] = arr[n - 1 - i] = max(arr[i], arr[n - 1 - i])
            changes[i] += 1
            k -= 1
        if (k < 0):
            return '-1'
    for i in range(int(n / 2) + (n & 1)):
        if (arr[i] == arr[n - 1 - i]):
            if (arr[i] != '9'):
                if (changes[i] == 1 or i == (n - 1 - i)):
                    cost = 1
                else:
                    cost = 2
                if (k >= cost):
                    arr[i] = arr[n - 1 - i] = '9'
                    k -= cost
    return ''.join(arr)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    s = input()

    result = highestValuePalindrome(s, n, k)

    fptr.write(result + '\n')

    fptr.close()
