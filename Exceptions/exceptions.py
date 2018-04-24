inputs = [input().split() for _ in range(int(input()))]
for a, b in inputs:
    try:
        print(int(a)//int(b))
    except (ValueError, ZeroDivisionError) as e:
        print('Error Code: {}'.format(e))
