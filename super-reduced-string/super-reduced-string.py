import math
import os
import random
import re
import sys

# Complete the superReducedString function below.
def superReducedString(s):
    res = []
    for c in s:
        if res and res[-1] == c:
            res.pop()
        else:
            res.append(c)
    res = ''.join(res)
    return res or "Empty String"
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = superReducedString(s)

    fptr.write(result + '\n')

    fptr.close()
