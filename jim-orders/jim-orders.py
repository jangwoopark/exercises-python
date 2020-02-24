#!/bin/python3

import math
import os
import random
import re
import sys

def jimOrders(orders):

    orders = list(enumerate(orders))

    orders.sort(key=lambda x:x[1][0] + x[1][1])

    return [i[0]+1 for i in orders]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    orders = []

    for _ in range(n):
        orders.append(list(map(int, input().rstrip().split())))

    result = jimOrders(orders)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
