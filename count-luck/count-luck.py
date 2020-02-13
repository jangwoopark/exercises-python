#!/bin/python3

import math
import os
import random
import re
import sys

decisions = 0

def findPath(matrix, row, col, visited):
    if (matrix[row][col] == '*'):
        return True
    
    possibleMoves = []
    visited.append([row, col])
    
    if (row > 0):
        if (matrix[row-1][col] != 'X') and ([row-1, col] not in visited):
            possibleMoves.append([row-1, col])
    if (row < len(matrix) - 1):
        if (matrix[row+1][col] != 'X') and ([row+1, col] not in visited):
            possibleMoves.append([row+1, col])
    if (col > 0):
        if (matrix[row][col-1] != 'X') and ([row, col-1] not in visited):
            possibleMoves.append([row, col-1])
    if (col < len(matrix[0]) - 1):
        if (matrix[row][col+1] != 'X') and ([row, col+1] not in visited):
            possibleMoves.append([row, col+1])
            
    if (len(possibleMoves) == 0):
        return False        
        
    for pos in possibleMoves:
        if(findPath(matrix, pos[0], pos[1], visited)):
            if (len(possibleMoves) > 1):
                global decisions
                decisions += 1
            return True

def countLuck(matrix, k):
    visited = []
    row = 0
    col = 0
    stop = False
    
    for i in range(len(matrix)):
        if (stop):
            break
        for j in range(len(matrix[0])):
            if (matrix[i][j] == 'M'):
                row = i
                col = j
                stop = True
                break
    
    findPath(matrix, row, col, visited)
    
    global decisions
    if (decisions == k):
        decisions = 0
        return "Impressed"
    else:
        decisions = 0
        return "Oops!"
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nm = input().split()

        n = int(nm[0])

        m = int(nm[1])

        matrix = []

        for _ in range(n):
            matrix_item = input()
            matrix.append(matrix_item)

        k = int(input())

        result = countLuck(matrix, k)

        fptr.write(result + '\n')

    fptr.close()
