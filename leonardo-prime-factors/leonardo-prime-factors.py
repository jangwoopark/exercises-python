#!/bin/python3

import os
import sys

def primeCount(n):
    a=[]
    for i in range(2,100):
        f=0
        for j in range(2,int(i**0.5)+1):
            if(i%j==0):
                f=1
                break
        if(f==0):
            a.append(i)
    s=1
    c=0
    while(s<=n):
        s=s*a[c]
        c+=1

    return c-1
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        n = int(input())

        result = primeCount(n)

        fptr.write(str(result) + '\n')

    fptr.close()
