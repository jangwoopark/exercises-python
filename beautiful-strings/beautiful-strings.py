import itertools
s = input()
groups = [(c, sum(1 for x in l)) for c, l in itertools.groupby(s)]
multiple = sum(x[1] > 1 for x in groups)
fence = sum(groups[i - 1][0] == groups[i + 1][0] and groups[i][1] == 1 \
            for i in range(1, len(groups) - 1))
print(multiple + len(groups) * (len(groups) - 1) // 2 - fence)
