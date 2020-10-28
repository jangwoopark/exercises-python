import json

SERIAL = 'serial'

num_lines = int(input())
inputs = [json.loads(input()) for _ in range(num_lines)]
for line in inputs:
    del line[SERIAL]
    all_marks = line.values()
    moy = int(sum(x for x in all_marks)/4)
    result = moy
    if moy == 1:
        result = 2
    if moy == 8:
        result = 7
    print(result)
