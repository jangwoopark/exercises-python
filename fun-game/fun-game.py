for _ in range(eval(input())):
    n,a,b = eval(input()),list(map(int, input().split())),list(map(int, input().split()))
    s = [a[x] + b[x] for x in range(n)]
    add = c = 0
    for i in range(n):
        index = s.index(max(s))
        if c == 0: add += a[index]
        if c == 1: add -= b[index]
        s.pop(index)
        a.pop(index)
        b.pop(index)
        c = 1 - c
    if add > 0: print("First")
    elif add < 0: print("Second")
    else: print("Tie")
