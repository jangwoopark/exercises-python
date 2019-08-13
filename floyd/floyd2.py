n, m = tuple(int(x) for x in input().strip().split())
edges = {node: list() for node in range(1,n+1)}
for _ in range(m):
    f,t,r = tuple(int(x) for x in input().strip().split())
    try:
        idx = next(i for i,(to,_) in enumerate(edges[f]) if to == t)
        edges[f][idx] = (t,r)
    except StopIteration:
        edges[f].append((t,r))
questions = [
    tuple(int(x) for x in input().strip().split())
        for _ in range(int(input()))
]
questions_dict = dict()
for fr, to in questions:
    if fr not in questions_dict:
        questions_dict[fr] = {to}
    else:
        questions_dict[fr].add(to)
answers = dict()
for fr, tos in questions_dict.items():
    visited = {fr}
    dists = {node: -1 for node in range(1,n+1)}
    dists[fr] = 0
    while visited:
        next_visited = set()
        for node in visited:
            nd = dists[node]
            for node2,r in edges[node]:
                nw = nd+r
                if dists[node2] == -1 or nw < dists[node2]:
                    dists[node2] = nw
                    next_visited.add(node2)
        visited = next_visited
    for to in tos:
        answers[(fr,to)] = dists[to]
for fr, to in questions:
    print(answers[(fr,to)])
