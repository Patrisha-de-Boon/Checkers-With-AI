import pygame  # load pygame keywords
import sys     # let python use the file system
import os      # help python identify the OS

# the initialisation calls for pygame and the current screen.
pygame.init()  # initialize module
# record monitor information
DisplayInfo = pygame.display.Info()
# create screen surface on
screen = pygame.display.set_mode((720, 720)) 

# import gloabl after initializing pygame and screen
import Global
import GameState
import Player

Global.DisplayHeight = DisplayInfo.current_h
Global.DisplayWidth = DisplayInfo.current_w
# default to full screen, but this can be changes later in settings
Global.Width = 720
Global.Height = 720

# which to draw things
if Global.Width < Global.Height:
    measurement = Global.Width
else:
    measurement = Global.Height
Global.boardImg = pygame.transform.scale(Global.get_image(os.path.join('Assets','ChessBoard' + str(Global.boardType) + '.jpg')), (measurement, measurement))
Global.boardImgRect = Global.boardImg.get_rect()
Global.boardImgRect.center = (Global.Width/2, Global.Height/2)

screen.fill(Global.BLACK) # draw background
backdropbox = screen.get_rect()
pygame.display.set_caption("ChAI - Checkers with AI")

# the functional state machine states are defined below
Quit = False
State = 0

while not Quit:

     # handle player input
    for event in pygame.event.get():
        # quit the game if the user presses the x button on the window
        if event.type == pygame.QUIT:
            quit = True
            break

        elif event.type == pygame.KEYDOWN:
            # enter the pause screen if they press escape in game
            if State == 4 and event.key == pygame.K_ESCAPE:
                State = 7
        elif event.type == pygame.VIDEORESIZE:
            screen = pygame.display.set_mode(event.dict['size'], pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.RESIZABLE)
            screen.blit(pygame.transform.scale(Global.boardImg, event.dict['size']), (0, 0))
            Global.Width = event.w
            Global.Height = event.h
            pygame.display.flip()

    # Start
    if State == 0:
        # Show splash screen and start screen
        State = 6  # TODO: change this to State == 1 when MainMenu is implemented

    # MainMenu
    if  State == 1:
        #State = MainMenuState(screen)
        pass

    # Settings
    if State == 2:
        #State = SettingsState(screen)
        pass

    # HighScores
    if State == 3:
        #State = HighScores(screen)
        pass

    # Game
    if State == 4:
        # run game and change state acording to output
        State = GameState.RunGame(screen)

    # GameOver  
    if State == 5:
        #State = GameOver(screen)
        pass

    # Restart
    if State == 6:
        # empty the player piece groups
        Global.Player1List.empty() 
        Global.Player2List.empty()
        Global.Player1Dict.clear()
        Global.Player2Dict.clear()

        # place the player pieces in the correct location and store the data
        for i in range(1,9):
            if i%2 != 0:
                Player1Piece = Player.PlayerPiece(1, i, 2)
                Global.Player1List.add(Player1Piece)
                Global.Player1Dict[i, 2] = Player1Piece

                Player2Piece = Player.PlayerPiece(2,i,6)
                Global.Player2List.add(Player2Piece)
                Global.Player2Dict[i, 6] = Player2Piece

                Player2Piece = Player.PlayerPiece(2,i,8)
                Global.Player2List.add(Player2Piece)
                Global.Player2Dict[i, 8] = Player2Piece
                
            else:
                Player1Piece = Player.PlayerPiece(1, i, 1)
                Global.Player1List.add(Player1Piece)
                Global.Player1Dict[i, 1] = Player1Piece

                Player1Piece = Player.PlayerPiece(1, i, 3)
                Global.Player1List.add(Player1Piece)
                Global.Player1Dict[i, 3] = Player1Piece

                Player2Piece = Player.PlayerPiece(2,i,7)
                Global.Player2List.add(Player2Piece)
                Global.Player2Dict[i, 7] = Player2Piece

        State = 4 # go to the game state

    # Pause
    if State == 7:
        #State = PauseState(screen)
        pass

    # Load
    if State == 8:
        #State = LoadState(screen)
        pass
    
    # Quit
    if State == 9:
        Quit = True

# closes the window.
pygame.display.quit()
pygame.quit()
sys.exit()
