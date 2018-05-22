import re
n = int(input())

for _ in range(n):
    if re.search(r'^[A-Z]{5}[0-9]{4}[A-Z]$', input()):
        print('YES')
    else:
        print('NO')
