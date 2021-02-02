#!/bin/python3

import os
import sys

def solve(arr):
    stack_left, stack_right = [], []
    left, right = [], []
    # left -> right
    for i,e in enumerate(arr):
        while stack_left and e >= stack_left[-1][0]:
            stack_left.pop()
        left.append(stack_left[-1][1] if stack_left else 0)
        stack_left.append((e, i+1))
    # right -> left
    for i in reversed(range(len(arr))):
        while stack_right and arr[i] >= stack_right[-1][0]:
            stack_right.pop()
        right.append(stack_right[-1][1] if stack_right else 0)
        stack_right.append((arr[i], i+1))
    # multiply and we are done...
    res = -float('inf')
    for i,e in enumerate(left):
        res = max(res, (left[i])*(right[len(right)-1 -i]))
    return res
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = solve(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
