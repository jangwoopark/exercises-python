#!/bin/python3

import math
import os
import random
import re
import sys


def workbook(n, k, arr):
    chapter=0 
    page=0 
    problemHi=0
    problemLow=0
    specials=0
    
    while chapter<len(arr):
        
        problemLow=problemHi+1
        page+=1

        if problemHi+k>arr[chapter]:
            problemHi=arr[chapter]
        else:
            problemHi+=k
                
        if page<=problemHi and page>=problemLow:
            specials+=1
        
        if problemHi==arr[chapter]:
            chapter+=1
            problemHi=0
            problemLow=0
    
    return specials 
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = workbook(n, k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
