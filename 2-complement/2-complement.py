#!/bin/python3

import os
import sys

def twosCompliment(a, b):
    count = 0
    h1 = a
    h2 = b + 1
    for num in range(32):
        power = 2 ** num
        sum_a = (h1 // (power * 2)) * power + max(0, (h1 % (power * 2)) - power)
        sum_b = (h2 // (power * 2)) * power + max(0, (h2 % (power * 2)) - power)
        #print(num, sum_a, sum_b)
        count += sum_b - sum_a
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        ab = input().split()

        a = int(ab[0])

        b = int(ab[1])

        result = twosCompliment(a, b)

        fptr.write(str(result) + '\n')

    fptr.close()
