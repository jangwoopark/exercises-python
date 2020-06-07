#!/bin/python3

import os
import sys

def solve(V):
    n=len(V)
    ans=(n - n / 2) * (n / 2) * 2 * (1000000000 / (1000 * 10))
    V.sort()
    c=0
    print(V)
    for i in range(0,len(V)-1):
        if(V[i]+1==V[i+1]):
            c+=1
        else:
            
            ans+=(c+1)//2
            c=0
    ans+=(c+1)//2
    
    return int(ans*2)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    V_count = int(input())

    V = list(map(int, input().rstrip().split()))

    result = solve(V)

    fptr.write(str(result) + '\n')

    fptr.close()
