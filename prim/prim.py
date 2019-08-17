import math
import os
import random
import re
import sys
import operator

# Complete the prims function below.
def prims(n, edges, start):
    #build the graph
    graph = {}
    visited = set()
    for edge in edges:
        if edge[0] not in graph:
            graph[edge[0]] = []
        graph[edge[0]].append((edge[1], edge[2]))
        if edge[1] not in graph:
            graph[edge[1]] = []
        graph[edge[1]].append((edge[0], edge[2]))
    count = 0
    node = start
    pq = []
    visited.add(start)
    
    #traverse graph to build MST
    while len(visited) < n:
        for neighbour in graph[node]:
            if neighbour[0] not in visited:
                pq.append((neighbour[0], neighbour[1]))
        #update priority queue order
        pq.sort(key=operator.itemgetter(1))
        #count the edge if first item in pq 
        #is not the current node and not prev visited
        if not node == pq[0][0] and not pq[0][0] in visited:
            count += pq[0][1]
        #set first item of priority queue to new current node
        #then remove from pq
        node = pq[0][0]
        visited.add(node)
        pq.remove((pq[0][0], pq[0][1]))

    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    edges = []

    for _ in range(m):
        edges.append(list(map(int, input().rstrip().split())))

    start = int(input())

    result = prims(n, edges, start)

    fptr.write(str(result) + '\n')

    fptr.close()
