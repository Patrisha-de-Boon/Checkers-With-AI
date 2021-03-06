import pygame  # load pygame keywords
import sys     # let python use the file system
import os      # help python identify the OS
import Global  # includes variables meant to be common to multiple files
import itertools # includes extra tools for iterating through items

# completely redraw the entire screen and everything on it
def redraw(screen, selectedPiece, currentGame):
    Global.drawBackground(screen)
    screen.blit(Global.boardImg, Global.boardImgRect)
    screen.blit(Global.TimerBoard, Global.TimerBoardRect)

    # draw the menu options onto the screen
    screen.blit(titleText, (Global.boardImgRect.left, int(Global.boardImgRect.top/2 - titleSize/2)))
    if currentGame:
        screen.blit(continueGameText, continueGameRect)
    screen.blit(newGameText, newGameRect)
    screen.blit(loadGameText, loadGameRect)
    screen.blit(pieceText, pieceRect)
    screen.blit(backgroundText, backgroundRect)
    screen.blit(boardText, boardRect)
    screen.blit(timerText, timerRect)
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
def resizeScreen(screen, width, height, currentGame):
    screen = pygame.display.set_mode((width, height), pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.RESIZABLE)
    Global.Width = width
    Global.Height = height
    newBoardSize = (int(7*height/10), int(7*height/10))
    if height > width:
        newBoardSize = (int(7*width/10), int(7*width/10))
    Global.boardImg = pygame.transform.scale(Global.get_image(os.path.join('Assets', 'Boards', 'Board' + str(Global.boardType) + '.png')), newBoardSize)
    Global.boardImgRect = Global.boardImg.get_rect()
    Global.boardImgRect.center = (Global.Width/3 if Global.Width/3 - Global.boardImgRect.width/2 > 0 else 9*Global.boardImgRect.width/16, 2*Global.Height/3 if 2*Global.Height/3 + Global.boardImgRect.height/2 < Global.Height else Global.Height - 9*Global.boardImgRect.height/16)
    for piece in Global.Player1List:
        piece.resize(screen)
    for piece in Global.Player2List:
        piece.resize(screen)

    # creat title text
    global titleSize
    global titleText
    titleSize = int(Global.Height/9)
    titleFont = pygame.font.Font(os.path.join('Assets', 'Fonts', 'ahellya.ttf'), titleSize)
    if Global.Width - 2*Global.boardImgRect.left < titleFont.size("ChAI: Checkers with AI")[0]:
        titleRatio = titleFont.size("ChAI: Checkers with AI")[0]/titleSize
        titleSize = int((Global.Width - 2*Global.boardImgRect.left) / titleRatio)
        titleFont = pygame.font.Font(os.path.join('Assets', 'Fonts', 'ahellya.ttf'), titleSize)
    titleText = titleFont.render("ChAI: Checkers with AI", True, Global.BLACK)

    # create text for the menu options
    global startFont
    global itemFont
    global newGameText
    global continueGameText
    global loadGameText
    global boardText
    global pieceText
    global backgroundText
    global timerText

    startSize = int(Global.Height/16)
    startFont = pygame.font.Font(os.path.join('Assets', 'Fonts', 'ahellya.ttf'), startSize)
    itemFont = pygame.font.Font(os.path.join('Assets', 'Fonts', 'ahellya.ttf'), int(startSize*4/5))
    if Global.Width - Global.boardImgRect.left - startFont.size("Start New Game")[0] < Global.boardImgRect.right:
        startRatio = startFont.size("Start New Game")[0] / int(Global.Height/16)
        startSize = int((Global.Width - Global.boardImgRect.right - Global.boardImgRect.left - 2) / startRatio)
        startFont = pygame.font.Font(os.path.join('Assets', 'Fonts', 'ahellya.ttf'), startSize)
        itemFont = pygame.font.Font(os.path.join('Assets', 'Fonts', 'ahellya.ttf'), int(startSize*4/5))

    newGameText = startFont.render("Start New Game", True, Global.BLACK)
    continueGameText = startFont.render("Continue Game", True, Global.BLACK)
    loadGameText = itemFont.render("Load Saved Game", True, Global.BLACK)
    pieceText = itemFont.render("Checker Pieces", True, Global.BLACK)
    boardText = itemFont.render("Board", True, Global.BLACK)
    backgroundText = itemFont.render("Background", True, Global.BLACK)
    timerText = itemFont.render("Timer", True, Global.BLACK)

    # create the rects in which to place the menu option text
    global startRect
    global newGameRect
    global continueGameRect
    global loadGameRect
    global pieceRect
    global backgroundRect
    global boardRect
    global timerRect

    newGameRect = pygame.Rect(Global.Width - Global.boardImgRect.left - startFont.size("Start New Game")[0], Global.boardImgRect.top, startFont.size("Start New Game")[0], startFont.size("Start New Game")[1])
    if not currentGame:
        loadGameRect = pygame.Rect(Global.Width - Global.boardImgRect.left - itemFont.size("Load Saved Game")[0], Global.boardImgRect.top + startSize + Global.boardImgRect.height/16, itemFont.size("Load Saved Game")[0], itemFont.size("Load Saved Game")[1]) 
        pieceRect = pygame.Rect(Global.Width - Global.boardImgRect.left - itemFont.size("Checker Pieces")[0], Global.boardImgRect.top + startSize + int(startSize*4/5) + Global.boardImgRect.height/8, itemFont.size("Checker Pieces")[0], itemFont.size("Checker Pieces")[1])
        backgroundRect = pygame.Rect(Global.Width - Global.boardImgRect.left - itemFont.size("Background")[0], Global.boardImgRect.top + startSize + int(startSize*4/5)*2 + 3*Global.boardImgRect.height/16, itemFont.size("Background")[0], itemFont.size("Background")[1])
        boardRect = pygame.Rect(Global.Width - Global.boardImgRect.left - itemFont.size("Board")[0], Global.boardImgRect.top + startSize + int(startSize*4/5)*3 + Global.boardImgRect.height/4, itemFont.size("Board")[0], itemFont.size("Board")[1])
        timerRect = pygame.Rect(Global.Width - Global.boardImgRect.left - itemFont.size("Timer")[0], Global.boardImgRect.top + startSize + int(startSize*4/5)*4 + 5*Global.boardImgRect.height/16, itemFont.size("Timer")[0], itemFont.size("Timer")[1])
        
        
    else:
        continueGameRect = pygame.Rect(Global.Width - Global.boardImgRect.left - startFont.size("Continue Game")[0], Global.boardImgRect.top + startSize + Global.boardImgRect.height/16, startFont.size("Continue Game")[0], startFont.size("Continue Game")[1]) 
        loadGameRect = pygame.Rect(Global.Width - Global.boardImgRect.left - itemFont.size("Load Saved Game")[0], Global.boardImgRect.top + startSize*2 + Global.boardImgRect.height/8, itemFont.size("Load Saved Game")[0], itemFont.size("Load Saved Game")[1]) 
        pieceRect = pygame.Rect(Global.Width - Global.boardImgRect.left - itemFont.size("Checker Pieces")[0], Global.boardImgRect.top + startSize*2 + int(startSize*4/5) + 3*Global.boardImgRect.height/16, itemFont.size("Checker Pieces")[0], itemFont.size("Checker Pieces")[1])
        backgroundRect = pygame.Rect(Global.Width - Global.boardImgRect.left - itemFont.size("Background")[0], Global.boardImgRect.top + startSize*2 + int(startSize*4/5)*2 + Global.boardImgRect.height/4, itemFont.size("Background")[0], itemFont.size("Background")[1])
        boardRect = pygame.Rect(Global.Width - Global.boardImgRect.left - itemFont.size("Board")[0], Global.boardImgRect.top + startSize*2 + int(startSize*4/5)*3 + 5*Global.boardImgRect.height/16, itemFont.size("Board")[0], itemFont.size("Board")[1])
        timerRect = pygame.Rect(Global.Width - Global.boardImgRect.left - itemFont.size("Timer")[0], Global.boardImgRect.top + startSize*2 + int(startSize*4/5)*4 + 3*Global.boardImgRect.height/8, itemFont.size("Timer")[0], itemFont.size("Timer")[1])
        
        
    Global.TimerBoard = pygame.transform.scale(Global.get_image(os.path.join('Assets', 'TimerBoards', 'TimerBoard' + str(Global.TimerBoardType) + '.png')), (int(timerRect.width + 2*timerRect.height/13), int(timerRect.height + 2*timerRect.height/13)))
    Global.TimerBoardRect = Global.TimerBoard.get_rect()
    Global.TimerBoardRect.left = timerRect.left - timerRect.height/13
    Global.TimerBoardRect.top = timerRect.top - timerRect.height/13

