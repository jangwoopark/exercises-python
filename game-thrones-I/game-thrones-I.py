#!/bin/python3

import math
import os
import random
import re
import sys

def gameOfThrones(s):
    return (sum(s.count(x)%2 for x in set(s) ) <2  and 'YES') or 'NO'
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = gameOfThrones(s)

    fptr.write(result + '\n')

    fptr.close()
