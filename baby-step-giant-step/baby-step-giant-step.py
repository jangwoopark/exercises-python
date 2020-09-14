for _ in range(int(input())):
    a, b, d = map(int, input().split())
    if d == 0:
        # rien à faire
        print(0)
    elif d == a or d == b:
        # en un coup, on y est
        print(1)
    elif d < b:
        # un triangle isocèle
        print(2)
    else:
        if d % b == 0:
            # on se déplace uniquement sur (x)
            print(d // b)
        else:
            # on se déplace sur (x) et un triangle isocèle
            print(d // b + 1)
