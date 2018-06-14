DisplayWidth = 0
DisplayHeight = 0

WindowWidth = 500
WindowHeight = 500
boardType = 0  # default board type is 0 (the wooden one from this source http://www.vectorcopy.com/brown-wooden-chessboard-top-view-141-free-vector.html )

# this is the list of all the main colours.
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GOLD = (249, 166, 2)
BLUE = (0, 0, 255)
GRAY = (134, 136, 138)
RED = (255, 0, 0)
DARKBLUE = (16,24,115)

fps = 60 # max fps of game (not really necessary here but good practice)
clock = pygame.time.Clock() # game clock

Player1List  = pygame.sprite.Group()
Player2List  = pygame.sprite.Group()