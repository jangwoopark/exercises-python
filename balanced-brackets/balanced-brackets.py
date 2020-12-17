#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isBalanced function below.
def isBalanced(s):
    restart=True
    while restart:
        if '{}' in s:
            s=s.replace('{}','')
        elif '()' in s:
            s=s.replace('()','')
        elif '[]' in s:
            s=s.replace('[]','')
        else:
            restart=False
    return 'YES' if len(s)==0 else 'NO'
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
