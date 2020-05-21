#!/bin/python3

import os
import sys
import math
from fractions import Fraction

def solve(n):
    divisors = [1]
    for i in range(2, int(math.sqrt(n))+1):
        if n%i == 0:
            divisors.append(i)
            if(n//i != i):
                divisors.append(n//i)
    divisors.sort()
    count = 0
    for i in divisors:
        if i%2==0 and math.sqrt(i)==math.ceil(math.sqrt(i)):
            count+=1
    if count == 0:
        return "0"
    else:
        return str(Fraction(count,len(divisors)))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = solve(n)

        fptr.write(result + '\n')

    fptr.close()
