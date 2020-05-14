#!/bin/python3

import os
import sys

print ("\n".join(map(lambda x, p: "YES" if p == 2 or pow(x, (p - 1) // 2, p) != p - 1 else "NO", *zip(*(map(int, input().split()) for _ in range(int(input())))))))
