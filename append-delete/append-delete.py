#!/bin/python3

import math
import os
import random
import re
import sys

def appendAndDelete(s, t, k):
    if k >= len(s) + len(t) : return "Yes"

    i = 0 ; m = min( len(s), len(t) )
    while i < m and s[i] == t[i] : i += 1    
    d = len(s)-i + len(t)-i
        
    if k < d : return "No"
    if k == d : return "Yes"
    return "No" if (k-d)%2 else "Yes" 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()
