#!/bin/python3

import math
import os
import random
import re
import sys

from collections import deque
def bfs(matrix,i,j,visited,count):
    q=deque()
    q.append((i,j))
    while q:
        i,j = q.popleft()
        count+=1
        if i+1<len(matrix) and (i+1,j) not in visited and matrix[i+1][j]==1 :
            q.append((i+1,j))
            visited.add((i+1,j))
        if j+1<len(matrix[0]) and (i,j+1) not in visited and matrix[i][j+1]==1:
            q.append((i,j+1))
            visited.add((i,j+1))
        if i-1>=0 and (i-1,j) not in visited and matrix[i-1][j]==1:
            q.append((i-1,j))
            visited.add((i-1,j))
        if j-1>=0 and (i,j-1) not in visited and matrix[i][j-1]==1:
            q.append((i,j-1))
            visited.add((i,j-1))

        if i-1>=0 and j+1<len(matrix[0]) and (i-1,j+1) not in visited and matrix[i-1][j+1]==1 :
            q.append((i-1,j+1))
            visited.add((i-1,j+1))
        if i+1<len(matrix) and j-1>=0 and (i+1,j-1) not in visited and matrix[i+1][j-1]==1:
            q.append((i+1,j-1))
            visited.add((i+1,j-1))
        if i-1>=0 and j-1>=0 and  (i-1,j-1) not in visited and matrix[i-1][j-1]==1:
            q.append((i-1,j-1))
            visited.add((i-1,j-1))
        if i+1<len(matrix) and j+1<len(matrix[0]) and (i+1,j+1) not in visited and matrix[i+1][j+1]==1:
            q.append((i+1,j+1))
            visited.add((i+1,j+1))
    # print(visited)
    return count

def connectedCell(matrix):
    #use bfs
    visited=set()
    max_area= 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            count = 0
            if (i,j) not in visited and matrix[i][j]==1:
                visited.add((i,j))
                max_area = max(max_area, bfs(matrix,i,j,visited,count))
    return max_area

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    m = int(input())

    matrix = []

    for _ in range(n):
        matrix.append(list(map(int, input().rstrip().split())))

    result = connectedCell(matrix)

    fptr.write(str(result) + '\n')

    fptr.close()
