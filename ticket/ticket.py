# Enter your code here. Read input from STDIN. Print output to STDOUT

# getting input data
ppl, numCounters, numDests = list(map(int, input().split(' ')))
destPrices = {}
pplDests = {}
for i in range(numDests):
    a, b = input().split(' ')
    destPrices[a] = int(b)
for i in range(ppl):
    dest = input()
    pplDests[i] = dest

#print(pplDests)
# processing
# first person always goes to counter 1
buyCounters = [1]
costs = [destPrices[pplDests[1]]]
cntrDests = {}
cntrDests[pplDests[1]] = 1
curCnt = 1
pplCnt = 1

# initially fill counters with destinations
while True:
    if pplCnt >= ppl:
        break
    while pplDests[pplCnt] in cntrDests:
        #print('person',pplCnt,pplDests[pplCnt],'counter',cntrDests[pplDests[pplCnt]])
        buyCounters.append(cntrDests[pplDests[pplCnt]])
        costs.append(destPrices[pplDests[pplCnt]]*0.8)
        pplCnt += 1
        if pplCnt >= ppl:
            break
    if pplCnt >= ppl:
            break
    if pplDests[pplCnt] not in cntrDests:
        if len(cntrDests) < numCounters:
            curCnt += 1
        else:
            reservedCntrs = []
            for i in range(pplCnt+1, pplCnt+1+numCounters): # look forward in pplDests for match in cntrDests
                if i >= ppl:
                    break
                if pplDests[i] in cntrDests:
                    reservedCntrs.append(buyCounters[cntrDests[pplDests[i]]])
            for i in buyCounters:
                if i not in reservedCntrs:
                    curCnt = i
        cntrDests[pplDests[pplCnt]] = curCnt
        buyCounters.append(curCnt)
        costs.append(destPrices[pplDests[pplCnt]])
        #print('not in cntrdests', 'person',pplCnt,pplDests[pplCnt],'counter',cntrDests[pplDests[pplCnt]])
        pplCnt += 1

print(round(sum(costs),2))
for cntr in buyCounters:
    print(cntr)
