import pygame  # load pygame keywords
import sys     # let python use the file system
import os      # help python identify the OS
import Global  # includes variables meant to be common to multiple files

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
def resizeScreen(screen, event):
    screen = pygame.display.set_mode(event.dict['size'], pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.RESIZABLE)
    Global.Width = event.w
    Global.Height = event.h
    if event.h <= event.w:
        Global.boardImg = pygame.transform.scale(Global.get_image(os.path.join('Assets','ChessBoard' + str(Global.boardType) + '.jpg')), (event.h, event.h))
    else:
        Global.boardImg = pygame.transform.scale(Global.get_image(os.path.join('Assets','ChessBoard' + str(Global.boardType) + '.jpg')), (event.w, event.w))
    Global.boardImgRect = Global.boardImg.get_rect()
    Global.boardImgRect.center = (Global.Width/2, Global.Height/2)
    for piece in Global.Player1List:
        piece.resize(screen)
    for piece in Global.Player2List:
        piece.resize(screen)

# select and deselect player pieces according to user input
def processMouseInput(screen, event, currPiece):
    if currPiece is not None:
        for Object in currPiece.placeHolders.keys():
            if Object.rect.collidepoint(event.pos):
                x, y = currPiece.placeHolders[Object]
                # x = int((rect.left - Global.boardImgRect.left - Global.boardImgRect.width/16 + Global.boardImgRect.width/9/2)/Global.boardImgRect.width*9.135)
                # y = int((rect.top - Global.boardImgRect.top - Global.boardImgRect.height/16 + Global.boardImgRect.height/9.14/2)/Global.boardImgRect.height*9.14)
                currPiece.move(screen, x, y)
                return currPiece

    if Global.PlayerTurn == 1:        
        for piece in Global.Player1List:
            if piece.rect.collidepoint(event.pos):
                if piece != currPiece:
                    if currPiece is not None:
                        currPiece.deselect(screen)
                    piece.select(screen)
                    return piece

    elif Global.playerTurn == 2:
        for piece in Global.Player2List:
            if piece.rect.collidepoint(event.pos):
                if piece != currPiece:
                    if currPiece is not None:
                        currPiece.deselect(screen)
                    piece.select(screen)
                    return piece
    if currPiece is not None:
        currPiece.deselect(screen)
    return None

# Run the Game
def RunGame(screen):
    Quit = False
    selectedPiece = None
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
                resizeScreen(screen, event)
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







        
