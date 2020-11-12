import copy

SOLVEDSTATE = []

k = int(input())
board = []
whereami = ()

for r in range(k):
    row = []
    solved_row = []
    for c in range(k):
        tile = int(input())
        if tile == 0:
            whereami = (r,c)
        row.append(tile)
        solved_row.append((r,c))
    board.append(row)
    SOLVEDSTATE.extend(solved_row)
    

def getMD2SolvedBoard():
    md = 0
    for row in range(k):
        for col in range(k):
            coords = SOLVEDSTATE[board[row][col]]
            md += abs(row-coords[0]) + abs(col-coords[1])
    md -= (whereami[0] + whereami[1])
    return md


def getPossibleMoves(coords):
    moves=[]
    if coords[0] > 0: moves.append('UP');
    if coords[1] > 0: moves.append('LEFT');
    if coords[1] < k-1: moves.append('RIGHT');
    if coords[0] < k-1: moves.append('DOWN');
    return moves


def updateBoard(state, move):
    r,c = state[1][0], state[1][1]
    r1,c1 = None, None
    if move == 'UP': r1 = r-1; c1 = c;
    elif move == 'LEFT': r1=r; c1=c-1;
    elif move == 'RIGHT': r1=r; c1=c+1;
    elif move == 'DOWN': r1=r+1; c1=c;
    new_board = copy.deepcopy(state[0])
    temp = new_board[r1][c1]
    new_board[r1][c1] = 0
    new_board[r][c] = temp
    return new_board
    
def bisect_sorted_list(node):
    lo=0
    hi=len(todo)
    while lo < hi:
        mid = (lo+hi)//2
        if node[5] < todo[mid][5]: lo = mid+1
        else: hi = mid
    todo.insert(lo, node)
    
def hashBoard(b):
    string = ''
    for r in b:
        for c in r:
            string += str(c)
    return string

def addMoves(cur_state):
    cur_board = cur_state[0]
    r,c = cur_state[1][0], cur_state[1][1]
    new_depth = cur_state[3]+1
    old_dist = cur_state[4]
    for m in getPossibleMoves(cur_state[1]):
        diff=0
        new_board = None
        move = None
        coords = None
        if m=='UP':
            if SOLVEDSTATE[cur_board[r-1][c]][0] >= r: diff = -1;
            else : diff = 1;
            move = 'UP'
            coords = (r-1, c)
        elif m=='LEFT':
            if SOLVEDSTATE[cur_board[r][c-1]][1] >= c: diff = -1;
            else : diff = 1;
            move = 'LEFT'
            coords = (r, c-1)
        elif m=='RIGHT':
            if SOLVEDSTATE[cur_board[r][c+1]][1] <= c: diff = -1;
            else : diff = 1;
            move = 'RIGHT'
            coords = (r, c+1)
        elif m=='DOWN':
            if SOLVEDSTATE[cur_board[r+1][c]][0] <= r: diff = -1;
            else : diff = 1;
            move = 'DOWN'
            coords = (r+1, c)
            
        new_board = updateBoard(cur_state, move)
        new_board_hash = hashBoard(new_board)
        if new_board_hash not in checked:
            new_dist = old_dist+diff
            cost = new_depth+new_dist
            bisect_sorted_list((new_board, coords, move, new_depth, new_dist, cost, cur_state))
            checked.add(new_board_hash)


todo = []
dist = getMD2SolvedBoard()
depth=0
# board state, location of empty square, move, depth, dist, hueristic cost, parent node
todo.append((board, whereami, 'Start', depth, dist, dist+depth, None))
checked = set()
checked.add(hashBoard(board))
path=[]
solution_node = None
solution=[]


while True:
    nxt_move = todo.pop()
    path.append(nxt_move)
    if nxt_move[4] == 0:
        solution_node = nxt_move
        break
    addMoves(nxt_move)

    
#Get solution
node = solution_node
while node is not None:
    solution.append((node[0],node[1],node[2],node[3],node[4],node[5]))
    node = node[6]
solution = solution[-2::-1]
    
# print(len(path), '\n')
# for p in path:
#     for r in p[0]:
#         print(r, sep='\n')
#     print(p[1], p[2], p[3], p[4], p[5], '\n')
        
print(len(solution),*('{}'.format(s[2]) for s in solution), sep='\n')
