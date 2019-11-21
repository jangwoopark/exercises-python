def oddprimefactor(n):
    c = 0
    if n % 2 == 0:
        c += 1
    while n % 2 == 0:
        n /= 2
    i = 3
    while i * i <= n:
        while n % i == 0:
            n /= i
            if i % 2 != 0:
                c += 1
        i += 1
    if n > 2:
        c += 1
    return c

for _ in range(int(input())):
    n = int(input())
    towers = list(map(int, input().split()))
    ans = list(map(oddprimefactor, towers))
    x = 0
    for i in ans:
        x ^= i
    print(2 if x == 0 else 1)
