#!/bin/python3

import os
import sys

def bi_search(arr,v):
    st,end=0,len(arr)-1
    while st<=end:
        mid=(st+end)>>1
        if arr[mid]==v:
            return True
        elif arr[mid]>v:
            end=mid-1
        else:
            st=mid+1
    return False

def solve(a):
    accu=[]
    accu.append(0)
    cur_sum=0
    for i in range(len(a)):
        cur_sum+=a[i]
        accu.append(cur_sum)
    max_sum=accu[-1]
    
    res=[]
    for i in range(1,len(accu)):
        j=accu[i]*2
        while j<max_sum:
            if bi_search(accu,j):
                j+=accu[i]
            else:
                break
        if j==max_sum:
            res.append(accu[i])
    res.append(max_sum)
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a_count = int(input())

    a = list(map(int, input().rstrip().split()))

    result = solve(a)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
