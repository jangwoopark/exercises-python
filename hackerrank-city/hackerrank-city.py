n = int(input())
valueIn = list(map(int,input().split()))
numArr = [1]
pointArr = [0]
res = [0]
distance = 0 #Cross distance between furthest points
for i in range(1,n+1):
    a = valueIn[i-1]
    num = numArr[i-1]
    pointer = pointArr[i-1]
    numArr.append((numArr[i-1]*4+2)%1000000007)
    pointArr.append((pointer*4+(2+3*num)*distance+a*(3+6*num+2*num))%1000000007)
    res.append((res[i-1]*4+pointer*(numArr[i]-num)*4+(6*num*2+1)*a+num*num*16*a)%1000000007)
    distance = (distance * 2 + 3 * a) % 1000000007
#print(numArr)
#print(pointArr)
print(res[-1]%1000000007)
