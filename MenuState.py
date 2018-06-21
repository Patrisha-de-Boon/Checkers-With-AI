import pygame  # load pygame keywords
import sys     # let python use the file system
import os      # help python identify the OS
import Global  # includes variables meant to be common to multiple files
import itertools # includes extra tools for iterating through items

titleFont = pygame.font.SysFont("ahellya", 72)
# titleText = titleFont.render("ChAI: Checkers with AI", True, Global.BLACK)

# completely redraw the entire screen and everything on it
def redraw(screen, selectedPiece):
    screen.blit(Global.boardImg, Global.boardImgRect)
    screen.blit(titleFont, )
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
                return piece

    if currPiece is not None:
        currPiece.deselect(screen)
    return None

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
                selectedPiece = processMouseInput(screen, event, selectedPiece)
                redrawFlag = True
            
        if redrawFlag:
            pygame.display.update(Global.toUpdate)
            Global.toUpdate.clear()