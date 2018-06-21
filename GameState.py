import pygame  # load pygame keywords
import sys     # let python use the file system
import os      # help python identify the OS
import Global  # includes variables meant to be common to multiple files

# find all of the possible player moves, and show the necessary moves (ie. the capture moves)
def findAllPlayerMoves(screen):
    needToMove = []
    if Global.PlayerTurn == 1:
        PlayerPieces = Global.Player1List
    elif Global.PlayerTurn == 2:
        PlayerPieces = Global.Player2List
    for piece in PlayerPieces: 
        piece.findMoves(screen)
        if piece.necessaryMoves:
            needToMove.append(piece)
    return needToMove
    

# completely redraw the entire screen and everything on it
def redraw(screen, selectedPiece):
    screen.blit(Global.boardImg, Global.boardImgRect)
    if selectedPiece is not None:
        selectedPiece.select(screen)
    # draw the player pieces
    for player in Global.Player1List:
        player.draw(screen)
    for player in Global.Player2List:
        player.draw(screen)
    pygame.display.update()
    Global.toUpdate.clear()
  
# resize the screen and the items on it according to the user's manipulation of the screen size
def resizeScreen(screen, width, height):
    screen = pygame.display.set_mode((width, height), pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.RESIZABLE)
    Global.Width = width
    Global.Height = height
    Global.drawBackground(screen, Global.backImg)
    if height <= width:
        Global.boardImg = pygame.transform.scale(Global.get_image(os.path.join('Assets', 'Boards', 'Board' + str(Global.boardType) + '.jpg')), (int(9*height/10), int(9*height/10)))
    else:
        Global.boardImg = pygame.transform.scale(Global.get_image(os.path.join('Assets', 'Boards', 'Board' + str(Global.boardType) + '.jpg')), (int(9*width/10), int(9*width/10)))
    Global.boardImgRect = Global.boardImg.get_rect()
    Global.boardImgRect.center = (Global.Width/2, Global.Height/2)
    for piece in Global.Player1List:
        piece.resize(screen)
    for piece in Global.Player2List:
        piece.resize(screen)
    

# select and deselect player pieces according to user input
def processMouseInput(screen, event, currPiece):
    needToMove = findAllPlayerMoves(screen)
    # if a piece is selected and either there are no necessary moves, or the selected piece must move
    if currPiece is not None and (not needToMove or currPiece in needToMove):
        for Object in currPiece.placeHolders.keys():
            if Object.rect.collidepoint(event.pos):
                x, y = currPiece.placeHolders[Object]
                currPiece.move(screen, x, y)
                necessaryMoves = []
                if currPiece.isSelected:
                    currPiece.findMoves(screen)
                    necessaryMoves = currPiece.necessaryMoves.keys()
                # if no moves are necessary, it is the next player's turn
                if not necessaryMoves or not currPiece.isSelected:
                    if Global.PlayerTurn == 1:
                        Global.PlayerTurn = 2
                    else:
                        Global.PlayerTurn = 1
                    currPiece.deselect(screen)
                    return None
                return currPiece

    if Global.PlayerTurn == 1:    
        for piece in Global.Player1List:
            if piece.rect.collidepoint(event.pos):
                if piece != currPiece:
                    if currPiece is not None:
                        currPiece.deselect(screen)
                    if piece in needToMove or not needToMove:
                        piece.findMoves(screen)
                        piece.select(screen)
                    else:
                        piece.select(screen, canMove = False)
                    return piece

    elif Global.PlayerTurn == 2:
        for piece in Global.Player2List:
            if piece.rect.collidepoint(event.pos):
                if piece != currPiece:
                    if currPiece is not None:
                        currPiece.deselect(screen)
                    if piece in needToMove or not needToMove:
                        piece.findMoves(screen)
                        piece.select(screen)
                    else:
                        piece.select(screen, canMove = False)
                    return piece

    if currPiece is not None:
        currPiece.deselect(screen)
    return None

# Run the Game
def RunGame(screen):
    Quit = False
    selectedPiece = None
    resizeScreen(screen, Global.Width, Global.Height)
    redraw(screen, selectedPiece)

    while not Quit:
        redrawFlag = False
        # handle player input
        for event in pygame.event.get():
            # quit the game if the user presses the x button on the window
            if event.type == pygame.QUIT:
                Quit = True
                return 9

            # enter the pause screen if the user presses escape in game
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                Quit = True
                return 7

            # resize the board and the pieces according to the user's manipulation of the screen size
            elif event.type == pygame.VIDEORESIZE:
                resizeScreen(screen, event.w, event.h)
                redraw(screen, selectedPiece)
            
            # select and deselect pieces according to the user input
            elif event.type == pygame.MOUSEBUTTONDOWN:
                selectedPiece = processMouseInput(screen, event, selectedPiece)
                redrawFlag = True
                

        # redraw the board and pieces when necessary
        if redrawFlag:
            pygame.display.update(Global.toUpdate)
            Global.toUpdate.clear()
        Global.clock.tick(Global.fps) # Limit fps of game







        
