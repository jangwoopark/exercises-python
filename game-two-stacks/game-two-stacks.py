#!/bin/python3

import os
import sys

def twoStacks(x, a, b):
    a.reverse()
    b.reverse()
    stack = []
    total, score = 0, 0

    while a:
        item = a.pop()
        if (total + item) <= x:
            total += item
            score += 1
            stack.append(item)
        else: break
    
    maxScore = score

    while b:
        item = b.pop()
        total += item
        score += 1
        while total > x and stack:
            total -= stack.pop()
            score -= 1
        if total <= x and score > maxScore: maxScore = score
    
    return maxScore

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input())

    for g_itr in range(g):
        nmx = input().split()

        n = int(nmx[0])

        m = int(nmx[1])

        x = int(nmx[2])

        a = list(map(int, input().rstrip().split()))

        b = list(map(int, input().rstrip().split()))

        result = twoStacks(x, a, b)

        fptr.write(str(result) + '\n')

    fptr.close()
