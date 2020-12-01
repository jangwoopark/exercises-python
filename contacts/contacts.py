import sys
from collections import defaultdict

sys.stdin.readline()
trie = defaultdict(int)

for line in sys.stdin.readlines():
    operation, payload = line.strip().split(' ')

    if operation == 'add':
        for i in range(1, len(payload) + 1):
            key = payload[0:i]
            trie[key] += 1
    elif operation == 'find':
        print(trie[payload])
