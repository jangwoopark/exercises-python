#!/bin/python3

import math
import os
import random
import re
import sys



def dynamicArray(n, queries):
    seq = [[] for _ in range(n)]
    last_ans = 0
    res = []

    for q in queries:
        index = (q[1] ^ last_ans) % n
        
        if q[0] == 1:
            seq[index].append(q[2])
        else:
            position = q[2] % len(seq[index])
            last_ans = seq[index][position]
            res.append(last_ans)
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
