#!/bin/python3

import math
import os
import random
import re
import sys

def cost(B):
    L=len(B)
    dp=matrix = [[0 for i in range(2)] for i in range(L)]
    i=1
    while i<len(B):
        dp[i][0]=max(dp[i-1][0], dp[i-1][1]+B[i-1]-1)
        dp[i][1]=max(dp[i-1][0]+B[i]-1, dp[i-1][1]+abs(B[i]-B[i-1]))
        i += 1
    
    return max(dp[L-1][0],dp[L-1][1])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        B = list(map(int, input().rstrip().split()))

        result = cost(B)

        fptr.write(str(result) + '\n')

    fptr.close()
