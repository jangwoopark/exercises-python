import os
import sys

def hung(i,s):
    for x in E[i]:
        if F[x]!=s:
            F[x]=s
            if B[x]==-1 or hung(B[x],s):
                B[x]=i
                return 1
    return 0

for _ in range(int(input().strip())):
    N,K = map(int,input().strip().split(' '))
    D,F,B = [int(x) for x in input().strip().split()],[-1]*N,[-1]*N
    E = [list(filter(lambda j:abs(D[j]-D[i])>=K,range(i+1,N))) for i in range(N)]
    print(N - sum(map(lambda i :hung(i,i),range(N))))
