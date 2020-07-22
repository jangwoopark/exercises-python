primecount =[False for i in range(300000)]
count = 0
P = [0 for _ in range(300000)]
for i in range(2,300000):
    if primecount[i] == False:
        count += 1
        P[i] = count
        for j in range(i,300000,i):
            primecount[j] = True
    else:
        P[i] = count

dp = [0 for i in range(41)]
dp[1] = dp[2] = dp[3] = 1
dp[4] = 2
for _ in range(5,41):
    dp[_] = dp[_-1]+dp[_-4]
n = int(input())

for i in range(n):
    m = int(input())
    print (P[dp[m]])
