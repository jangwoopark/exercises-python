#!/bin/python3

import sys
        
# parse inputs
m,n = [int(q_temp) for q_temp in input().strip().split(' ')]
a = list()
for i in range(m):
    l = input().strip()
    a.append(l)
    
# set max perimeter to zero    
max_perim = 0
    
# iterate through each row
for i in range(m):
    # iterate through strings of '.' nested between 'x'
    if 2*(m-i-1) + 2*(n-1) < max_perim:
        continue
    # iterate through each column
    for j in range(n):
        i1 = j
        if a[i][j] == 'x' or a[i][min(j+1,n-1)] == 'x' or a[i][min(j+2,n-1)] == 'x' or j >= n - 1:
            continue
        if 2*(m-i-1) + 2*(n-j-1) < max_perim:
            continue
        i2 = n-1
        str_top = a[i][i1:i2+1]
        # iterate through various lengths of rectangle
        while i2 > i1:
            # top must not have any 'x'
            str_top = a[i][i1:i2+1]
            if str_top.count('x') == 0 and 2*(i2-i1) + 2*(m-i-1) > max_perim:
                search = True
                depth = 1
                # iterate through various depths / widths of rectangle
                while search and i+depth < m:
                    str = a[i+depth][i1:i2+1]
                    if str.count('x') == 0:
                        perim = 2*(i2-i1) + 2*depth
                        # new maximum perimeter found
                        if perim > max_perim:
                            max_perim = perim
                    # 'x' along edge - terminate search
                    if a[i+depth][i1] == 'x' or a[i+depth][i2] == 'x':
                        search = False
                    # increment depth
                    depth += 1
            # decrement length of rectangle
            i2 -= 1
# output result
if max_perim > 0:
    print(max_perim)
else:
    print('impossible')
