#!/bin/python3

import math
import os
import random
import re
import sys

def palindromeIndex(s):
    if s == s[::-1]:
        return -1
    a = list(s)
    for i in range(len(a)//2):
        if a[i] != a[len(a)-1-i]:
            a.pop(i)
            if a == a[::-1]:
                return i
            else:
                return (len(a)-i)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = palindromeIndex(s)

        fptr.write(str(result) + '\n')

    fptr.close()
