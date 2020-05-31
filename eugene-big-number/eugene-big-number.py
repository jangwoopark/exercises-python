#!/bin/python3

import os
import sys

def solve(a, n, m):
    return (((((pow(10,n*(len(str(a))),(10**(len(str(a))) - 1)*m)-1)//(10**(len(str(a))) - 1))%m)*(a%m)%m))

    if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        anm = input().split()

        a = int(anm[0])

        n = int(anm[1])

        m = int(anm[2])

        result = solve(a, n, m)

        fptr.write(str(result) + '\n')

    fptr.close()
