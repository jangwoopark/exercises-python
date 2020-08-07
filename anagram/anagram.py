#!/bin/python3

import math
import os
import random
import re
import sys

def anagram(s):
    if(len(s) % 2 != 0):return -1
    a = s[:len(s)//2]
    b = list(s[len(s)//2:])
    ans = 0
    for var in a:
        if(var in b):
            b.remove(var) 
        else:ans += 1
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = anagram(s)

        fptr.write(str(result) + '\n')

    fptr.close()
