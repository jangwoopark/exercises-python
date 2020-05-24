#!/bin/python3

import os
import sys

def find_gcd(x, y): 
    while(y): 
        x, y = y, x % y 
  
    return x 

def solve(a, queries):
    l=[]
    num1=a[0] 
    num2=a[1] 
    f=0
    if(len(list(set(a)))==1):
        f=1
    gcd=find_gcd(num1,num2)
    for i in range(2,len(a)): 
        gcd=find_gcd(gcd,a[i])
    for j in range(len(queries)):
        if(f==1):
            l.append(gcd+queries[j])
        else:
            l.append(find_gcd(gcd,queries[j]))
    return l

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nq = input().split()

    n = int(nq[0])

    q = int(nq[1])

    a = list(map(int, input().rstrip().split()))

    queries = []

    for _ in range(q):
        queries_item = int(input())
        queries.append(queries_item)

    result = solve(a, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
