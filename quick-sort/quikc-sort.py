import math
import os
import random
import re
import sys

# Complete the quickSort function below.
def quickSort(arr):
    n = len(arr)
    left_list = []
    right_list = []
    equal_list = []
    p = arr[0]  #pivot
 
    for i in range(n):
        if arr[i] > p:
            right_list.append(arr[i])
        elif arr[i] < p:
            left_list.append(arr[i])
        else:
            equal_list.append(arr[i])

    print("left_list = ", left_list)
    print("equal_list = ", equal_list)
    print("right_list = ", right_list)

    result = ''
    if left_list:
        for num in left_list:
            result = result + str(num)          

    if right_list:
        for num in equal_list:
            result = result + str(num) 
    if equal_list:
        for num in right_list:
            result = result + str(num)
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = quickSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
