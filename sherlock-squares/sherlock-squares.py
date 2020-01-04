#!/bin/python3

import math
import os
import random
import re
import sys

def squares(a, b):
    if(math.sqrt(a)==int(math.sqrt(a))):
        a= int(math.sqrt(a))
    else:
        a=int(math.sqrt(a))+1
    if(math.sqrt(b)==int(math.sqrt(b))):
        b=int(math.sqrt(b))+1
    else:
        b=int(math.sqrt(b))+1
    
    return b-a
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        ab = input().split()

        a = int(ab[0])

        b = int(ab[1])

        result = squares(a, b)

        fptr.write(str(result) + '\n')

    fptr.close()
