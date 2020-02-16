def set(tree, i, val):
    while i <= N:
        tree[i] += val
        i += (i & -i)


def bit_sum(tree, i):
    res = 0
    while i > 0:
        res += tree[i]
        i -= (i & -i)

    return res


def similarity(tree, bit_tree, root):
    from collections import deque
    stack = deque()
    stack.append((root, []))

    acc = 0

    while stack:
        node, ancestors = stack.pop()

        acc += bit_sum(bit_tree, min(N, node + K)) - bit_sum(bit_tree, max(1, node - K) - 1)
        set(bit_tree, node, 1)

        children = tree[node]
        if children:
            iterchild = iter(children)
            ancestors.append(node)
            stack.append((next(iterchild), ancestors))

            for child in iterchild:
                stack.append((child, []))

        else:
            for ancestor in ancestors:
                set(bit_tree, ancestor, -1)

            set(bit_tree, node, -1)

    return acc

N, K = map(lambda x: int(x), input().split(" "))
tree = list([[] for _ in range(N + 1)])

# Get root node
root, child = map(lambda x: int(x), input().split(" "))
tree[root].append(child)

# Get tree
for _ in range(N - 2):
    line = input().split(" ")
    parent = int(line[0])
    child = int(line[1])
    tree[parent].append(child)

print(similarity(tree, [0] * (N + 1), root))
