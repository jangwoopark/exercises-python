#!/bin/python3

import math
import os
import random
import re
import sys

def makingAnagrams(s1, s2):
    k=[c for c in s1]
    l=list()
    for m in s2:
        if m in k:
            k.remove(m)
        else:
            l.append(m)
    
    
    return (len(k)+len(l))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = makingAnagrams(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()
