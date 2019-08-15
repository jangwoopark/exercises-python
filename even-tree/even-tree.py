import math
import os
import random
import re
import sys

# Complete the evenForest function below.
def evenForest(t_nodes, t_edges, t_from, t_to):
    children_count = dict()
    length_list = []
 
    
    for index, value in enumerate(t_from):
        goes_to = t_to[index]
        if children_count.get(goes_to):
            children_count[goes_to].append(value)
        else:
            children_count[goes_to] = [value]
            
    for key, value in children_count.items():
        for x in value:
            if children_count.get(x):
                children_count[key] += children_count[x]
        
    for key, value in children_count.items():
        length_list.append(len(value)+1)
      
        
    length_list = sorted(length_list)
    length_list = [x for x in length_list if x % 2 == 0]
    
    
    
    return len(length_list)-1
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t_nodes, t_edges = map(int, input().rstrip().split())

    t_from = [0] * t_edges
    t_to = [0] * t_edges

    for i in range(t_edges):
        t_from[i], t_to[i] = map(int, input().rstrip().split())

    res = evenForest(t_nodes, t_edges, t_from, t_to)

    fptr.write(str(res) + '\n')

    fptr.close()
