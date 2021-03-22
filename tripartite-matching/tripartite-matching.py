#!/bin/python3

import os
import sys


def tripartiteMatching(n, g1, g2, g3):
    #data format for g1 and g2
    m1 = len(g1)
    m2 = len(g2)
    m3 = len(g3)
    e1 = [[] for x in range (0, n + 5)]
    e2 = [[] for x in range (0, n + 5)]
    ee = [[] for x in range (0, n + 5)]
    for [x, y] in g1:
        e1[x].append(y)
        e1[y].append(x)
    for [x, y] in g2:
        e2[x].append(y)
        e2[y].append(x)
    for [x, y] in g3:
        ee[x].append(y)
        ee[y].append(x)

    #add g3 to a set of edge for O(1) index
    e3 = set()
    for [x, y] in g3:
        e3.add((x, y))
        e3.add((y, x))

    #now count how many pair (a, b) (b, c) has an edge (a, c) in g3
    v1 = [0 for x in range(0, n + 5)]
    v2 = [0 for x in range(0, n + 5)]
    count = 0
    count_ll = 0;
    for i in range(1, n + 1):
        if len(e1[i]) + len(e2[i]) < 0:
            for a in e1[i]:
                for b in e2[i]:
                    if (a, b) in e3:
                        count += 1
        else:
            count_ll += 1
            for x in e1[i]:
                v1[x] = count_ll
            for x in e2[i]:
                v2[x] = count_ll

            for x in e1[i]:
                for y in ee[x]:
                    if (v1[x] == count_ll) & (v2[y] == count_ll):
                            count += 1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    m1 = int(input())

    g1 = []

    for _ in range(m1):
        g1.append(list(map(int, input().rstrip().split())))

    m2 = int(input())

    g2 = []

    for _ in range(m2):
        g2.append(list(map(int, input().rstrip().split())))

    m3 = int(input())

    g3 = []

    for _ in range(m3):
        g3.append(list(map(int, input().rstrip().split())))

    result = tripartiteMatching(n, g1, g2, g3)

    fptr.write(str(result) + '\n')

    fptr.close()
