#!/bin/python3

import math
import os
import random
import re
import sys

def strangeCounter(t):
    return(3 * 2 ** math.ceil(math.log2(t / 3 + 1)) - t - 2)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    result = strangeCounter(t)

    fptr.write(str(result) + '\n')

    fptr.close()
