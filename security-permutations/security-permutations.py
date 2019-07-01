n=int(input())
arr=list(map(int,input().split()))
list(map(lambda x:print(arr[x-1]),arr))
