n,a,b = eval(input()),list(map(int, input().split())),0
for i in a: b ^= i
print(sum([int(i^b < i) for i in a]))
