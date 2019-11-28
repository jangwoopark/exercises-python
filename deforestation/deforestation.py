from collections import defaultdict
from queue import Queue

def readGraph():
    graph = defaultdict(set)
    for i in range(eval(input()) - 1):
        v1, v2 = list(map(int, input().split()))
        graph[v1].add(v2)
        graph[v2].add(v1)

    return dict(graph)

def createRootedTree(tree, root):
    rootedTree, frontier, checked = defaultdict(list), Queue(), {root}
    frontier.put(root)
    while not frontier.empty():
        v = frontier.get()
        for i in tree[v]:
            if i not in checked:
                rootedTree[v].append(i)
                checked.add(i)
                frontier.put(i)

    return dict(rootedTree)

def green_hackenbush(tree, node):
    res = 0
    if node in tree:
        for child in tree[node]:
            res ^= 1 + green_hackenbush(tree, child)
    return res

for i in range(eval(input())):
    tree = readGraph()
    rooted_tree = {} if 1 not in tree else createRootedTree(tree, 1)
    print("Alice" if green_hackenbush(rooted_tree, 1) != 0 else "Bob")
