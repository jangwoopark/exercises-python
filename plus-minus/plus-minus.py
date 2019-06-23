import math
import os
import random
import re
import sys

def plusMinus(arr):
    positive = 0
    negative = 0
    zeroes = 0
    for i in arr:
        if i > 0:
            positive += 1
        elif i < 0:
            negative += 1
        else:
            zeroes += 1

    Length = len(arr)
    print(positive/Length)
    print(negative/Length)
    print(zeroes/Length)

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
