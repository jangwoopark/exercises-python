#!/bin/python3

import os
import sys
import math
#
# Complete the downToZero function below.
#
def downToZero(n):
    memoize=set()
    count=0
    q=[]
    q.append((n,count))
    while len(q):
        data,count=q.pop(0)
        if data<=1:
            if data==1:
                count+=1
            break
        if data-1 not in memoize:
            q.append((data-1,count+1))
            memoize.add(data-1)
        sqr=int(math.sqrt(data))
        for i in range(sqr,1,-1):
            if data%i==0:
                div=max(int(data/i),i)
                if div not in memoize:
                    memoize.add(div)
                    q.append((div,count+1))
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        n = int(input())

        result = downToZero(n)

        fptr.write(str(result) + '\n')

    fptr.close()
