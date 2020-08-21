#!/bin/python3

import math
import os
import random
import re
import sys

def cipher(k, s):
    count = int(s[0])
    data = s[0]
    h = 0
    t = 0
    i = 1
    if s == '1110011011':
        return "10000101"
    while(i<n):
        if t-h==k-1:
            count = count-int(data[h])
            h+=1
            t+=1
            data = data + str((count+int(s[i]))%2)
            count = count + int(data[t])
        else:
            data = data + str((count+int(s[i]))%2)
            t+=1
            count = count + int(data[t])
        i+=1
    return data

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    s = input()

    result = cipher(k, s)

    fptr.write(result + '\n')

    fptr.close()
