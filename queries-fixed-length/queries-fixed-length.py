#!/bin/python3

import os
import sys

# Complete the solve function below.
def solve(arr, queries):
    l=[]
    for i in queries:
        d=i
        minn=1000000000
        m=max(arr[0:d])
        if(minn>m):
            minn=m
        for j in range(d,len(arr)):
            if(m!=arr[abs(d-j)] and m<=arr[j]):
                m=arr[j]
            elif(m==arr[abs(d-j)]):
                m=max(arr[abs(d-j)+1:j+1])
            if(minn>m):
                minn=m
        l.append(minn)
    return l
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nq = input().split()

    n = int(nq[0])

    q = int(nq[1])

    arr = list(map(int, input().rstrip().split()))

    queries = []

    for _ in range(q):
        queries_item = int(input())
        queries.append(queries_item)

    result = solve(arr, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
