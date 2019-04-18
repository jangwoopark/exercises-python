import re

print('\n'.join(['VALID' if re.search('^[_.]\d+[a-zA-Z]*[_]?$', input()) else 'INVALID' for _ in range(int(input()))]))
