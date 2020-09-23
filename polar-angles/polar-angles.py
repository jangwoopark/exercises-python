from math import pi, atan2
print("\n".join(map("{} {}".format, *zip(*sorted((list(map(int,input().split())) for _ in range(int(input()))), key=lambda x: (atan2(x[1], x[0]) % (2 * pi), x[0] ** 2 + x[1] ** 2))))))
