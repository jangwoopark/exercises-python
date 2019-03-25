#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the pangrams function below.
def pangrams(s):

    p = "pangram"
    np = "not pangram"

    if len(set([i.lower() for i in s.strip()]) & set("abcdefghijklmnopqrstuvwxyz")) == 26:
        return p
    else: 
        return np

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
