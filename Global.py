
import pygame  # load pygame keywords
import TwoWayDict  # include two way dictionary class for player character

DisplayWidth = 0
DisplayHeight = 0

WindowWidth = 500
WindowHeight = 500
boardType = 0  # default board type is 0 (the wooden one from this source http://www.vectorcopy.com/brown-wooden-chessboard-top-view-141-free-vector.html)
checkerType = 0 # default board type is 0 (the wooden ones. The original unedited image came from here https://www.bearwood.com/product119.html)

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

# sprite list for each player's pieces
Player1List  = pygame.sprite.Group()
Player2List  = pygame.sprite.Group()

# dictionary to access location from player piece and vice versa
Player1Dict = {}
Player2Dict = {}

# the get_image function will load in the correct image for each enemy 
# only once, and will store the image in a dictionary so that it doesn't have
# to be loaded in pixel by pixel every time a new bullet is spawned. This code
# came from this source https://nerdparadise.com/programming/pygame/part2.
_image_library = {}
def get_image(path):
        global _image_library
        image = _image_library.get(path)
        if image == None:
                image = pygame.image.load(path).convert_alpha()
                _image_library[path] = image
        return image

boardImg = get_image(os.path.join('Assets','ChessBoard' + str(boardType) + '.jpg')
