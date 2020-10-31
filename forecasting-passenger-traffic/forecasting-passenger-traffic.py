from fileinput import input
import numpy as np

months = []
values = []

d = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[], 8:[], 9:[], 10:[], 11:[]}

N = None
 
for line in input():
    if N is None:
        N = line
    else:
        line = line.rstrip()
        line = line.split()
        month = int(line[0].split("_")[-1]) % 12
        months.append(month)
        value = int(line[-1])
        values.append(value)
        d[month].append(value)

last_month = months[-1]
for i in range(1, 13):
    m = (last_month + i) % 12
    print(int(np.mean(d[m])))
