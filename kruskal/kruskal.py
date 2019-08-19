import math
import os
import random
import re
import sys

#
# Complete the 'kruskals' function below.
#
# The function is expected to return an INTEGER.
# The function accepts WEIGHTED_INTEGER_GRAPH g as parameter.
#

#
# For the weighted graph, <name>:
#
# 1. The number of nodes is <name>_nodes.
# 2. The number of edges is <name>_edges.
# 3. An edge exists between <name>_from[i] and <name>_to[i]. The weight of the edge is <name>_weight[i].
#
#

def kruskals(g_nodes, g_from, g_to, g_weight):
    # Write your code here
    summation = 0 
    v = [1] 
    g_nodes = g_nodes - 1 
    upper_bound = max(g_weight)
    while (g_nodes!=0):
        edge_from = 0
        edge_to = 0
        index = -1
        min_wt = upper_bound
        for i in range(len(g_from)):  
            if ((g_from[i] in v) and (g_to[i] not in v)) or ((g_from[i] not in v) and (g_to[i] in v)):
                if (g_weight[i]<min_wt):
                    edge_from = g_from[i]
                    edge_to = g_to[i]
                    min_wt = g_weight[i]
                    index = i
                elif (g_weight[i] == min_wt) and (g_from[i]+g_to[i]<edge_from + edge_to):
                    edge_from = g_from[i]
                    edge_to = g_to[i]
                    index = i

        if edge_from not in v:
            v.append(edge_from)
        else:
            v.append(edge_to)
    #print(edge_from, edge_to)
        g_nodes -= 1

        summation += min_wt
        del g_from[index]
        del g_to[index]
        del g_weight[index]

    #print(summation)
    return summation

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g_nodes, g_edges = map(int, input().rstrip().split())

    g_from = [0] * g_edges
    g_to = [0] * g_edges
    g_weight = [0] * g_edges

    for i in range(g_edges):
        g_from[i], g_to[i], g_weight[i] = map(int, input().rstrip().split())

    res = kruskals(g_nodes, g_from, g_to, g_weight)

    # Write your code here.
    fptr.write(str(res))
    fptr.close()
