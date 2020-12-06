#!/bin/python3

from heapq import heappop,heappush,heapify

firstLine = [int(x) for x in input().split()]
cookies = [int(x) for x in input().split()]

cookieCount = int(firstLine[0])
minSweetness = int(firstLine[1])

heapify(cookies)

fC = 0
try:
    while cookies[0] < minSweetness:
        fC+=1
        c1 = heappop(cookies)
        c2 = heappop(cookies)
        newCookie=(1*c1)+(2*c2)
        heappush(cookies,newCookie)
    print(fC)
except:
    print("-1")
