#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the gameOfStones function below.
def gameOfStones(n):
    if (n%7 not in [0,1] ):
        return "First"
    else:
        return "Second"
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = gameOfStones(n)

        fptr.write(result + '\n')

    fptr.close()
