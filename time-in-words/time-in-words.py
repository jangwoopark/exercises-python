import math
import os
import random
import re
import sys

# Complete the timeInWords function below.
def timeInWords(h, m):
    if m > 30:
        h += 1
        m = m - 60
    nums = ('~!@#', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty', 'twenty one', 'twenty two', 'twenty three', 'twenty four', 'twenty five', 'twenty six', 'twenty seven', 'twenty eight', 'twenty nine', '*&^%$')
    w = {0 : "%s minutes"%nums[abs(m)], 1 : "one minute", 15 : "quarter", 30 : "half"}
    _ = '' if m == 0 else " past " if m > 0 else " to "
    if m == 0:
        return nums[h] + " o' clock"
    else:
        return w[abs(m) * int(abs(m) in (0,1, 15, 30))] + _ + nums[h]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = int(input())

    m = int(input())

    result = timeInWords(h, m)

    fptr.write(result + '\n')

    fptr.close()
