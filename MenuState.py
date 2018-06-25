import pygame  # load pygame keywords
import sys     # let python use the file system
import os      # help python identify the OS
import Global  # includes variables meant to be common to multiple files
import itertools # includes extra tools for iterating through items

# completely redraw the entire screen and everything on it
def redraw(screen, selectedPiece):
    Global.drawBackground(screen)
    screen.blit(Global.boardImg, Global.boardImgRect)
    screen.blit(titleText, (Global.boardImgRect.left, int(Global.boardImgRect.top/2 - titleSize/2)))
    screen.blit(newGameText, newGameRect)
    screen.blit(loadGameText, loadGameRect)
    screen.blit(pieceText, pieceRect)
    screen.blit(backgroundText, backgroundRect)
    screen.blit(boardText, boardRect)
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
    newBoardSize = (int(7*height/10), int(7*height/10))
    if height > width:
        newBoardSize = (int(7*width/10), int(7*width/10))
    Global.boardImg = pygame.transform.scale(Global.get_image(os.path.join('Assets', 'Boards', 'Board' + str(Global.boardType) + '.jpg')), newBoardSize)
    Global.boardImgRect = Global.boardImg.get_rect()
    Global.boardImgRect.center = (Global.Width/3 if Global.Width/3 - Global.boardImgRect.width/2 > 0 else 9*Global.boardImgRect.width/16, 2*Global.Height/3 if 2*Global.Height/3 + Global.boardImgRect.height/2 < Global.Height else Global.Height - 9*Global.boardImgRect.height/16)
    for piece in Global.Player1List:
        piece.resize(screen)
    for piece in Global.Player2List:
        piece.resize(screen)

    global titleSize
    global titleText
    titleSize = int(Global.Height/9)
    titleFont = pygame.font.Font(os.path.join('Assets', 'Fonts', 'ahellya.ttf'), titleSize)
    titleText = titleFont.render("ChAI: Checkers with AI", True, Global.BLACK)

    global startFont
    global itemFont
    global newGameText
    global loadGameText
    global boardText
    global pieceText
    global backgroundText

    startSize = int(Global.Height/16)
    startFont = pygame.font.Font(os.path.join('Assets', 'Fonts', 'ahellya.ttf'), startSize)
    newGameText = startFont.render("Start New Game", True, Global.BLACK)

    itemSize = int(Global.Height/20)
    itemFont = pygame.font.Font(os.path.join('Assets', 'Fonts', 'ahellya.ttf'), itemSize)
    loadGameText = itemFont.render("Load Saved Game", True, Global.BLACK)
    pieceText = itemFont.render("Checker Pieces", True, Global.BLACK)
    boardText = itemFont.render("Board", True, Global.BLACK)
    backgroundText = itemFont.render("Background", True, Global.BLACK)

    global startRect
    global newGameRect
    global loadGameRect
    global pieceRect
    global backgroundRect
    global boardRect

    newGameRect = pygame.Rect(Global.Width - Global.boardImgRect.left - startFont.size("Start New Game")[0], Global.boardImgRect.top, startFont.size("Start New Game")[0], startFont.size("Start New Game")[1])
    loadGameRect = pygame.Rect(Global.Width - Global.boardImgRect.left - itemFont.size("Load Saved Game")[0], Global.boardImgRect.top + startSize + Global.boardImgRect.height/16, itemFont.size("Load Saved Game")[0], itemFont.size("Load Saved Game")[1]) 
    pieceRect = pygame.Rect(Global.Width - Global.boardImgRect.left - itemFont.size("Checker Pieces")[0], Global.boardImgRect.top + startSize + itemSize + Global.boardImgRect.height/8, itemFont.size("Checker Pieces")[0], itemFont.size("Checker Pieces")[1])
    backgroundRect = pygame.Rect(Global.Width - Global.boardImgRect.left - itemFont.size("Background")[0], Global.boardImgRect.top + startSize + itemSize*2 + 3*Global.boardImgRect.height/16, itemFont.size("Background")[0], itemFont.size("Background")[1])
    boardRect = pygame.Rect(Global.Width - Global.boardImgRect.left - itemFont.size("Board")[0], Global.boardImgRect.top + startSize + itemSize*3 + Global.boardImgRect.height/4, itemFont.size("Board")[0], itemFont.size("Board")[1])

# select and deselect menu items according to user input
def processMouseInput(screen, event, currPiece):
    # select pieces to show moves and how it all looks together
    for piece in itertools.chain(Global.Player1List, Global.Player2List):
        if piece.rect.collidepoint(event.pos):
            if piece != currPiece:
                if currPiece is not None:
                    currPiece.deselect(screen)
                piece.findMoves(screen)
                piece.select(screen)
                return False, piece
    if currPiece is not None:
        currPiece.deselect(screen)

    if newGameRect.collidepoint(event.pos):
        return True, 4
    elif loadGameRect.collidepoint(event.pos):
        return True, 8
    elif pieceRect.collidepoint(event.pos):
        return False, 0
    elif backgroundRect.collidepoint(event.pos):
        return False, 1
    elif boardRect.collidepoint(event.pos):
        return False, 2

    return False, None

def RunMenu(screen):
    Quit = False
    selectedPiece = None
    resizeScreen(screen, Global.Width, Global.Height)
    redraw(screen, selectedPiece)

    while not Quit:
        redrawFlag = False
        for event in pygame.event.get():
            # quit the game if the user presses the x button on the window
            if event.type == pygame.QUIT:
                Quit = True
                return 9
            
            # resize the board and the pieces according to the user's manipulation of the screen size
            elif event.type == pygame.VIDEORESIZE:
                resizeScreen(screen, event.w, event.h)
                redraw(screen, selectedPiece)
            
            # select and deselect pieces according to the user input
            elif event.type == pygame.MOUSEBUTTONDOWN:
                changeState, x = processMouseInput(screen, event, selectedPiece)
                if changeState:
                    # return x
                    pass
                else:
                    if x == 0:
                        Global.checkerType += 1
                        if Global.checkerType > 0:
                            Global.checkerType = 0
                    elif x == 1:
                        Global.backgroundType += 1
                        if Global.backgroundType > 2:
                            Global.backgroundType = 0
                        redraw(screen, selectedPiece)

                    elif x == 2:
                        Global.boardType += 1
                        if Global.boardType > 0:
                            Global.boardType = 0
                    else:
                        selectedPiece = x
                redrawFlag = True
            
        if redrawFlag:
            pygame.display.update(Global.toUpdate)
            Global.toUpdate.clear()