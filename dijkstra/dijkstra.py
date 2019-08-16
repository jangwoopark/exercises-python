import sys

def dijkstra(G, s, n):

    dist = [sys.maxsize] * (n + 1)
    visited = [False] * (n + 1)
    dist[s] = 0

    while True:
        u = -1
        sd = sys.maxsize
        for v in range(1, n + 1):
            if dist[v] < sd and visited[v] == False:
                u = v
                sd = dist[v]
        if u == -1: return dist
        visited[u] = True
        for v in G[u]:
            w = G[u][v]
            newLen = dist[u] + w
            if newLen < dist[v]:
                dist[v] = newLen

    return dist

if __name__=="__main__":
    T = int(input().strip())
    for tt in range(T):
        n, m = map(int, input().strip().split())
        G = {}
        for nn in range(n + 1): G[nn] = {}
        for mm in range(m):
            a, b, c = map(int, input().strip().split())
            try:
                if G[a][b] > c:
                    G[a][b] = G[b][a] = c
            except:
                G[a][b] = G[b][a] = c
        s = int(input().strip())
        dist = dijkstra(G, s, n)
        for index in range(1, len(dist)):
            if index == s: continue
            print(dist[index] if dist[index] != sys.maxsize else -1, end=' ')
        print()
