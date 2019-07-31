import re, sys
for s in filter(re.compile(r"(?i:hi\s[^d])").match, sys.stdin):
    print(s)
