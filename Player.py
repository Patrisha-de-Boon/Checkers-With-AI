import pygame  # load pygame keywords
import sys     # let python use the file system
import os      # help python identify the OS
import Global

# Crown 0 is from the following link <div>Icons made by <a href="http://www.freepik.com" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a> is licensed by <a href="http://creativecommons.org/licenses/by/3.0/" title="Creative Commons BY 3.0" target="_blank">CC 3.0 BY</a></div> 

class PlayerPiece():
    def __init__(self, PlayerNum, x, y):
        self.player = PlayerNum
        self.x = x
        self.y = y
        self.path = os.path.join('Assets','Checker' + str(PlayerNum) + str(Global.checkerType)
        self.image = Global.get_image(self.path + '.png')
        self.image.rect.centre = self.x*Global.boardImg.rect.width/8 - Global.boardImg.rect.width/16, (9-self.y)*Global.boardImg.rect.width/8 - Global.boardImg.rect.width/16
        self.availableMoves = {}
        self.isKing = False

    def select(self):
        self.image = Global.get_image(os.path.join(self.path + 'H' + '.png')
        # TODO: show the available moves
    
    def deselect(self):
        self.image = Global.get_image(os.path.join(self.path + '.png')
    
    def move(self, newX, newY):
        if (newX, newY) in self.availableMoves:
            self.x = newX
            self.y = newY
        self.image.rect.centre = self.x*Global.boardImg.rect.width/8 - Global.boardImg.rect.width/16, (9-self.y)*Global.boardImg.rect.width/8 - Global.boardImg.rect.width/16

    def findMoves(self):
        self.availableMoves = {}
        if (self.player = 1 or self.isKing()) and self.x+1 < 9:
            if self.y-1 > 0 and (self.x+1, self.y-1) not in Global.Player1Dict and (self.x+1, self.y-1) not in Global.Player2Dict:
                self.availableMoves.append((self.x+1, self.y-1))
            if self.y+1 < 9 and (self.x+1, self.y+1) not in Global.Player1Dict and (self.x+1, self.y+1) not in Global.Player2Dict:
                self.availableMoves.append((self.x+1, self.y+1))
        if (self.player = 2 or self.isKing()) and self.x-1 > 0:
            if self.y-1 > 0 and (self.x-1, self.y-1) not in Global.Player1Dict and (self.x-1, self.y-1) not in Global.Player2Dict:
                self.availableMoves.append((self.x-1, self.y-1))
            if self.y+1 < 9 and (self.x-1, self.y+1) not in Global.Player1Dict and (self.x-1, self.y+1) not in Global.Player2Dict:
                self.availableMoves.append((self.x-1, self.y+1))

    def king(self):
        if self.isKing == False:
            self.isKing = True
            self.path = self.path + 'K'