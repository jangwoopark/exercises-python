for _ in range(int(input())):
    n1 = int(input()) + 1
    y = sorted(map(int, input().split()))
    v = 0
    prev = 0
    for i, yi in enumerate(y):
        if yi != prev:
            prev = yi
            vi = n1 / (n1 - i)
        v += vi
    print("{:.2f}".format(v))
