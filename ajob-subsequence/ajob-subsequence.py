
#!/usr/bin/env python3


def inv(n):
    return pow(n,P-2,P)


def fact_val(n):
    q = P
    v = 0
    while q<=n:
        v += n//q
        q *= P
    return v

def fact(n):
    if n<P:
        return Fact[n]
    q,r = divmod(n,P)
    return (pow(Fact[P-1],q,P) * fact(q) * Fact[r]) % P

def binom(n,p):
    assert 0<=p<=n
    A = (fact(n) * inv((fact(p)*fact(n-p))%P)) % P
    v = fact_val(n) - fact_val(p) - fact_val(n-p)
    return 0 if v>0 else A

if __name__=='__main__':
    T = int(input())
    for _ in range(T):
        N,K,P = map(int,input().split())
        Fact = [1]*P
        for i in range(2,P):
            Fact[i] = (Fact[i-1]*i) % P
        print(binom(N+1,K+1))
