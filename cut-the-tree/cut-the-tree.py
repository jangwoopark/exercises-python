n = int(input())
vals = list(map(int,input().split()))
t = sum(vals)

adjLi = [[] for i in range(n)]

for i in range(n-1):
    u,v = map(int,input().split())
    adjLi[u-1].append(v-1)
    adjLi[v-1].append(u-1)

totVal = [0]*n
explored = []
waiting = {i for i in range(n) if len(adjLi[i]) == 1}
while(len(waiting)):
    for i in waiting:
        totVal[i] += vals[i]
        if(len(adjLi[i])):
            adjLi[adjLi[i][0]].remove(i)
            totVal[adjLi[i][0]] += totVal[i]
    waiting = {adjLi[i][0] for i in waiting if len(adjLi[i]) and len(adjLi[adjLi[i][0]]) == 1}

rt = abs(t- 2*totVal[0])
for i in range(1,n):
    k = abs(t-2*totVal[i])
    if k < rt:
        rt = k

print(rt)
