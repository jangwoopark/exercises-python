def nextMove(n,r,c,grid):
    princess = []
    for i in range(0,n):
        for j in range(0, n):
            if(grid[i][j] == 'p'):
                princess = [i,j]
    
    delta_row = princess[0] - r
    delta_col = princess[1] - c
    if(delta_row > 0):
        return "DOWN"
    elif(delta_row < 0):
        return "UP"
    elif(delta_col > 0):
        return "RIGHT"
    elif(delta_col < 0):
        return "LEFT"
    return "PRINCESS FOUND"

n = int(input())
r,c = [int(i) for i in input().strip().split()]
grid = []
for i in range(0, n):
    grid.append(input())

print(nextMove(n,r,c,grid))
