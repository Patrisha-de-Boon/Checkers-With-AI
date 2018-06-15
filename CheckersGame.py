import pygame  # load pygame keywords
import sys     # let python use the file system
import os      # help python identify the OS
import Global
import GameState

# the initialisation calls for pygame and the current screen.
pygame.init()  # initialize module
# record monitor information
Global.DisplayHeight, Global.DisplayWidth = pygame.display.Info()
# default to full screen, but this can be changes later in settings
Global.width = Global.DisplayWidth
Global.height = Global.DisplayHeight
screen = pygame.display.set_mode((Global.width, Global.height)) # create screen surface on
# which to draw things
screen.fill(shared.BLACK) # draw background
backdropbox = screen.get_rect()
screen.set_caption("ChAI - Checkers with AI")

# the functional state machine states are defined below
Quit = False
State = 0

while not Quit:

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
        nextState = GameState.RunGame(screen)

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
                player1Piece = Player.PlayerPiece(1, i, 2)
                Global.Player1List.add(Player1Piece)
                Global.Player1Dict(i, 2) = Player1Piece

                player2Piece = Player.PlayerPiece(2,i,6)
                Global.Player2List.add(Player2Piece)
                Global.Player2Dict(i, 6) = Player2Piece

                player2Piece = Player.PlayerPiece(2,i,8)
                Global.Player2List.add(Player2Piece)
                Global.Player2Dict(i, 8) = Player2Piece
                
            else:
                player1Piece = Player.PlayerPiece(1, i, 1)
                Global.Player1List.add(Player1Piece)
                Global.Player1Dict(i, 1) = Player1Piece

                player1Piece = Player.PlayerPiece(1, i, 3)
                Global.Player1List.add(Player1Piece)
                Global.Player1Dict(i, 3) = Player1Piece

                player2Piece = Player.PlayerPiece(2,i,7)
                Global.Player2List.add(Player2Piece)
                Global.Player2Dict(i, 7) = Player2Piece



       # TODO: make player pieces and other variables required to make the game run
        State = 4
        pass

    # PopUpMenu
    if State == 7:
        #State = PopUpMenuState(screen)
        pass

    # Load
    if State == 8:
        #State = LoadState(screen)
        pass
    
    # Quit
    if State == 9:
        Quit = True

    pygame.display.flip()  # required to show changes to screen
    Global.clock.tick(Global.fps) # limit fps of game to shared.fps

# closes the window.
pygame.quit()
sys.exit()
