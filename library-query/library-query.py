class BinaryIndexedTree2D:

    def __init__(self,max_x=10000):
        self.x_max = 10000
        self.y_max = 1000
        self.tree = [[0 for i in range(self.y_max + 5)] for j in range(self.x_max + 5)]

    def update(self, x, y, val):
        while x <= self.x_max:
            y1 = y
            while y1 <= self.y_max:
                self.tree[x][y1] += val
                y1 += (y1 & -y1)
            x += (x & -x)

    def getFrequency(self, x, y):
        sum_ = 0
        while x > 0:
            y1 = y
            while y1 > 0:
                sum_ += self.tree[x][y1]
                y1 -= (y1 & -y1)
            x -= (x & -x)
        return sum_


def solve(t, l, r, k):
    low = 1
    high = t.y_max
    ans = -1
    while low <= high:
        mid = (low + high) // 2
        v2 = t.getFrequency(r, mid)
        v1 = t.getFrequency(l - 1, mid)
        if v2 - v1 >= k:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans


s = ''

for _ in range(int(input())):
    n = int(input())
    tree = BinaryIndexedTree2D(n)

    no_books=[0] +list(map(int, input().split()))
    for i in range(1, n+1):
        tree.update(i, no_books[i], 1)

    q = int(input())
    for i in range(q):
        query = list(map(int, input().split()))
        t = query[0]
        if t == 0:
            x, y, k = query[1:]
            res = solve(tree, x, y, k)
            s += str(res) + '\n'
        else:
            x, k = query[1:]
            tree.update(x, no_books[x], -1)
            no_books[x] = k
            tree.update(x, no_books[x], 1)
    

print(s)
