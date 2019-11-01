import os
import sys


def getKnightPossibleNextMoves(xy, board, isWhite):
    res = []
    x = xy[0]
    y = xy[1]
    if x > 0 and y < 2:
        if (isWhite and board[y+2][x-1].startswith('W')) \
            or (not isWhite and board[y+2][x-1].startswith('B')):
            pass
        else:
            res.append((x-1, y+2))
    if x > 0 and y > 1:
        if (isWhite and board[y-2][x-1].startswith('W')) \
            or (not isWhite and board[y-2][x-1].startswith('B')):
            pass
        else:
            res.append((x-1, y-2))
    if x > 1 and y < 3:
        if (isWhite and board[y+1][x-2].startswith('W')) \
            or (not isWhite and board[y+1][x-2].startswith('B')):
            pass
        else:
            res.append((x-2, y+1))
    if x > 1 and y > 0:
        if (isWhite and board[y-1][x-2].startswith('W')) \
            or (not isWhite and board[y-1][x-2].startswith('B')):
            pass
        else:
            res.append((x-2, y-1))
    if x < 3 and y < 2:
        if (isWhite and board[y+2][x+1].startswith('W')) \
            or (not isWhite and board[y+2][x+1].startswith('B')):
            pass
        else:
            res.append((x+1, y+2))
    if x < 3 and y > 1:
        if (isWhite and board[y-2][x+1].startswith('W')) \
            or (not isWhite and board[y-2][x+1].startswith('B')):
            pass
        else:
            res.append((x+1, y-2))
    if x < 2 and y < 3:
        if (isWhite and board[y+1][x+2].startswith('W')) \
            or (not isWhite and board[y+1][x+2].startswith('B')):
            pass
        else:
            res.append((x+2, y+1))
    if x < 2 and y > 0:
        if (isWhite and board[y-1][x+2].startswith('W')) \
            or (not isWhite and board[y-1][x+2].startswith('B')):
            pass
        else:
            res.append((x+2, y-1))
    return res


def getQueenPossibleNextMoves(xy, board, isWhite):
    return list(set(getBishopPossibleNextMoves(xy, board, isWhite) \
        + getRookPossibleNextMoves(xy, board, isWhite)))


def getBishopPossibleNextMoves(xy, board, isWhite):
    res = []
    x = xy[0]
    y = xy[1]
    for i in range(1, 4):
        if y+i > 3 or x+i > 3: break
        if (isWhite and board[y+i][x+i].startswith('W')) \
            or (not isWhite and board[y+i][x+i].startswith('B')):
            break
        else:
            res.append((x+i,y+i))
        if board[y+i][x+i] != "  ": break
    for i in range(1, 4):
        if y+i > 3 or x-i < 0: break
        if (isWhite and board[y+i][x-i].startswith('W')) \
            or (not isWhite and board[y+i][x-i].startswith('B')):
            break
        else:
            res.append((x-i,y+i))
        if board[y+i][x-i] != "  ": break
    for i in range(1, 4):
        if y-i < 0 or x+i > 3: break
        if (isWhite and board[y-i][x+i].startswith('W')) \
            or (not isWhite and board[y-i][x+i].startswith('B')):
            break
        else:
            res.append((x+i,y-i))
        if board[y-i][x+i] != "  ": break
    for i in range(1, 4):
        if y-i < 0 or x-i < 0: break
        if (isWhite and board[y-i][x-i].startswith('W')) \
            or (not isWhite and board[y-i][x-i].startswith('B')):
            break
        else:
            res.append((x-i,y-i))
        if board[y-i][x-i] != "  ": break
    return res


def getRookPossibleNextMoves(xy, board, isWhite):
    res = []
    x = xy[0]
    y = xy[1]
    for i in reversed(range(0,x)):
        if (isWhite and board[y][i].startswith('W')) \
            or (not isWhite and board[y][i].startswith('B')):
            break
        else:
            res.append((i,y))
        if board[y][i] != "  ":
            break
    for i in range(x+1,4):
        if (isWhite and board[y][i].startswith('W')) \
            or (not isWhite and board[y][i].startswith('B')):
            break
        else:
            res.append((i,y))
        if board[y][i] != "  ":
            break
    for i in reversed(range(0,y)):
        if (isWhite and board[i][x].startswith('W')) \
            or (not isWhite and board[i][x].startswith('B')):
            break
        else:
            res.append((x,i))
        if board[i][x] != "  ":
            break
    for i in range(y+1,4):
        if (isWhite and board[i][x].startswith('W')) \
            or (not isWhite and board[i][x].startswith('B')):
            break
        else:
            res.append((x,i))
        if board[i][x] != "  ":
            break
    return res


def getPossibleNextMoves(candidate, board, isWhite):
    piece = candidate[0]
    xy = posToXY(candidate[1:])
    if piece == "N":
        return getKnightPossibleNextMoves(xy, board, isWhite)
    elif piece == "Q":
        return getQueenPossibleNextMoves(xy, board, isWhite)
    elif piece == "B":
        return getBishopPossibleNextMoves(xy, board, isWhite)
    elif piece == "R":
        return getRookPossibleNextMoves(xy, board, isWhite)


