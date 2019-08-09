import math
import os
import random
import re
import sys

def floyd(g,n):
    vertices = range(n)
    d = g
    for v2 in vertices:
        tv2 = d[v2]
        for v1 in vertices:
            if d[v1][v2] is None: continue
            tv1= d[v1]
            tt = tv1[v2]
            for v3 in vertices:
                if tv2[v3] is None: continue
                ttt = tt + tv2[v3]
                if tv1[v3] is None or ttt < tv1[v3]:
                    tv1[v3] = ttt
    return d

if __name__ == '__main__':
    road_nodes, road_edges = map(int, input().split())
    g=[[None for j in range(road_nodes)] for i in range(road_nodes)]
    for i in range(road_nodes):
        g[i][i] = 0
    road_from = [0] * road_edges
    road_to = [0] * road_edges
    road_weight = [0] * road_edges

    for i in range(road_edges):
        road_from[i], road_to[i], road_weight[i] = map(int, input().split())
        g[road_from[i]-1][road_to[i]-1] = road_weight[i]

    d = floyd(g, road_nodes)

    q = int(input())

    for q_itr in range(q):
        xy = input().split()

        x = int(xy[0])

        y = int(xy[1])

        t = d[x-1][y-1]
        if t is None:
            print(-1)
        else:
            print(t)
