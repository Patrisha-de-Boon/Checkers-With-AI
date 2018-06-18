import pygame  # load pygame keywords
import sys     # let python use the file system
import os      # help python identify the OS
import Global

# Crown 0 is from the following link <div>Icons made by <a href="http://www.freepik.com" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a> is licensed by <a href="http://creativecommons.org/licenses/by/3.0/" title="Creative Commons BY 3.0" target="_blank">CC 3.0 BY</a></div> 

class PlayerPiece(pygame.sprite.Sprite):
    def __init__(self, PlayerNum, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.player = PlayerNum
        self.x = x
        self.y = y
        self.path = os.path.join('Assets','Checker' + str(PlayerNum) + str(Global.checkerType))
        self.image = Global.get_image(self.path + '.png')
        self.image = pygame.transform.scale(self.image, (int(Global.boardImgRect.width/10), int(Global.boardImgRect.height/10)))
        self.rect  = self.image.get_rect()
        self.__place__()
        self.availableMoves = {}
        self.isKing = False
        self.isSelected = False

    # select the piece and show all of its available moves
    def select(self):
        self.isselected = True
        self.image = Global.get_image(os.path.join(self.path + 'H' + '.png'))

        # TODO: show the available moves
    
    # deselect the piece and stop showing all of its available moves
    def deselect(self):
        self.isSelected = False
        self.resize
    
    # move the piece to a new location on the board
    def move(self, newX, newY):
        if (newX, newY) in self.availableMoves:
            self.x = newX
            self.y = newY
        self.__place__()

    # find and record all available moves for this piece
    def findMoves(self):
        self.availableMoves = {}
        if (self.player == 1 or self.isKing()) and self.x+1 < 9:
            if self.y-1 > 0 and (self.x+1, self.y-1) not in Global.Player1Dict and (self.x+1, self.y-1) not in Global.Player2Dict:
                self.availableMoves.append((self.x+1, self.y-1))
            if self.y+1 < 9 and (self.x+1, self.y+1) not in Global.Player1Dict and (self.x+1, self.y+1) not in Global.Player2Dict:
                self.availableMoves.append((self.x+1, self.y+1))
        if (self.player == 2 or self.isKing()) and self.x-1 > 0:
            if self.y-1 > 0 and (self.x-1, self.y-1) not in Global.Player1Dict and (self.x-1, self.y-1) not in Global.Player2Dict:
                self.availableMoves.append((self.x-1, self.y-1))
            if self.y+1 < 9 and (self.x-1, self.y+1) not in Global.Player1Dict and (self.x-1, self.y+1) not in Global.Player2Dict:
                self.availableMoves.append((self.x-1, self.y+1))

    # king a piece so it can move in every direction
    def king(self):
        if self.isKing == False:
            self.isKing = True
            self.path = self.path + 'K'

    # resize the pieces according to the board image size and location
    def resize(self):
        if self.isSelected == False:
            self.image = pygame.transform.scale(Global.get_image(self.path + '.png'), (int(Global.boardImgRect.width/10), int(Global.boardImgRect.height/10)))
        else:
            self.image = pygame.transform.scale(Global.get_image(self.path + 'H' + '.png'), (int(Global.boardImgRect.width/10), int(Global.boardImgRect.height/10)))
        self.rect = self.image.get_rect()
        self.__place__()

    # place the pieces according to their x and y location on the board.
    def __place__(self):
        self.rect.center = (Global.boardImgRect.left + Global.boardImgRect.width/16 + self.x*Global.boardImgRect.width/9.135 - Global.boardImgRect.width/9/2, Global.boardImgRect.top + Global.boardImgRect.height/16 + (9-self.y)*Global.boardImgRect.height/9.14- Global.boardImgRect.height/9.14/2)
