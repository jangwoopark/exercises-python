#!/bin/python3

import os
import sys

from bisect import bisect_left,bisect_right
parents = {}
rep = {}
def make_set(n):
    global parents,rep
    parents=dict(list(zip(list(range(1,n+1)),list(range(1,n+1)))))
    rep=dict(list(zip(list(range(1,n+1)),({i} for i in range(1,n+1)))))
def add_edge(x, y,paths,w):
    xroot = find(x)
    yroot = find(y)
    paths[w]+=len(rep[xroot])*len(rep[yroot])
    if xroot == yroot:
        return
    else:
        if len(rep[yroot])<len(rep[xroot]):
            parents[yroot] = xroot
            rep[xroot].update(rep[yroot])
            del rep[yroot]
        else:
            parents[xroot] = yroot
            rep[yroot].update(rep[xroot])
            del rep[xroot]

def find(x):
    if parents[x] != x:
        parent = find(parents[x])
        parents[x] = parent
    return parents[x]
def solve(tree, queries):
    n = len(tree)+1
    tree.sort(key=lambda e:e[2])
    paths = {0:0}
    weights = [0]
    prev = 0   
    make_set(len(tree)+1)
    for a,b,w in tree:
        if w != prev:
            weights.append(w)
            paths[w] = paths[prev]
        add_edge(a,b,paths,w)
        prev=w
    for l,r in queries:
        wr = weights[bisect_right(weights,r)-1]
        wl = weights[bisect_right(weights,l-1)-1]
        yield paths[wr]-paths[wl]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nq = input().split()

    n = int(nq[0])

    q = int(nq[1])

    tree = []

    for _ in range(n-1):
        tree.append(list(map(int, input().rstrip().split())))

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = solve(tree, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
