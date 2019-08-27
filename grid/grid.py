import math
import os
import random
import re
import sys

# Complete the gridChallenge function below.
def gridChallenge(grid):
    sgrid = [sorted(row) for row in grid]
    for col in zip(*sgrid):
        if any(ord(col[i+1]) < ord(v) for i,v in enumerate(col[:-1])):
            return 'NO'
    return 'YES' 
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        grid = []

        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)

        result = gridChallenge(grid)

        fptr.write(result + '\n')

    fptr.close()
