#!/bin/python3

import math
import os
import random
import re
import sys

def biggerIsGreater(w):
    for i in range(len(w)-1)[::-1]:
        if w[i] < w[i+1]:
            for j in range(i+1,len(w))[::-1]:
                if w[i] < w[j]:
                    lis = list(w) 
                    lis[i],lis[j]=lis[j],lis[i]
                    return "".join(lis[:i+1]+lis[i+1:][::-1])
    return 'no answer'
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input())

    for T_itr in range(T):
        w = input()

        result = biggerIsGreater(w)

        fptr.write(result + '\n')

    fptr.close()
