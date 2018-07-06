#  
def minmax(depth, isPlayer1, player1Pieces, player2Pieces):

# return a random value for each configuration 
def EasyHeuristic():
    return rand()

# return a value based on how many more checker pieces you have compared to your opponent
def MidyHeuristic():

# reutnr a value based o nhow many more checker pieces you have, and how advantageously they are positioned
def HardHeuristic():

def findMoves(player, MyPieces, TheirPieces, location, isKing):
        # if the piece can move up
        if (player == 1 or isKing) and self.y+1 < 9:
            # if the piece can move left
            if self.x-1 > 0:
                # if this player's piece is not in the upper left square
                if (self.x-1, self.y+1) not in MyPieces:
                    # if there is no piece in the upper left square, add it as a possible move
                    if (self.x-1, self.y+1) not in TheirPieces:
                        self.availableMoves.append((self.x-1, self.y+1))
                    # if you can jump over the player piece, put it as a necessary move
                    elif self.y+2 < 9:
                        if self.x-2 > 0 and (self.x-2, self.y+2) not in MyPieces and (self.x-2, self.y+2) not in TheirPieces:
                            self.necessaryMoves[(self.x-2, self.y+2)] = (self.x-1, self.y+1)
            # if the piece can move right
            if self.x+1 < 9:
                # if this player's piece is not in the upper right square
                if (self.x+1, self.y+1) not in MyPieces:
                    # if there is no piece in the upper right square, add it as a possible move
                    if (self.x+1, self.y+1) not in TheirPieces:
                        self.availableMoves.append((self.x+1, self.y+1))
                    # if you can jump over the player piece, put it as a necessary move
                    elif self.y+2 < 9:
                        if self.x+2 < 9 and (self.x+2, self.y+2) not in MyPieces and (self.x+2, self.y+2) not in TheirPieces:
                            self.necessaryMoves[(self.x+2, self.y+2)] = (self.x+1, self.y+1)

        # if the piece can move down
        if (self.player == 2 or self.isKing) and self.y-1 > 0:
            # if the piece can move left
            if self.x-1 > 0:
                # if this player's piece is not in the bottom left square
                if (self.x-1, self.y-1) not in MyPieces:
                    # if there is no piece in the bottom left square, add it as a possible move
                    if (self.x-1, self.y-1) not in TheirPieces:
                        self.availableMoves.append((self.x-1, self.y-1))
                    # if you can jump over the player piece, put it as a necessary move
                    elif self.y-2 > 0:
                        if self.x-2 > 0 and (self.x-2, self.y-2) not in MyPieces and (self.x-2, self.y-2) not in TheirPieces:
                            self.necessaryMoves[(self.x-2, self.y-2)] = (self.x-1, self.y-1)
            # if the piece can move right
            if self.x+1 < 9:
                # if this player's piece is not in the bottom right square
                if (self.x+1, self.y-1) not in MyPieces:
                    # if there is no piece in the bottom right square, add it as a possible move
                    if (self.x+1, self.y-1) not in TheirPieces:
                        self.availableMoves.append((self.x+1, self.y-1))
                    # if you can jump over the player piece, put it as a necessary move
                    elif self.y-2 > 0:
                        if self.x+2 < 9 and (self.x+2, self.y-2) not in MyPieces and (self.x+2, self.y-2) not in TheirPieces:
                            self.necessaryMoves[(self.x+2, self.y-2)] = (self.x+1, self.y-1)