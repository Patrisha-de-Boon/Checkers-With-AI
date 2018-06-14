import pygame  # load pygame keywords
import sys     # let python use the file system
import os      # help python identify the OS
import Global
import GameState

# the initialisation calls for pygame and the current screen.
pygame.init()  # initialize module
Global.DisplayHeight, Global.DisplayWidth = pygame.display.Info()
screen = pygame.display.set_mode((Global.width, Global.height)) # create screen surface on
# which to draw things
screen.fill(shared.BLACK) # draw background
backdropbox = screen.get_rect()
screen.set_caption("ChAI - Checkers with AI")

# the functional state machine states are defined below
Quit = False
State = 0

# the get_image function will load in the correct image only once, and will store the image in 
# a dictionary so that it doesn't have to be loaded in pixel by pixel every time. This code
# came from this source https://nerdparadise.com/programming/pygame/part2.
_image_library = {}
def get_image(path):
        global _image_library
        image = _image_library.get(path)
        if image == None:
                image = pygame.image.load(path).convert_alpha()
                _image_library[path] = image
        return image

while not Quit:

    # Start
    if State == 0:
        State = 4  # TODO: change this to State == 1 when MainMenu is implemented

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
        boardImg = get_image(os.path.join('Assets','ChessBoard' + str(Global.boardType) + '.jpg')
        nextState = GameState.RunGame(screen, boardImg)

    # GameOver  
    if State == 5:
        #State = GameOver(screen)
        pass

    # Restart
    if State == 6:
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
