#!/bin/python3

import os
import sys

#
# Complete the waiter function below.
#
def waiter(number, q):
    primes = []
    a=2
    while len(primes) in range(q):
        b=2
        flag=0
        for b in range(2,a):
            if a%b == 0:
                flag+=1
                break
            b=b+1
        if flag == 0:
            primes.append(a)
        a+=1
        
    output=[]
    for i in range(q):
        output.append([num for num in number[::-1] if num % primes[i] == 0])
        number = [num for num in number if num % primes[i] != 0][::-1]
  
    output.append(number)
    return [x for y in output for x in y[::-1]]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nq = input().split()

    n = int(nq[0])

    q = int(nq[1])

    number = list(map(int, input().rstrip().split()))

    result = waiter(number, q)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
