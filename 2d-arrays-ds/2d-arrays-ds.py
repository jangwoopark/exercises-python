import math
import os
import random
import re
import sys

def hourglassSum(arr):
    return (max([sum(arr[i-1][j-1:j+2] + [arr[i][j]] + arr[i+1][j-1:j+2]) for j in range(1, 5) for i in range(1, 5)]))
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
