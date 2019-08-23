import math
import os
import random
import re
import sys

#
# Complete the 'getWays' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. LONG_INTEGER_ARRAY c
#
memoizing_dict = {}
def getWays(n, c):
    # Write your code here
    global memoizing_dict
    if n < 0:
        return 0
    elif n == 0:
        return 1
    elif (n,len(c)) in memoizing_dict.keys():
        return memoizing_dict[(n,len(c))]
    else:
        cum_sum = 0
        for c_index in range(len(c)):
            c_item = c[c_index]
            if c_item > n:
                continue
            else:
                result = getWays(n-c_item, c[c_index:])
                if result > 0:
                    cum_sum += result
        memoizing_dict[(n,len(c))] = cum_sum
        return cum_sum
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    c = list(map(int, input().rstrip().split()))

    # Print the number of ways of making change for 'n' units using coins having the values given by 'c'

    ways = getWays(n, c)

    fptr.write(str(ways) + '\n')

    fptr.close()
