import math
import os
import random
import re
import sys

t1, t2, n = map(int, input().split())
for _ in range(2, n):
    t1, t2 = t2 + t1**2, t1
print (t2 + t1**2)
