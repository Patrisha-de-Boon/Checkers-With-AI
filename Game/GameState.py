import pygame  # load pygame keywords
import sys     # let python use the file system
import os      # help python identify the OS
import Global  # includes variables meant to be common to multiple files
import time
import SaveAndLoad

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

def drawTimers(screen):
    screen.blit(Global.get_image(os.path.join('Assets', 'Backgrounds', 'background2.jpg')), (gameTimeRect.left - 2, gameTimeRect.top - 2), (0, 0, gameTimeRect.width + 4, gameTimeRect.height + 4))
    screen.blit(Global.get_image(os.path.join('Assets', 'Backgrounds', 'background2.jpg')), (roundTimeRect.left - 2, roundTimeRect.top - 2), (0, 0, roundTimeRect.width + 4, roundTimeRect.height + 4))
    gameTimeText = clockFont.render(str(int(Global.GameTime/60)) + ':' + str(Global.GameTime%60).zfill(2), True, Global.BLACK)
    roundTimeText = clockFont.render(str(int(Global.roundTime/60))+ ':' + str(Global.roundTime%60).zfill(2), True, Global.BLACK)
    screen.blit(gameTimeText, gameTimeRect)
    screen.blit(roundTimeText, roundTimeRect)
    Global.toUpdate.append(gameTimeRect)
    Global.toUpdate.append(roundTimeRect)

# completely redraw the entire screen and everything on it
def redraw(screen, selectedPiece):
    screen.blit(Global.boardImg, Global.boardImgRect)
    Global.toUpdate.append(Global.boardImgRect)
    drawTimers(screen)
    if selectedPiece is not None:
        selectedPiece.select(screen)
    # draw the player pieces
    for player in Global.Player1List:
        player.draw(screen)
    for player in Global.Player2List:
        player.draw(screen)
  
# resize the screen and the items on it according to the user's manipulation of the screen size
def resizeScreen(screen, width, height):
    screen = pygame.display.set_mode((width, height), pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.RESIZABLE)
    Global.Width = width
    Global.Height = height
    Global.drawBackground(screen)
    if height <= width:
        Global.boardImg = pygame.transform.scale(Global.get_image(os.path.join('Assets', 'Boards', 'Board' + str(Global.boardType) + '.png')), (int(9*height/10), int(9*height/10)))
    else:
        Global.boardImg = pygame.transform.scale(Global.get_image(os.path.join('Assets', 'Boards', 'Board' + str(Global.boardType) + '.png')), (int(9*width/10), int(9*width/10)))
    Global.boardImgRect = Global.boardImg.get_rect()
    Global.boardImgRect.center = (Global.Width/2, Global.Height/2)
    for piece in Global.Player1List:
        piece.resize(screen)
    for piece in Global.Player2List:
        piece.resize(screen)
    
    global clockSize
    global clockFont
    global gameTimeText
    global roundTimeText
    global gameTimeRect
    global roundTimeRect
    
    clockSize = int(Global.Height/9)
    clockFont = pygame.font.Font(os.path.join('Assets', 'Fonts', 'ahellya.ttf'), clockSize)
    gameTimeText = clockFont.render(str(int(Global.GameTime/60)) + ':' + str(Global.GameTime%60).zfill(2), True, Global.BLACK)
    roundTimeText = clockFont.render(str(int(Global.roundTime/60))+ ':' + str(Global.roundTime%60).zfill(2), True, Global.BLACK)
    gameTimeRect = pygame.Rect(Global.Width - Global.boardImgRect.left/2 - (clockFont.size('0:00')[0])/2, Global.Height/2 - clockSize/2, clockFont.size('0:00')[0], clockSize)
    roundTimeRect = pygame.Rect((Global.Width - Global.boardImgRect.right)/2 - (clockFont.size('0:00')[0])/2, Global.Height/2 - clockSize/2, clockFont.size('0:00')[0], clockSize)

# select and deselect player pieces according to user input
def processMouseInput(screen, event, currPiece, needToMove):
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
def RunGame(screen, selectedPiece = None):
    Quit = False
    LastSwitch = time.time() # Last time the player turn switched
    LastTick = time.time() # Last time the timer increased
    needToMove = findAllPlayerMoves(screen) # list of necessary moves for the current player

    # draw in the screen
    resizeScreen(screen, Global.Width, Global.Height)
    redraw(screen, selectedPiece)
    pygame.display.update(Global.toUpdate)
    Global.toUpdate.clear()

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
                SaveAndLoad.SaveGame(0, Global.PlayerTurn, Global.Player1List, Global.Player2List, Global.roundTime, Global.GameTime)
                Quit = True
                return 7

            # resize the board and the pieces according to the user's manipulation of the screen size
            elif event.type == pygame.VIDEORESIZE:
                resizeScreen(screen, event.w, event.h)
                redraw(screen, selectedPiece)
                redrawFlag = True
            
            # select and deselect pieces according to the user input
            elif event.type == pygame.MOUSEBUTTONDOWN:
                startPlayer = Global.PlayerTurn
                selectedPiece = processMouseInput(screen, event, selectedPiece, needToMove)
                if startPlayer != Global.PlayerTurn:
                    needToMove = findAllPlayerMoves(screen)
                    # reset the roundTime
                    if needToMove:
                        Global.roundTime = 60
                    else:
                        Global.roundTime = 5*60
                    drawTimers(screen)
                redrawFlag = True
        
        # If it has been a second since the last tick, count the game timer up
        if time.time() - LastTick > 1:
            LastTick = time.time()
            Global.GameTime += 1
            Global.roundTime -= 1

            # if the player has used all time in a round, I chose to just let skip the player's turn
            if Global.roundTime <= 0:
                # deselect the piece if necessary
                if selectedPiece is not None:
                    selectedPiece.deselect(screen)
                    selectedPiece = None

                # skip the player's turn
                if Global.PlayerTurn == 1:
                    Global.PlayerTurn = 2
                else:
                    Global.PlayerTurn = 1
                needToMove = findAllPlayerMoves(screen)

                # reset the roundTime
                if needToMove:
                    Global.roundTime = 60
                else:
                    Global.roundTime = 5*60
            drawTimers(screen)
            redrawFlag = True
            

        # redraw the board and pieces when necessary
        if redrawFlag:
            pygame.display.update(Global.toUpdate)
            Global.toUpdate.clear()
            
        Global.clock.tick(Global.fps) # Limit fps of game

        # If the player
        if not Global.Player1Dict or not Global.Player2Dict:
            print("Game Over")
            Quit = True
            return 5







        
