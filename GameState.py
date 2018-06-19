import pygame  # load pygame keywords
import sys     # let python use the file system
import os      # help python identify the OS
import Global  # includes variables meant to be common to multiple files

def redraw(screen):
    screen.blit(Global.boardImg, Global.boardImgRect)
    # draw the player pieces
    for player in Global.Player1List:
        player.draw(screen)
    for player in Global.Player1List:
        player.draw(screen)
  

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

def processMouseInput(screen, event, currPiece):
    for piece in Global.Player1List:
        if piece.rect.collidepoint(event.pos):
            if piece != currPiece:
                piece.select(screen)
                return piece
    for piece in Global.Player2List:
        if piece.rect.collidepoint(event.pos):
            if piece != currPiece:
                piece.select(screen)
                return piece
    return None

def RunGame(screen):
    Quit = False
    redraw(screen)
    selectedPiece = None

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
                redrawFlag = True
            
            elif event.type == pygame.MOUSEBUTTONDOWN:
                newSelectedPiece = processMouseInput(screen, event, selectedPiece)
                if selectedPiece is not None and newSelectedPiece != selectedPiece:
                    selectedPiece.deselect(screen)
                selectedPiece = newSelectedPiece

        # redraw the board and pieces when necessary
        if redrawFlag:
            pygame.display.update(Global.dirty_rects)
            Global.dirty_rects.()
        Global.clock.tick(Global.fps) # Limit fps of game







        
