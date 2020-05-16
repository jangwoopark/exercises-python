#!/bin/python3

import os
import sys

mat_mult = lambda A, B: [[sum(map(int.__mul__, row, col)) % 1000000007 for col in zip(*B)] for row in A]
mat_pow = lambda A, n: A if n == 1 else mat_mult(A, A) if n == 2 else mat_mult(mat_pow(mat_pow(A, n // 2), 2), A) if n % 2 else mat_pow(mat_pow(A, n // 2), 2)
print("\n".join(map(lambda a, b, n: str(mat_mult(mat_pow([[0, 1], [1,1]], n),[[a],[b]])[0][0]), *zip(*(map(int, input().split()) for _ in range(int(input())))))))
