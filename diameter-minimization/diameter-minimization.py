#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    # Write Your Code Here
    Matrix = [[0 for j in range(m)] for i in range(n)]
    count=0;
    for i in range(0,n):
        for j in range(0,m):
            if(count==n):
                count=0
            Matrix[i][j]=count
            count=count+1
    k=n-1
    dia=0
    while(not(k==0)):
        for i in range(0,n):
            if(k in Matrix[i]):
                k=i
                i=0
                dia=dia+1
                #print(k)
                break;
    print(dia)
    for i in range(0,n):
        print(' '.join(str(e) for e in Matrix[i]))
