#!/bin/python3

import os
import sys
import math

def solve(x):
    C = (math.sqrt(3)*math.sqrt(3888*x*x-1)+x*108)**(1./3.)
    return math.floor((C/9**(1./3.)+1/(3**(1./3.)*C)-1)/2+0.0000001)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        x = int(input())

        result = solve(x)

        fptr.write(str(result) + '\n')

    fptr.close()
