#!/bin/python3

import os
import sys


def solve(n):
    i = 1
    while(True):
        t = int(bin(i)[2:])*9
        if(t%n == 0):
            return str(t)
        else:
            i+=1
            continue
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = solve(n)

        fptr.write(result + '\n')

    fptr.close()
