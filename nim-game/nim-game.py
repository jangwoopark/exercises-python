from functools import reduce

for _ in range(int(input())):
    _, lis = input(), list(map(int,input().split()))
    print("Second" if reduce(lambda a,b:a^b, lis)==0 else "First")
