def nextMove(player, board):
    growers = []
    squares = []
    g = [[4, 4], [4, 24], [24, 4], [24, 24]]
    s = [[17, 13], [17, 17], [13, 13], [13, 17], [15, 9], [15, 21],
    [9, 15], [21, 15], [15, 1], [15, 28], [15, 5], [15, 24]]
    newBoard = []
    
    #determine opponent color
    if player == 'b':
        opp = 'w'
    else:
        opp = 'b'
    
    for str in board:
        newBoard.append(list(str))
    #construct patterned coord lists from start cells
    for coord in g:
        x = coord[0]
        y = coord[1]
        l = [[x, y], [x, y-1], [x, y+1], [x-1, y]]
        growers.append(l)
    for coord in s:
        x = coord[0]
        y = coord[1]
        l = [[x, y], [x-1, y], [x-1, y-1]]
        squares.append(l)
    #build patterns
    for grower in growers:
        for cell in grower:
            if not taken(newBoard, cell[0], cell[1]):
                return cell[0], cell[1]
    for square in squares:
        for cell in square:
            if not taken(newBoard, cell[0], cell[1]):
                return cell[0], cell[1]
    
def taken(board, x, y):
    if (0 <= x <= 28 and 0 <= y <= 28):
        return board[x][y] != '-'
    else:
        return True

#Hackerrank Tail starts here
player = input()
board = []
for i in range(0, 29):
    board.append(input())
a,b = nextMove(player,board)
print (a,b)
