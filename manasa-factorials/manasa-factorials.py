#!/bin/python3

import os
import sys

def getdiff(no):
    temp=no
    count=0
    while temp >=5:
        temp=int(temp/5)
        count=count+temp
    return count

def solve(n):
    if n>5:
        res=n*5-(n-(n%5))
        df=getdiff(res)
        while df < n:
            res=+res+5
            df=getdiff(res)
        return res
    else:
       return n*5

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = solve(n)

        fptr.write(str(result) + '\n')

    fptr.close()
