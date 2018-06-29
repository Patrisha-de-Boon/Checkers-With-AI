import pygame  # load pygame keywords
import sys     # let python use the file system
import os      # help python identify the OS
import Global   # import global variables
import Player

# create a save file in .txt format from data structures in the game
def SaveGame(SaveNumber, PlayerTurn, Player1List, Player2List, roundTime, gameTime):
    ostream = open(os.path.join('Saves', 'save' + str(SaveNumber) + '.txt'), 'w')

    ostream.write('pt' + ',' + str(PlayerTurn))
    ostream.write(' ')

    for piece in Global.Player1List:
        isKing = '1' if piece.isKing else '0'
        isSelected = '1' if piece.isSelected else '0'
        ostream.write('p1' + ',' + str(piece.x) + ',' + str(piece.y) + ',' + isKing + ',' + isSelected)
        ostream.write(' ')

    for piece in Global.Player2List:
        isKing = '1' if piece.isKing else '0'
        isSelected = '1' if piece.isSelected else '0'
        ostream.write('p2' + ',' + str(piece.x) + ',' + str(piece.y) + ',' + isKing + ',' + isSelected)
        ostream.write(' ')

    ostream.write('rt' + ',' + str(roundTime))
    ostream.write(' ')

    ostream.write('gt' + ',' + str(gameTime))
    ostream.write(' ')

# read info from a save file into data structures the game can read
def LoadGame(screen, SaveNumber):
    # try opening a save file, and return an error if the file can't be opened
    try:
        istream = open(os.path.join('Saves', 'save' + str(SaveNumber) + '.txt'), 'r')
    except:
        print("A save file for save number " + str(SaveNumber) + " could not be found")
        return False
    
     # empty the player piece groups
    Global.Player1List.empty() 
    Global.Player2List.empty()
    Global.Player1Dict.clear()
    Global.Player2Dict.clear()
    selectedPiece = None

    # record the text in the istream and initialize the applicable data structures
    Input = istream.read().split()
    
    # for each space seperated section of the input file
    for I in Input:
        # create a list of each comma seperated section of I
        X = I.split(',')

        # record player turn
        if X[0] == 'pt':
            Global.PlayerTurn = int(X[1])

        # create the player pieces for player 1
        elif X[0] == 'p1':
            piece = Player.PlayerPiece(screen, 1, int(X[1]), int(X[2]))
            if X[3] == '1':
                piece.isKing = True
            if X[4] == '1':
                piece.isSlected = True
                selectedPiece = piece
            Global.Player1List.add(piece)
            Global.Player1Dict[int(X[1]), int(X[2])] = piece

        # create the player pieces for player 2
        elif X[0] == 'p2':
            piece = Player.PlayerPiece(screen, 2, int(X[1]), int(X[2]))
            if X[3] == '1':
                piece.isKing = True
            if X[4] == '1':
                piece.isSlected = True
            Global.Player2List.add(piece)
            Global.Player2Dict[int(X[1]), int(X[2])] = piece

        # record the time left in the round
        elif X[0] == 'rt':
            Global.roundTime = int(X[1])

        # record the time that this game has been played thus far
        elif X[0] == 'gt':
            Global.GameTime = int(X[1])
        
    return selectedPiece

# desplay the current saved games that can be loaded
def LoadState(screen):
    MustRewrite = False
    FileList = os.listdir(os.path.join('Saves'))
    NumFiles = len(FileList)
    if NumFiles > 10:
        MustRewrite = True
    for name in FileList:
        print(name)
    return 4
