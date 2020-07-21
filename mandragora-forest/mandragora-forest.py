t = int(input())
if 1<=t<=100000:
    while t:
        n = int(input())
        l = list(map(int,input().split()))
        l.sort()
        s,p = n,0
        m,a = 0,0
        for i in range(n):
            m += l[n-i-1]
            p = m*s
            if p>a:
                a = p
            s-=1
        print(a)
        t-=1
