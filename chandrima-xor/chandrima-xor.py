fibList = [1, 1]
while fibList[-1] < 10**18:
    fibList.append(fibList[-1] + fibList[-2])

def presentationAsFibonacci(n):
    from bisect import bisect_right
    num = 0
    while True:
        pos = bisect_right(fibList, n) - 1
        if n <= 0:
            break

        num += 1 << (pos - 1)
        n -= fibList[pos]

    return num

input()
res = 0
for i in list(map(int, input().split())):
    res ^= presentationAsFibonacci(i)
print (res % (10**9 + 7))
