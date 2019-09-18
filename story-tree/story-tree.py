import os
import sys
from collections import defaultdict, deque
from fractions import Fraction

def fillParent(source, parent, graph):
    stack = deque([source])
    while stack:           
        n = stack.pop()
        for adj in graph[n]:
            if adj not in parent:
                parent[adj] = n
                stack.append(adj)

def score(guesses, parent):
    score = 0
    for guess in guesses:
        guess_parent = guess[0]
        guess_child = guess[1]
        if parent[guess_child] is guess_parent:
            score += 1
    return score

def simplify(frac):
    if frac[0] == 0:
        return Fraction()
    if frac[0] >= frac[1]:
        return Fraction(1)
    simplified = Fraction(frac[0], frac[1])
    return str(simplified.numerator) + "/" + str(simplified.denominator)

#
# Complete the storyOfATree function below.
#
def storyOfATree(n, edges, k, guesses):
    #
    # Write your code here.
    #
    
    # create undirected graph
    g = defaultdict(list)
    for edge in edges:
        u = edge[0]
        v = edge[1]
        if v not in g[u]:
            g[u].append(v)
        if u not in g[v]:
            g[v].append(u)
    
    # store possible wins
    possible_wins = 0
    
    #iterate through every node being source
    for node in range(1, n + 1):
        s = node            # source
        parent = [None] * (n + 1)
        fillParent(s, parent, g)
        currScore = score(guesses, parent)
        if currScore >= k:
            possible_wins += 1
            
    possibility = simplify([possible_wins, n])

    return possibility

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        n = int(input())

        edges = []

        for _ in range(n-1):
            edges.append(list(map(int, input().rstrip().split())))

        gk = input().split()

        g = int(gk[0])

        k = int(gk[1])

        guesses = []

        for _ in range(q):
            guesses.append(list(map(int, input().rstrip().split())))

        result = storyOfATree(n, edges, k, guesses)

        fptr.write(result + '\n')

    fptr.close()
