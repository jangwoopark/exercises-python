#!/bin/python3

import os
import sys


def truckTour(petrolpumps):
    fuel=0
    ll=len(petrolpumps)
    l=0
    i=l
    while i<ll:
        fuel=fuel+petrolpumps[i][0]-petrolpumps[i][1]
        if fuel<0:
            l=l+1
            i=l
            fuel=0
        else:
            i+=1
    return l

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    petrolpumps = []

    for _ in range(n):
        petrolpumps.append(list(map(int, input().rstrip().split())))

    result = truckTour(petrolpumps)

    fptr.write(str(result) + '\n')

    fptr.close()
