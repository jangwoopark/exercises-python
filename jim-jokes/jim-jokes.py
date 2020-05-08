#!/bin/python3

import os
import sys

import collections as cl

T = int(input())
array = []
for _ in range(T):
    m,d = [int(temp) for temp in input().split()]
    if d // 10 >= m or d % 10 >= m:
        pass
    else:
        array.append((d // 10) * m + d % 10)
ans = 0
for c in cl.Counter(array).items():
    ans += c[1] * (c[1] - 1) // 2
print(ans)
