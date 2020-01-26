#!/bin/python3

import math
import os
import random
import re
import sys

def almostSorted(arr):
    prev = arr[0]
    start = -1
    end = len(arr)
    count = 0
    if len(arr) == 2:
        if arr[0]>arr[1]:
            print('yes')
            print('swap', 1, 2)
        else:
            print('yes')
        return
    for i in range(1, len(arr)):
        if arr[i-1] > arr[i]:
            count += 1
            if end != len(arr):
                end = i
            else:
                start = i-1
                end = i

    if end - start == count:
        if count == 1:
            if start == 0:
                if arr[start] > arr[end+1]:
                    print('no')
                else:
                    print('yes')
                    print('swap', start+1, end+1)
            elif end == len(arr)-1:
                if arr[end] < arr[start-1]:
                    print('no')
                else:
                    print('yes')
                    print('swap', start+1, end+1)
            else:
                if arr[start] > arr[end+1] or arr[end] < arr[start-1]:
                    print('no')
                else:
                    print('yes')
                    print('swap', start+1, end+1)
        else:
            if start == 0:
                if end == len(arr)-1:
                    print('yes')
                    print('reverse', start+1, end+1)
                else:
                    if arr[start] > arr[end+1]:
                        print('no')
                    else:
                        print('yes')
                        print('reverse', start+1, end+1)
            elif end == len(arr)-1:
                if arr[end] < arr[start-1]:
                    print('no')
                else:
                    print('yes')
                    print('reverse', start+1, end+1)
            else:
                if arr[start] > arr[end+1] or arr[end] < arr[start-1]:
                    print('no')
                else:
                    print('yes')
                    print('reverse', start+1, end+1)
    elif start is -1:
        print('yes')
    elif count == 2:
        if arr[end] > arr[start+1] or arr[start] < arr[end-1]:
            print('no')
            return
        
        if start == 0:
            if end == len(arr)-1:
                print('yes')
                print('swap', start+1, end+1)   
            else:
                if arr[start] > arr[end+1]:
                    print('no')
                else:
                    print('yes')
                    print('swap', start+1, end+1)     
        else:
            if end == len(arr)-1:
                if arr[end]<arr[start-1]:
                    print('no')
                else:
                    print('yes')
                    print('swap', start+1, end+1)
            elif arr[start]>arr[end+1] or arr[end]<arr[start-1]:
                print('no')
            else:
                print('yes')
                print('swap', start+1, end+1)
    else:
        print('no')
    
if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    almostSorted(arr)
