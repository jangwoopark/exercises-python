t=int(input())
while t>0:
    n=int(input())
    a=list(map(int,input().split()))
    m=min(a)
    cost=2**31

    for i in range(5):
        x=m-i
        c=0
        for j in range(len(a)):
           k=a[j]-x
           c+=k//5+k%5 //2+k%5 %2
        cost=min(cost,c)
    print(cost)
    t-=1
