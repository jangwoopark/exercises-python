def nextMove(posr, posc, board):
    board_dim = len(board)
    shortest_dist = 2*board_dim
    shortest_pos = [board_dim, board_dim]
    
    for y in range(board_dim):
        for x in range(board_dim):
            if board[y][x] == 'd':
                Manhattan_dist = abs(y - posr) + abs(x - posc) # Manhattan Distance
                if Manhattan_dist < shortest_dist:
                    shortest_dist = Manhattan_dist
                    shortest_pos = [y, x]

    h_steps = shortest_pos[1] - posc
    v_steps = shortest_pos[0] - posr
        
    if h_steps > 0:
        print ('RIGHT')
    elif h_steps < 0:
        print ('LEFT')
    elif v_steps < 0:
        print ('UP')
    elif v_steps > 0:
        print ('DOWN')
    elif h_steps == 0 and v_steps == 0 and board[posr][posc] == 'd':
        board[posr][posc] = '-'
        print ('CLEAN')
    else:
        pass
if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    nextMove(pos[0], pos[1], board)
