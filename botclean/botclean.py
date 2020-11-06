def next_move(posr, posc, board):
    i, j = min(((i, j) for i, row in enumerate(board) if 'd' in row for j, c in enumerate(row) if c == 'd'), key=lambda x: abs(posr - x[0]) + abs(posc - x[1]))
    print("LEFT" if j < posc else "RIGHT" if j > posc else "UP" if i < posr else "DOWN" if i > posr else "CLEAN")