def posToXY(pos):
    if   pos[0] == "A": x = 0
    elif pos[0] == "B": x = 1
    elif pos[0] == "C": x = 2
    elif pos[0] == "D": x = 3
    if   pos[1] == "1": y = 0
    elif pos[1] == "2": y = 1
    elif pos[1] == "3": y = 2
    elif pos[1] == "4": y = 3
    return (x,y)


def xyToPos(xy):
    if   xy[0] == 0: pos0 = "A"
    elif xy[0] == 1: pos0 = "B"
    elif xy[0] == 2: pos0 = "C"
    elif xy[0] == 3: pos0 = "D"
    if   xy[1] == 0: pos1 = "1"
    elif xy[1] == 1: pos1 = "2"
    elif xy[1] == 2: pos1 = "3"
    elif xy[1] == 3: pos1 = "4"
    return (pos0,pos1)


def printBoard(board):
    for l in reversed(board):
        print(l)


def getCurBoard(whites, blacks):
    board = [['  ', '  ', '  ', '  '],
             ['  ', '  ', '  ', '  '],
             ['  ', '  ', '  ', '  '],
             ['  ', '  ', '  ', '  ']]
    for p in whites:
        x,y = posToXY(p[1:])
        board[y][x] = 'W'+p[0]
    for p in blacks:
        x,y = posToXY(p[1:])
        board[y][x] = 'B'+p[0]
    return board


def checkWin(pnm, opponent):
    for p in opponent:
        if p[0] == "Q":
            queenXy = posToXY((p[1],p[2]))
    for p in pnm:
        if queenXy[0] == p[0] and queenXy[1] == p[1]:
            return True
    return False


def eatPiece(pos, opponent):
    newOpponent = opponent[:]
    for i in range(len(opponent)):
        if pos[0] == opponent[i][1] and pos[1] == opponent[i][2]:
            del newOpponent[i]
            break
    return newOpponent


def simplifiedChessEngine(whites, blacks, moves, isWhite=True):
    if moves == 0:
        return None
    if not isWhite and moves < 2:
        return None
    # print("Moves: {}".format(moves))
    board = getCurBoard(whites, blacks)
    # printBoard(board)
    if isWhite:
        hasRecourse = False
        for i in range(len(whites)):
            pnm = getPossibleNextMoves(whites[i], board, isWhite=True)
            if checkWin(pnm, blacks):
                return "WHITEWIN"
            for j in pnm:
                pos = xyToPos(j)
                newWhites = whites[:i]+whites[i+1:]
                newWhites.append([whites[i][0], pos[0], pos[1]])
                newBlacks = eatPiece(pos, blacks)
                res = simplifiedChessEngine(newWhites, newBlacks, moves-1, isWhite=False)
                if res == "WHITEWIN":
                    return "WHITEWIN"
                elif res is None:
                    hasRecourse = True
        if hasRecourse:
            return None
        else:
            return "BLACKWIN"
    else:
        hasRecourse = False
        for i in range(len(blacks)):
            pnm = getPossibleNextMoves(blacks[i], board, isWhite=False)
            if checkWin(pnm, whites):
                return "BLACKWIN"
            for j in pnm:
                pos = xyToPos(j)
                newBlacks = blacks[:i] + blacks[i + 1:]
                newBlacks.append([blacks[i][0], pos[0], pos[1]])
                newWhites = eatPiece(pos, whites)
                res = simplifiedChessEngine(newWhites, newBlacks, moves-1, isWhite=True)
                if res == "BLACKWIN":
                    return "BLACKWIN"
                elif res is None:
                    hasRecourse = True
        if hasRecourse:
            return None
        else:
            return "WHITEWIN"


if __name__ == '__main__':
    if len(sys.argv) > 1:
        lines = ip.split('\n')
        g = int(lines[0])
        prev = 0
        game = 0
        for j in range(g):
            game += 1
            wbm = lines[prev+1].split()
            if game == 999:
                print("Line: {}".format(lines[prev+1]))
            w = int(wbm[0])
            b = int(wbm[1])
            m = int(wbm[2])
            whites = []
            for i in range(w):
                if game == 999:
                    print("Whites: {}".format(lines[2+i+prev]))
                whites.append(list(map(lambda x: x[0], lines[2+i+prev].rstrip().split())))
            blacks = []
            for i in range(b):
                if game == 999:
                    print("BLACKS: {}".format(lines[2+w+i+prev]))
                blacks.append(list(map(lambda x: x[0], lines[2+w+i+prev].rstrip().split())))
            result = simplifiedChessEngine(whites, blacks, m, isWhite=True)
            if result == "WHITEWIN":
                print("YES")
            else:
                print("NO")
            prev += w+b+1
    else:
        ## submission
        fptr = open(os.environ['OUTPUT_PATH'], 'w')
        g = int(input())
        for g_itr in range(g):
            wbm = input().split()
            w = int(wbm[0])
            b = int(wbm[1])
            m = int(wbm[2])
            whites = []
            for _ in range(w):
                whites.append(list(map(lambda x: x[0], input().rstrip().split())))
            blacks = []
            for _ in range(b):
                blacks.append(list(map(lambda x: x[0], input().rstrip().split())))
            result = simplifiedChessEngine(whites, blacks, m, isWhite=True)
            if result == "WHITEWIN":
                fptr.write("YES\n")
            else:
                fptr.write("NO\n")
        fptr.close()
