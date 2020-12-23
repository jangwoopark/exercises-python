#!/bin/python3

import os
import sys


def andXorOr(a):
    ans=-1
    s=[0]
    i=1
    while i<len(a):
        if s==[]:
            s.append(i)
            i+=1
        elif  a[i]>a[s[-1]]:
            s.append(i)
            t=a[s[-1]]^a[s[-2]]
            i+=1
        else:
            top=s.pop(-1)
            t=a[i]^a[top]
        if t>ans:ans=t   
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a_count = int(input())

    a = list(map(int, input().rstrip().split()))

    result = andXorOr(a)

    fptr.write(str(result) + '\n')

    fptr.close()
