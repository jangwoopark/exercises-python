#!/bin/python3

import os
import sys

def compute_score(group_1, group_2):
    score = 0
    for i in group_1:
        for j in group_2:
            score += abs(i - j)    
    return score

def fairCut(k, arr):
    arr.sort()
    
    if 2 * k > n:
        k = n - k
    
    start = (len(arr) - 2 * k) // 2
    stop = start + 2 * k
    group_1, group_2 = [], []

    for i in range(len(arr)):
        if stop >= i >= start and (i - start) % 2 == 1:
            group_1.append(arr[i])
        else:
            group_2.append(arr[i])
    
    return compute_score(group_1, group_2)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = fairCut(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
