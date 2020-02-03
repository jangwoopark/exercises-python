#!/bin/python3

import math
import os
import random
import re
import sys

def activityNotifications(expenditure, d):
    k = 200
    counter = 0

    count = (k+1)*[0] #indices runs from 0 to max(array) inclusive

    for i in expenditure[:d]:
        count[i] += 1    #Initial frequency array, jth value of count is the frequency of number j

    
    if ((d % 2) == 1): #Odd frequency case
        for i in range(d,len(expenditure)):
            cumfreq = (k+1)*[0]
            cumfreq[0] = count[0]

            for j in range(1,k+1):
                cumfreq[j] += cumfreq[j-1] + count[j]
                

                if (cumfreq[j]>(d)/2):
                    median = j #first j s.t. count[j-1] < (d+1)/2 and count[j] >= (d+1)/2
                    break
                else:
                    continue
        
            if expenditure[i]>=2*median:
                counter += 1
        
            count[expenditure[i-d]] -= 1
            count[expenditure[i]] += 1

    if ((d % 2) == 0): #Even frequency case
        for i in range(d,len(expenditure)):
            cumfreq = (k+1)*[0]
            cumfreq[0] = count[0]

            m1 = None
            m2 = None

            for j in range(1,k+1):
                cumfreq[j] += cumfreq[j-1] + count[j]

                if (cumfreq[j]>=(d)/2) and (m1 is None):
                    m1 = j

                if (cumfreq[j]>=(d+1)/2):
                    m2 = j
                    median = (m1+m2)/2
                    break
                else:
                    continue

            if expenditure[i]>=2*median:
                counter += 1
        
            count[expenditure[i-d]] -= 1
            count[expenditure[i]] += 1
    

    return counter

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    fptr.write(str(result) + '\n')

    fptr.close()
