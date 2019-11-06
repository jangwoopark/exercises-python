#!/bin/python3

import math
import os
import random
import re
import sys
import collections

# Complete the kFactorization function below.
def kFactorization(n, A):
    parents_of = bfs(n, A)
    if 1 not in parents_of:
            return [-1]

    v = 1
    path = []
    while True:
            path.append(str(v))
            if v == n:
                    break
            v = min(parents_of[v])

    return path

def bfs(n, A):
    parents_of = dict()
    q = collections.deque()
    q.append(n)
    while q:
        num_elements_at_this_depth = len(q)
        first_seen_at_this_depth = set()

        for i in range(num_elements_at_this_depth):
            v = q.popleft()
            if v == 1:
                    break
            for a in A:
                if v % a == 0:
                    u = v // a
                    if u not in parents_of:
                        first_seen_at_this_depth.add(u)
                        parents_of[u] = []
                        q.append(u)

                    if u in parents_of and u in first_seen_at_this_depth:
                        parents_of[u].append(v)


    return parents_of

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    A = list(map(int, input().rstrip().split()))

    result = kFactorization(n, A)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
