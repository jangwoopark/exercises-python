#!/bin/python3

import os
import sys

def solve(n, k):
    max_sum = n + (n - 1)
    i_le_n = n // k
    max_no = max_sum // k 

    if k % 2 == 0:
        num1 = 0.25 * (i_le_n + 1) * i_le_n * k - i_le_n
        num2 = 0.25 * ((max_no + 1) * max_no - (i_le_n + 1) * i_le_n) * k
        num2 = n * (max_no - i_le_n) - num2
    else:
        num1 = 0.25 * (i_le_n + 1) * i_le_n * k - i_le_n + 0.25 * i_le_n
        num2 = 0.25 * ((max_no + 1) * max_no - (i_le_n + 1) * i_le_n) * k
        num2 = n * (max_no - i_le_n) - num2 + 0.25 * (max_no - i_le_n)

    print(num1, num2)
    return round(num1 + num2)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        result = solve(n, k)

        fptr.write(str(result) + '\n')

    fptr.close()