# select and deselect menu items according to user input
def processMouseInput(screen, event, currPiece, currentGame):
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

    if currentGame:
        if continueGameRect.collidepoint(event.pos):
            return True, 4
    if newGameRect.collidepoint(event.pos):
        return True, 6
    elif loadGameRect.collidepoint(event.pos):
        return True, 8
    elif pieceRect.collidepoint(event.pos):
        return False, 0
    elif backgroundRect.collidepoint(event.pos):
        return False, 1
    elif boardRect.collidepoint(event.pos):
        return False, 2
    elif timerRect.collidepoint(event.pos):
        return False, 3

    return False, None

# Run the Menu state
def RunMenu(screen, currentGame):
    Quit = False
    selectedPiece = None
    resizeScreen(screen, Global.Width, Global.Height, currentGame)
    redraw(screen, selectedPiece, currentGame)

    while not Quit:
        redrawFlag = False
        for event in pygame.event.get():
            # quit the game if the user presses the x button on the window
            if event.type == pygame.QUIT:
                Quit = True
                return 9
            
            # resize the board and the pieces according to the user's manipulation of the screen size
            elif event.type == pygame.VIDEORESIZE:
                resizeScreen(screen, event.w, event.h, currentGame)
                redraw(screen, selectedPiece, currentGame)
            
            # select and deselect pieces and buttons according to the user input
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # x is 0 to 3 if they changes aesthetics, it's the new state if they changed states, 
                # and it is the new selected piece if they selected or deselected a piece
                changeState, x = processMouseInput(screen, event, selectedPiece, currentGame)
                if changeState:
                    return x
                    pass
                else:
                    # Change the checker type
                    if x == 0:
                        Global.checkerType += 1
                        if Global.checkerType > 0:
                            Global.checkerType = 0

                    # Change the background
                    elif x == 1:
                        Global.backgroundType += 1
                        if Global.backgroundType > 6:
                            Global.backgroundType = 0
                        redraw(screen, selectedPiece, currentGame)

                    # Change the checker board
                    elif x == 2:
                        Global.boardType += 1
                        if Global.boardType > 8:
                            Global.boardType = 0
                        newBoardSize = (int(7*Global.Height/10), int(7*Global.Height/10))
                        if Global.Height > Global.Width:
                            newBoardSize = (int(7*Global.Width/10), int(7*Global.Width/10))
                        Global.boardImg = pygame.transform.scale(Global.get_image(os.path.join('Assets', 'Boards', 'Board' + str(Global.boardType) + '.png')), newBoardSize)
                        screen.blit(Global.boardImg, Global.boardImgRect)
                        for piece in Global.Player1List:
                            piece.resize(screen)
                        for piece in Global.Player2List:
                            piece.resize(screen)
                        pygame.display.update(Global.boardImgRect)

                    # Change the timer board 
                    elif x == 3:
                        Global.TimerBoardType += 1
                        if Global.TimerBoardType > 6:
                            Global.TimerBoardType = 0
                        Global.TimerBoard = pygame.transform.scale(Global.get_image(os.path.join('Assets', 'TimerBoards', 'TimerBoard' + str(Global.TimerBoardType) + '.png')), (int(timerRect.width + 2*timerRect.height/13), int(timerRect.height + 2*timerRect.height/13)))
                        screen.blit(Global.TimerBoard, Global.TimerBoardRect)
                        screen.blit(timerText, timerRect)
                        Global.toUpdate.append(Global.TimerBoardRect)

                    # otherwise just select the applicable piece
                    else:
                        selectedPiece = x
                    
                redrawFlag = True
            
        if redrawFlag:
            pygame.display.update(Global.toUpdate)
            Global.toUpdate.clear()