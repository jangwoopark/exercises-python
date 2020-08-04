#!/bin/python3

import math
import os
import random
import re
import sys

def steadyGene(gene):
    dic = {'A':0,'T':0,'C':0,'G':0}
    for i in gene:
        dic[i]+=1
    x=len(gene)
    factor=x/4

    if dic['A']==factor and dic['T']==factor and dic['C']==factor and dic['G']==factor:
        return 0
    
    upper=0
    lower=0
    minlen=x
    while upper<x and lower<x:
        while (dic['A']>factor or dic['C']>factor or dic['T']>factor or dic['G']>factor) and upper<x:
            dic[gene[upper]]-=1
            upper+=1
        while dic['A']<=factor and dic['C']<=factor and dic['T']<=factor and dic['G']<=factor:
            dic[gene[lower]]+=1
            lower+=1
        if upper - lower < minlen :
            minlen=upper-lower+1
    return minlen

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    gene = input()

    result = steadyGene(gene)

    fptr.write(str(result) + '\n')

    fptr.close()
