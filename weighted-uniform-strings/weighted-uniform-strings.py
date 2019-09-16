import math
import os
import random
import re
import sys

# Complete the weightedUniformStrings function below.
def weightedUniformStrings(s, queries):
    t=s[0]
    acc=-(ord(t) - 96)
    tot={}
    for i in s:
        if i ==t:
            acc+=ord(i) - 96
            tot[ord(i) - 96+acc if i != 0 else ord(i) - 96]=0
        else:
            acc=0
            tot[ord(i) - 96+acc]=0
        t=i
    return ['Yes' if i in tot else 'No' for i in queries] 
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input())
        queries.append(queries_item)

    result = weightedUniformStrings(s, queries)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
