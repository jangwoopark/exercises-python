import math
import os
import random
import re
import sys
from collections import defaultdict

def journeyToMoon(n, astronaut):
    d=defaultdict(list)
    ans=int(n*(n-1)/2)
    for i,k in astronaut:
        d[i].append(k)
    for k,v in d.items():
        if len(v)>1:
            ans=ans-math.factorial(len(v))-1
        else:
            ans=ans-1
    return ans
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    np = input().split()

    n = int(np[0])

    p = int(np[1])

    astronaut = []

    for _ in range(p):
        astronaut.append(list(map(int, input().rstrip().split())))

    result = journeyToMoon(n, astronaut)

    fptr.write(str(result) + '\n')

    fptr.close()
