def dot(x, y):
    return sum(i*j for i,j in zip(x,y))
    
def pcc(x, y, n):
    num = n*dot(x,y) - sum(x)*sum(y)
    den = pow(n*dot(x,x) - pow(sum(x),2),0.5)*pow(n*dot(y,y) - pow(sum(y),2),0.5)
    return round(num/den,2)

if __name__ == '__main__':
    n = int(input())
    m = [0]*n
    p = [0]*n
    c = [0]*n
    count = 0
    for _ in range(n):
        m[count], p[count], c[count] = map(int, tuple(input().split()))
        count += 1
    
    print(pcc(m,p,n))
    print(pcc(p,c,n))
    print(pcc(c,m,n))
