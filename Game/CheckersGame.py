import pygame  # load pygame keywords
import sys     # let python use the file system
import os      # help python identify the OS

# the initialisation calls for pygame and the current screen.
pygame.init()  # initialize module
# record monitor information
DisplayInfo = pygame.display.Info()
# create screen surface on
screen = pygame.display.set_mode((720, 1080), pygame.FULLSCREEN) 

# import gloabl after initializing pygame and screen
import Global
import GameState
import Player
import MenuState
import SaveAndLoad

# default to full screen, but this can be changes later in settings
Global.DisplayHeight = DisplayInfo.current_h
Global.DisplayWidth = DisplayInfo.current_w

Global.Height = 720
Global.Width = 1080

# which to draw things
if Global.Width < Global.Height:
    measurement = Global.Width
else:
    measurement = Global.Height
# Global.boardImg = pygame.transform.scale(Global.get_image(os.path.join('Assets','ChessBoard' + str(Global.boardType) + '.jpg')), (int(9*measurement/10), int(9*measurement/10)))
# Global.boardImgRect = Global.boardImg.get_rect()
# Global.boardImgRect.center = (Global.Width/2, Global.Height/2)

# Global.drawBackground(screen, Global.backImg) # draw the background
backdropbox = screen.get_rect()
pygame.display.set_caption("ChAI - Checkers with AI")

# the functional state machine states are defined below
Quit = False
State = 0
toMenu = False
CurrentGame = False

while not Quit:

     # handle player input
    for event in pygame.event.get():
        # quit the game if the user presses the x button on the window
        if event.type == pygame.QUIT:
            quit = True
            break

    # Start
    if State == 0:
        # Show splash screen and start screen
        State = 6
        toMenu = True

    # MainMenu
    if  State == 1:
        toMenu = False
        State = MenuState.RunMenu(screen, CurrentGame)

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
        CurrentGame = True

    # GameOver  
    if State == 5:
        # end the last game, reset pieces, then go to the menu
        CurrentGame = False
        State = 6
        toMenu = True
        #State = GameOver(screen) # show game over screen

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
                Player1Piece = Player.PlayerPiece(screen, 1, i, 1)
                Global.Player1List.add(Player1Piece)
                Global.Player1Dict[i, 1] = Player1Piece

                Player1Piece = Player.PlayerPiece(screen, 1, i, 3)
                Global.Player1List.add(Player1Piece)
                Global.Player1Dict[i, 3] = Player1Piece

                Player2Piece = Player.PlayerPiece(screen, 2,i,7)
                Global.Player2List.add(Player2Piece)
                Global.Player2Dict[i, 7] = Player2Piece
                
            else:
                Player1Piece = Player.PlayerPiece(screen, 1, i, 2)
                Global.Player1List.add(Player1Piece)
                Global.Player1Dict[i, 2] = Player1Piece

                Player2Piece = Player.PlayerPiece(screen, 2,i,6)
                Global.Player2List.add(Player2Piece)
                Global.Player2Dict[i, 6] = Player2Piece

                Player2Piece = Player.PlayerPiece(screen, 2,i,8)
                Global.Player2List.add(Player2Piece)
                Global.Player2Dict[i, 8] = Player2Piece

        if toMenu:
            CurrentGame = False
            State = 1
        else:
            State = 4 # go to the game state

    # Pause
    if State == 7:
        #State = PauseState(screen)
        State = 1

    # Load a Game
    if State == 8:
        State = SaveAndLoad.LoadState(screen)
        #print(State)
        # selectedPiece = SaveAndLoad.LoadGame(screen, 0)
        # State = GameState.RunGame(screen, selectedPiece)
    
    # Quit
    if State == 9:
        Quit = True

# closes the window.
pygame.display.quit()
pygame.quit()
sys.exit()
