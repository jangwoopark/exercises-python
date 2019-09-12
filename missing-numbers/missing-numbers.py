import math
import os
import random
import re
import sys
from collections import Counter
# Complete the missingNumbers function below.
def missingNumbers(arr, brr):
    return sorted(list((Counter(brr)-Counter(arr)).keys()))
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    m = int(input())

    brr = list(map(int, input().rstrip().split()))

    result = missingNumbers(arr, brr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
