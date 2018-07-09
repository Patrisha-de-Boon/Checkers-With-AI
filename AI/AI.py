# Use the minimax algorithm to return the best move
def minimaxOld(difficulty, player, myPieces, theirPieces):
    depth = 1
    if difficulty == 1:
        depth = 4
    elif difficulty == 2:
        depth = 4
    isMyTurn = True
    values = dict()

    for i in range(depth + 1):
        Extreme = 0
        ExtremeMove = ((0,0), (0,0))
        necessary = False
        for piece in myPieces:
            availableMoves, necessaryMoves = findMoves(player, myPieces, theirPieces, piece.isKing)

            if necessaryMoves:
                necessary = True
                extremeValue = 0
                extremeMove = ((0,0), (0,0))
                for move in necessaryMoves:
                    _, _, moves, value = CompleteTurn((move[0], (piece.x, piece.y)), difficulty, player, piece, move[1], myPieces, theirPieces, isMax)
                    if (isMyTurn and value > )
            elif availableMoves and not necessary:

            
            for move in possibleMoves:

           
        if isMyTurn:
            isMyTurn = False
        else:
            isMyTurn = True

def CompleteTurn(moves, difficulty, player, piece, captured, myPieces, theirPieces, isMax):
    # find the new list of their pieces
    theirNewPieces
    for theirPiece in theirPieces:
        if theirPiece.x != captured[-1][0] or theirPiece.y != captured[-1][1]:
            theirNewPieces.append(theirPiece)

    # move your piece
    piece.x = moves[-1][0]
    piece.y = moves[-1][1]
        
    # find new moves
    availableMoves, necessaryMoves = findMoves(player, myPieces, theirNewPieces, piece.isKing)
    value = findValue(difficulty, player, myPieces, theirNewPieces)

    # return the new pieces and the moves required to get there when you can no longer move
    if not necessaryMoves:
        return myPieces, theirNewPieces, moves, value

    # otherwise move your piece again and recurse
    else:
        extremeValue = 0
        for newMove in necessaryMoves.keys():
            newMoves = moves
            newMoves.append(newMove)
            myNewPieces, NewPieces, newMoves, value = CompleteTurn(newMoves, player, piece, necessaryMoves[newMove], myPieces, theirNewPieces, false)
            if (isMax and value >= extremeValue) or (not isMax and value <= extremeValue:
                extremeValue = value
                theirNewPieces = newPieces
                myPieces = myNewPieces
                moves = newMoves

        return myPieces, theirNewPieces, moves, extremeValue

def findValue(difficulty, player, myPieces, theirPieces):
    if difficulty == 0:
        return EasyHeuristic()
    elif difficult == 1:
        return MidHeuristic(len(myPieces), len(theirPieces))
    elif difficulty == 2:
        return HardHeuristic()

# Find optimal move using the minimax algorithm
# depth is the current depth (int)
# difficulty determine which Heuristic to use (int)
# isMax shows if the current player is being maximized (bool)
# isPlayer1 shows if the player being maximized is player 1 (bool)
# myPieces is a list of the maximizing player's pieces (list of PlayerPiece objects)
# theirPieces is a list of the minimizing player's pieces (list of PlayerPiece objects)
# values is a dictionary mapping a move to it's value (dict of tuples of tuples)
# move is a tuple of a tuple defining the current move, where the starting x and y locations are on the left, and the ending x and y location is on the right
# maxDepth is the maximum depth (int)
def minimax(depth, difficulty, isMax, isPlayer1, myPieces, theirPieces, values, moves, maxDepth):
    # exit if depth reached
    if depth == maxDepth:
        return moves
    
    if isMax:
        return max(minimax(depth+1, difficulty, not isMax, isPlayer1, theirPieces, myPieces, values, ))

        

# return a random value for each configuration 
def EasyHeuristic():
    return rand() % 100

# return a value based on how many more checker pieces you have compared to your opponent
def MidHeuristic(numMyPieces, numTheirPieces):
    return numMyPieces - numTheirPieces

# reutnr a value based o nhow many more checker pieces you have, and how advantageously they are positioned
def HardHeuristic():
    pass

def findMoves(player, MyPieces, TheirPieces, x, y, isKing):
    availableMoves = []
    necessaryMoves = {}
    # if the piece can move up
    if (player == 1 or isKing) and y+1 < 9:
        # if the piece can move left
        if x-1 > 0:
            # if this player's piece is not in the upper left square
            if (x-1, y+1) not in MyPieces:
                # if there is no piece in the upper left square, add it as a possible move
                if (x-1, y+1) not in TheirPieces:
                    availableMoves.append((x-1, y+1))
                # if you can jump over the player piece, put it as a necessary move
                elif y+2 < 9:
                    if x-2 > 0 and (x-2, y+2) not in MyPieces and (x-2, y+2) not in TheirPieces:
                        necessaryMoves[(x-2, y+2)] = (x-1, y+1)
        # if the piece can move right
        if x+1 < 9:
            # if this player's piece is not in the upper right square
            if (x+1, y+1) not in MyPieces:
                # if there is no piece in the upper right square, add it as a possible move
                if (x+1, y+1) not in TheirPieces:
                    availableMoves.append((x+1, y+1))
                # if you can jump over the player piece, put it as a necessary move
                elif y+2 < 9:
                    if x+2 < 9 and (x+2, y+2) not in MyPieces and (x+2, y+2) not in TheirPieces:
                        necessaryMoves[(x+2, y+2)] = (x+1, y+1)

    # if the piece can move down
    if (player == 2 or isKing) and y-1 > 0:
        # if the piece can move left
        if x-1 > 0:
            # if this player's piece is not in the bottom left square
            if (x-1, y-1) not in MyPieces:
                # if there is no piece in the bottom left square, add it as a possible move
                if (x-1, y-1) not in TheirPieces:
                    availableMoves.append((x-1, y-1))
                # if you can jump over the player piece, put it as a necessary move
                elif y-2 > 0:
                    if x-2 > 0 and (x-2, y-2) not in MyPieces and (x-2, y-2) not in TheirPieces:
                        necessaryMoves[(x-2, y-2)] = (x-1, y-1)
        # if the piece can move right
        if x+1 < 9:
            # if this player's piece is not in the bottom right square
            if (x+1, y-1) not in MyPieces:
                # if there is no piece in the bottom right square, add it as a possible move
                if (x+1, y-1) not in TheirPieces:
                    availableMoves.append((x+1, y-1))
                # if you can jump over the player piece, put it as a necessary move
                elif y-2 > 0:
                    if x+2 < 9 and (x+2, y-2) not in MyPieces and (x+2, y-2) not in TheirPieces:
                        necessaryMoves[(x+2, y-2)] = (x+1, y-1)
        
        return availableMoves, necessaryMoves