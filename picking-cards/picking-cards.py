import os
import sys

def solve(c):
    c.sort(reverse=True)
    l = len(c)
    res = 1
    for i, ca in enumerate(c):
        val = l-ca
        if val <= 0:
            return 0
        res *= (val-i) 
    return res % 1000000007

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        c_count = int(input())

        c = list(map(int, input().rstrip().split()))

        result = solve(c)

        fptr.write(str(result) + '\n')

    fptr.close()
