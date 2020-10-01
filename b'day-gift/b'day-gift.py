#!/bin/python3

import os
import sys


def solve(balls):
    s=0
    for i in balls:
        s=s+i*0.5
    return s

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    balls_count = int(input())

    balls = []

    for _ in range(balls_count):
        balls_item = int(input())
        balls.append(balls_item)

    result = solve(balls)

    fptr.write(str(result) + '\n')

    fptr.close()
