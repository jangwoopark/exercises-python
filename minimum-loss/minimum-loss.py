#!/bin/python3

import math
import os
import random
import re
import sys

def minimumLoss(price):
    sorted_price = sorted(price)
    res = max(price)
    for i, p in enumerate(sorted_price[:-1]):
        loss = sorted_price[i + 1] - p
        if loss < res and price.index(p) > price.index(sorted_price[i + 1]):
          res = loss
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    price = list(map(int, input().rstrip().split()))

    result = minimumLoss(price)

    fptr.write(str(result) + '\n')

    fptr.close()
