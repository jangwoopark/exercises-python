#!/bin/python3

import functools as ft

def gcd(a,b):
    if a < b:
        a,b = b,a
    if not a % b:
        return b
    else:
        return gcd(b, a % b)

for _ in range(int(input())):
    n = int(input())
    array = [int(temp) for temp in input().split()]
    print('YES' if ft.reduce(gcd, array) == 1 else 'NO')
