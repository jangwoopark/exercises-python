#!/bin/python3

import os
import sys

def solve(a, b):
    answer = 2
    while a:
        answer = (answer ** 2) % b
        a -= 1
    return answer
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    result = solve(a, b)

    fptr.write(str(result) + '\n')

    fptr.close()
