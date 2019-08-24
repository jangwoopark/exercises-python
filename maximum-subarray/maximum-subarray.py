import math
import os
import random
import re
import sys

# Complete the maxSubarray function below.
def maxSubarray(arr):
    maxEle = max(arr)
    if maxEle < 0:
        return (maxEle, maxEle)
    maxSumSeq = sum(e for e in arr if e > 0)

    n = len(arr)
    sums = [None] * n
    sums[0] = (arr[0], arr[0])
    for i in range(1, n):
        sumMax, sumMaxWithLast = sums[i - 1]
        sumWithLastI = sumMaxWithLast + arr[i]
        if sumWithLastI > arr[i]:
            sums[i] = (sumWithLastI, sumWithLastI) if sumWithLastI > sumMax else (sumMax, sumWithLastI)
        else:
            sums[i] = (arr[i], arr[i]) if arr[i] > sumMax else (sumMax, arr[i])
    return (sums[-1][0], maxSumSeq)
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = maxSubarray(arr)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
