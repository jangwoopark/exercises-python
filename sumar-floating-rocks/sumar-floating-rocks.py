#!/bin/python3

import os
import sys
import math

def solve(x1, y1, x2, y2):
    if(x1==x2):
        return abs(y2-y1)-1
    elif(y1==y2):
        return abs(x2-x1) -1
    t=math.gcd(abs(y2-y1),abs(x2-x1))
    t1=abs(y2-y1)//(abs(y2-y1)//t)
    return t1-1
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        x1Y1X2Y2 = input().split()

        x1 = int(x1Y1X2Y2[0])

        y1 = int(x1Y1X2Y2[1])

        x2 = int(x1Y1X2Y2[2])

        y2 = int(x1Y1X2Y2[3])

        result = solve(x1, y1, x2, y2)

        fptr.write(str(result) + '\n')

    fptr.close()
