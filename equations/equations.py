primes = []
sieve = [True] * 1000001
for n in range(2, 1000001):
    if sieve[n]:
        primes.append(n)
        
        for i in range(2 * n, 1000001, n):
            sieve[i] = False


n = int(input())
r = 1
for p in primes:
    ep = 0
    i = p
    while True:
        e = n // i
        if e == 0:
            break
        ep += e
        i *= p
    r *= (2 * ep + 1)
    r %= 1000007
print(r)
