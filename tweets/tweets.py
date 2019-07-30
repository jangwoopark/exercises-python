import re
n = int(input().strip())
found = 0
for _ in range(n):
    if re.search(r'hackerrank', input(), re.IGNORECASE):
        found += 1
print(found)
