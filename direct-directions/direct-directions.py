#!/bin/python3

import os
import sys
from collections import defaultdict,deque
import bisect
p=10**9+7

def build(a,pos=1,start=1,end=None):
    end=end or n
    global tree
    if(start==end):
        tree[pos]=a[start-1]
        return
    mid=(start+end)//2
    build(a,2*pos,start,mid)
    build(a,2*pos+1,mid+1,end)
    tree[pos]=tree[2*pos]+tree[2*pos+1]

def query(l,r,pos=1,start=1,end=None):
    end=end or n
    global tree
    if(l>end or r<start):
        return(0)
    if(l<=start and r>=end):
        return(tree[pos])
    mid=(start+end)//2
    return(query(l,r,2*pos,start,mid)+query(l,r,2*pos+1,mid+1,end))

def update(x,val,pos=1,start=1,end=None):
    end=end or n
    global tree
    if(start==end):
        tree[pos]-=val
        return
    mid=(start+end)//2
    if(x<=mid):
        update(x,val,2*pos,start,mid)
    else:
        update(x,val,2*pos+1,mid+1,end)
    tree[pos]=tree[2*pos]+tree[2*pos+1]
    
t=int(input())
for _ in range(t):
    ans=0
    n=int(input())
    tree=[0]*(4*n+1)
    
    location=list(map(int,input().split()))
    population=list(map(int,input().split()))
    loc_asc=sorted(location)
    info_dict=defaultdict(lambda: [])
    
    build(loc_asc)
    
    for k,v in zip(population,location):
        info_dict[k].append(v)
    
    pos_dict={v:k for k,v in list(enumerate(loc_asc,1))}
    pop_desc=deque(sorted(list(set(population)),key=None,reverse=True))
    
    calculated=[]
    while(pop_desc):
        max_pop=pop_desc.popleft()
        while(info_dict[max_pop]):
            loc=info_dict[max_pop].pop()
            index=pos_dict[loc]
            prefix_sum=query(1,index-1)
            suffix_sum=query(index+1,n)
            before=bisect.bisect(calculated,loc)
            after=len(calculated)-before
            ans+=max_pop*(((index-1-before)*loc-prefix_sum) + (suffix_sum-(n-index-after)*loc) )
            update(index,loc)
            bisect.insort(calculated,loc)
    print(ans%p)
