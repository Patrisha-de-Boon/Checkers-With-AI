from random import randint

# note 0 means empty, 1 means player one pawn, 2 means player two pawn,
# 3 means player one king, 4 means player two king
def makeBoard(player1Pieces, player2Pieces):
    # make an 8 by 8 board (0 indexed)
    board = [[0 for i in range(8)] for j in range(8)]

    # place the pieces in their appropriate spots
    for piece in player1Pieces:
        if piece.isKing:
            board[piece.x-1][piece.y-1] = 3
        else:
            board[piece.x-1][piece.y-1] = 1
    for piece in player2Pieces:
          if piece.isKing:
            board[piece.x-1][piece.y-1] = 4
        else:
            board[piece.x-1][piece.y-1] = 2

# assume moves contains only the moves already required to get where you are now. Return all possible series of moves
def findJump(board, x, y, moves, possibleMoves = None):
    if possibleMoves is None:
        possibleMoves = []
    piece = board[x][y]
    mod2 = piece%2
    # if the piece can move 'up'
    if (mod2 != 0 or piece == 4) and y+1 < 8:
        # if the piece can move left
        if x-1 >= 0:
            # if you can jump over a piece in the upper left square, add it
            elif board[x-1][y+1]%2 != mod2 and y+2 < 8 and x-2 >= 0 and board[x-2][y+2] == 0:
                tempMoves = moves
                tempMoves.append([(x-1,y+1), (x-2, y+2)])

                tempBoard = board
                tempBoard[x-1][y+1] = tempBoard[x][y] = 0
                tempBoard[x-2][y+2] = piece
                newTempMoves = findJump(tempBoard, x-2, y+2, tempMoves, completeMoves)
                possibleMoves.append(newTempMoves)
        # if the piece can move right
        if x+1 < 8:
            # if you can jump over a piece in the upper right square, add it
            elif board[x+1][y+1]%2 != mod2 and y+2 < 8 and x+2 < 8 and board[x+2][y+2] == 0:
                tempMoves = moves
                tempMoves.append([(x+1,y+1), (x+2, y+2)])
                
                tempBoard = board
                tempBoard[x+1][y+1] = tempBoard[x][y] = 0
                tempBoard[x+2][y+2] = piece
                newTempMoves = findJump(tempBoard, x+2, y+2, tempMoves, completeMoves)
                possibleMoves.append(newTempMoves)

    # if the piece can move 'down'
    elif (mod2 == 0 or piece == 3) and y-1 >= 0: 
        # if the piece can move left
        if x-1 >= 0:
            # if you can jump over a piece in the bottom left square, add it
            elif board[x-1][y-1]%2 != mod2 and y+2 < 8 and x-2 > 0 and board[x-2][y-2] == 0:
                tempMoves = moves
                moves.append([(x-1,y-1), (x-2, y-2)])
                
                tempBoard = board
                tempBoard[x-1][y-1] = tempBoard[x][y] = 0
                tempBoard[x-2][y-2] = piece
                newTempMoves = findJump(tempBoard, x-2, y-2, tempMoves, completeMoves)
                possibleMoves.append(newTempMoves)
        # if the piece can move right
        if x+1 < 8:
            # if you can jump over a piece in the bottom right square, add it
            elif board[x+1][y-1]%2 != mod2 and y+2 < 8 and x+2 < 8 and board[x+2][y-2] == 0:
                tempMoves = moves
                moves.append([(x+1,y-1), (x+2, y-2)])
                
                tempBoard = board
                tempBoard[x+1][y-1] = tempBoard[x][y] = 0
                tempBoard[x+2][y-2] = piece
                newTempMoves = findJump(tempBoard, x+2, y-2, tempMoves, completeMoves)
                possibleMoves.append(newTempMoves)
    
    return possibleMoves

# given a board and a player, return a list of available but not necessary moves, 
# and a list of necessary moves
def findMoves(board, isPlayer1):
    availableMoves = []
    necessaryMoves = []
    for place in board:
        x, y = place
        piece = board[x][y]
        mod2 = piece%2
        # if the piece can move 'up'
        if (mod2 != 0 or piece == 4) and y+1 < 8:
            # if the piece can move left
            if x-1 >= 0:
                # if the upper left square is empty, add it
                if board[x-1][y+1] == 0:
                    availableMoves.append((x,y), (x-1,y+1))
                # if you can jump over a piece in the upper left square, add it
                elif board[x-1][y+1]%2 != mod2 and y+2 < 8 and x-2 >= 0 and board[x-2][y+2] == 0:
                    necessaryMoves.append([(x,y), (x-1,y+1), (x-2, y+2)])
            # if the piece can move right
            if x+1 < 8:
                # if the upper right square is empty, add it
                if board[x+1][y+1] == 0:
                    availableMoves.append((x+1,y+1))
                # if you can jump over a piece in the upper right square, add it
                elif board[x+1][y+1]%2 != mod2 and y+2 < 8 and x+2 < 8 and board[x+2][y+2] == 0:
                    necessaryMoves.append([(x+1,y+1), (x+2, y+2)])
        # if the piece can move 'down'
        elif (mod2 == 0 or piece == 3) and y-1 >= 0: 
            # if the piece can move left
            if x-1 >= 0:
                # if the bottom left square is empty, add it
                if board[x-1][y-1] == 0:
                    availableMoves.append((x-1,y-1))
                # if you can jump over a piece in the bottom left square, add it
                elif board[x-1][y-1]%2 != mod2 and y+2 < 8 and x-2 > 0 and board[x-2][y-2] == 0:
                    necessaryMoves.append([(x-1,y-1), (x-2, y-2)])
            # if the piece can move right
            if x+1 < 8:
                # if the bottom right square is empty, add it
                if board[x+1][y-1] == 0:
                    availableMoves.append((x+1,y-1))
                # if you can jump over a piece in the bottom right square, add it
                elif board[x+1][y-1]%2 != mod2 and y+2 < 8 and x+2 < 8 and board[x+2][y-2] == 0:
                    necessaryMoves.append([(x+1,y-1), (x+2, y-2)])
                
        return availableMoves, necessaryMoves

def EasyHeuristic():
    return randint(0, 100)

def MedHeuristic(board):
    return board.count(1) + board.count(3) - board.count(2) - board.count(4) 

def HarHeuristic(board):
    return board.count(1) + 2*board.count(3) - board.count(2) - 2*board.count(4)

def minimax(depth, maxDepth, difficulty, isPlayer1, isMax, board, moves, values = None):
    # if values hasn't been initialized, then initialize it
    if values is None:
        values = {}
        values[board] = MedHeuristic(board)

    # TODO: Make isWon test
    # return the value of the board, and the moves required to get to the board
    if depth == maxDepth or isWon:
        return values(board), moves

    availableMoves, necessaryMoves = findMoves
    if isMax:
        if necessaryMoves:
            for 
    
