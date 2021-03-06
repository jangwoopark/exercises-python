#!/bin/python3

import math
import os
import random
import re
import sys

def cavityMap(grid):
    for i in range(1,n-1):
        for j in range(1,n-1):
            if grid[i][j] > max(grid[i-1][j],grid[i+1][j],grid[i][j-1],grid[i][j+1]):
                grid[i] = grid[i][:j] +'X' + grid[i][j+1:]
                
    return grid
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    result = cavityMap(grid)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
