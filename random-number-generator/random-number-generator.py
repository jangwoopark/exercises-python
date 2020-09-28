import sys

def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x%y)

def prob(a,b,c):
    if a+b <= c:
        return 1,1
    if a >= c and b >= c:
        x = c * c
        y = 2 * a * b
        d = gcd(x,y)
        return x/d, y/d
    
    if a <= c and b <= c:
        x = 2* a*b -  (a - c + b)**2
        y  = 2 *a *b 
        d = gcd(x,y)
        return x/d, y/d
    
    a, b = max(a,b), min(a,b)
    x = c**2 - (c-b)**2
    y = 2 * a* b
    d = gcd(x,y)
    return x/d, y/d

n = int( input().strip() )

for i in range(n):
    a,b,c, = list(map(int, input().strip().split()))
    
    x,y = prob(a,b,c)
    print("{}/{}".format(int(x),int(y)))
