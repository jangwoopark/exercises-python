#!/bin/python3

import math
import os
import random
import re
import sys

def getTotalX(a, b):
    
    x=a[len(a)-1]
    y=b[0]
    count=0

    for p in range(x,y+1):
        chk=0
        for i in b:
            if i%p!=0:
                chk=1
                break
        if chk == 1:
            continue
        else:
            chk1=0
            for i in a:
                if p%i!=0:
                    chk1=1
                    break
            if chk1==0:
                count+=1
    return count
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
