current_player =  input()
player_pos = input().split(" ")
player_pos = list(map(int, player_pos))
rpos = [player_pos[0], player_pos[1]]
gpos = [player_pos[2], player_pos[3]]
grid_size = 15
grid = []
for gr in range(grid_size):
    grid.append(input())
    
# algorithm starts, here we are identifying how many free steps in each directions.
def get_free_grid(grid, pos):
    left = right = up = down = 0
    row, column = pos[0]-1, pos[1]
    while row > 0: # up
        if grid[row][column] == "-":
            up += 1
            row -= 1
        else:
            break
    row, column = pos[0]+1, pos[1]       
    while row < 15: #down
        if grid[row][column] == "-":
            down += 1
            row += 1
        else:
            break
    row, column = pos[0], pos[1]+1
    while column < 15: #right
        if grid[row][column] == "-":
            right += 1
            column += 1
        else:
            break
    row, column = pos[0], pos[1]-1
    while column > 0: # left
        if grid[row][column] == "-":
            left += 1
            column -= 1
        else:
            break
    return {"LEFT":left, "RIGHT":right, "UP":up, "DOWN":down}

max_free_direction = ""
max_free_value = 0
ppos = rpos if current_player == "r" else gpos
free_grids = get_free_grid(grid, ppos)

for direction in free_grids:
    if free_grids[direction] > max_free_value:
        max_free_direction, max_free_value = direction, free_grids[direction]
print(max_free_direction)
