#!/bin/python3

import math
import os
import random
import re
import sys

def angryChildren(n, k, packets):
    packets.sort()
    ps = [0]
    for i in range(n):
        ps.append(ps[-1] + packets[i])
    cur = 0
    for i in range(k):
        cur += i * packets[i] - ps[i]
    ans = cur
    for i in range(1, n - k + 1):
        cur -= ps[i + k - 1] - ps[i - 1] - k * packets[i - 1]
        cur += k * packets[i + k - 1] - ps[i + k] + ps[i]
        ans = min(ans, cur)
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    k = int(input())

    packets = []

    for _ in range(n):
        packets_item = int(input())
        packets.append(packets_item)

    result = angryChildren(n, k, packets)

    fptr.write(str(result) + '\n')

    fptr.close()
