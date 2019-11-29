#!/bin/python3

import os
import sys

def GrudyNumber(nodes):
    if(nodes == 0 or nodes == 2):
        return 0 
    else:
        return ((nodes-1)%2+1)

def bobAndBen(trees): 
    GrudyNumers= []
    for i in range(len(trees)):
        GrudyNumers.append(GrudyNumber(trees[i][0]))
    re=GrudyNumers[0]
    print(GrudyNumers)
    if((len(GrudyNumers)-1)>1):
        for j in range(1,len(GrudyNumers)):
            re^=GrudyNumers[j]
    elif((len(GrudyNumers)-1)==1):
        re=re ^ GrudyNumers[1]
    if(re != 0): 
        return 'BOB' 
    else:
        return 'BEN'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input())

    for g_itr in range(g):
        n = int(input())

        trees = []

        for _ in range(n):
            trees.append(list(map(int, input().rstrip().split())))

        result = bobAndBen(trees)

        fptr.write(result + '\n')

    fptr.close()
