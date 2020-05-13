#!/bin/python3

import os
import sys
import math

def Digit_sum(n):
    s=0
    while(n>0):
        s+=n%10
        n=n//10
    return(s) 

def solve(n):
    t=n
    lst=[]
    while n%2==0:
        lst.append(2)
        n=n//2

    for i in range(3,int(math.sqrt(n))+1,2):
        while n%i==0:
            lst.append(i) 
            n=n//i

    if(n>2):
        lst.append(n)

    su=0
    for i in range(len(lst)):
        if lst[i]<=7:
            su+=lst[i]
        else:
            su+=Digit_sum(lst[i])

    s2=Digit_sum(t)
    if su==s2:
        return(1)
    else:
        return(0)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = solve(n)

    fptr.write(str(result) + '\n')

    fptr.close()
