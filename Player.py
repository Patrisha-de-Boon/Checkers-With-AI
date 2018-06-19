import pygame  # load pygame keywords
import sys     # let python use the file system
import os      # help python identify the OS
import Global   # import global variables

# Crown 0 is from the following link <div>Icons made by <a href="http://www.freepik.com" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a> is licensed by <a href="http://creativecommons.org/licenses/by/3.0/" title="Creative Commons BY 3.0" target="_blank">CC 3.0 BY</a></div> 

class PlayerPiece(pygame.sprite.Sprite):
    class PlaceHolder(pygame.sprite.Sprite):
        def __init__(self, x, y):
            self.x = x
            self.y = y
            self.image = pygame.transform.scale(Global.get_image(os.path.join('Assets', 'placeHolder' + str(Global.placeHolderType) + '.png')), (int(Global.boardImgRect.width/13), int(Global.boardImgRect.height/13)))
            self.rect = self.image.get_rect()
            self.rect.center = (Global.boardImgRect.left + Global.boardImgRect.width/16 + x*Global.boardImgRect.width/9.135 - Global.boardImgRect.width/9/2, Global.boardImgRect.top + Global.boardImgRect.height/16 + (9-y)*Global.boardImgRect.height/9.14- Global.boardImgRect.height/9.14/2)

    def __init__(self, screen, PlayerNum, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.player = PlayerNum
        self.x = x
        self.y = y
        self.path = os.path.join('Assets','Checker' + str(PlayerNum) + str(Global.checkerType))
        self.image = Global.get_image(self.path + '.png')
        self.image = pygame.transform.scale(self.image, (int(Global.boardImgRect.width/10), int(Global.boardImgRect.height/10)))
        self.rect  = self.image.get_rect()
        self.__place__(screen)
        self.availableMoves = []
        self.isKing = False
        self.isSelected = False
        self.placeHolders = {}

    # select the piece and show all of its available moves
    def select(self, screen):
        self.findMoves()
        self.isSelected = True
        self.resize(screen)
        for move in self.availableMoves:
            x, y = move
            # placeHolderImg = pygame.transform.scale(Global.get_image(os.path.join('Assets', 'placeHolder' + str(Global.placeHolderType) + '.png')), (int(Global.boardImgRect.width/13), int(Global.boardImgRect.height/13)))
            # placeHolderRect = placeHolderImg.get_rect()
            # placeHolderRect.center = (Global.boardImgRect.left + Global.boardImgRect.width/16 + x*Global.boardImgRect.width/9.135 - Global.boardImgRect.width/9/2, Global.boardImgRect.top + Global.boardImgRect.height/16 + (9-y)*Global.boardImgRect.height/9.14- Global.boardImgRect.height/9.14/2)
            placeHolder = self.PlaceHolder(x,y)
            screen.blit(placeHolder.image, placeHolder.rect)
            Global.toUpdate.append(placeHolder.rect)
            self.placeHolders[placeHolder] = (x,y)
    
    # deselect the piece and stop showing all of its available moves
    def deselect(self, screen):
        self.isSelected = False
        for Object in self.placeHolders.keys():
            ############# WHY DOES THIS NOT WORK ?!?!?!?!? ##############
            # screen.blit(Global.boardImg, Global.boardImgRect, (rect.left-Global.boardImgRect.left, rect.top-Global.boardImgRect.top, rect.width, rect.height)) # blit section of board image over the placeholder
            screen.blit(Global.boardImg, Global.boardImgRect)
            Global.toUpdate.append(Object.rect)
        self.placeHolders.clear()
        self.resize(screen)
    
    # move the piece to a new location on the board
    def move(self, screen, newX, newY):
        if (newX, newY) in self.availableMoves:
            # remove placeholders for available moves
            for Object in self.placeHolders.keys():
                ############# WHY DOES THIS NOT WORK ?!?!?!?!? ##############
                # screen.blit(Global.boardImg, Global.boardImgRect, (rect.left-Global.boardImgRect.left, rect.top-Global.boardImgRect.top, rect.width, rect.height)) # blit section of board image over the placeholder
                screen.blit(Global.boardImg, Global.boardImgRect)
                Global.toUpdate.append(Object.rect)
            self.placeHolders.clear()

            # remove old piece
            # screen.blit(Global.boardImg, Global.boardImgRect, self.rect) # TODO: MAKE THIS WORK
            screen.blit(Global.boardImg, Global.boardImgRect)
            Global.toUpdate.append(self.rect)

            # Remove old entry in dictionary
            if self.player == 1:
                del Global.Player1Dict[(self.x, self.y)]
            elif self.player == 1:
                del Global.Player1Dict[(self.x, self.y)]
            
            # change coordinates of piece
            self.x = newX
            self.y = newY
            
            # add new entry in dictionary
            if self.player == 1:
                Global.Player1Dict[(self.x, self.y)] = self
            elif self.player == 1:
                Global.Player1Dict[(self.x, self.y)] = self

            self.__place__(screen)
            Global.toUpdate.append(self.rect)
        
            self.select(screen)
        

    # find and record all available moves for this piece
    def findMoves(self):
        self.availableMoves = []
        if (self.player == 1 or self.isKing) and self.y+1 < 9:
            if self.x-1 > 0 and (self.x-1, self.y+1) not in Global.Player1Dict and (self.x-1, self.y+1) not in Global.Player2Dict:
                self.availableMoves.append((self.x-1, self.y+1))
            if self.x+1 < 9 and (self.x+1, self.y+1) not in Global.Player1Dict and (self.x+1, self.y+1) not in Global.Player2Dict:
                self.availableMoves.append((self.x+1, self.y+1))
        if (self.player == 2 or self.isKing) and self.y-1 > 0:
            if self.x-1 > 0 and (self.x-1, self.y-1) not in Global.Player1Dict and (self.x-1, self.y-1) not in Global.Player2Dict:
                self.availableMoves.append((self.x-1, self.y-1))
            if self.x+1 < 9 and (self.x+1, self.y-1) not in Global.Player1Dict and (self.x+1, self.y-1) not in Global.Player2Dict:
                self.availableMoves.append((self.x+1, self.y-1))

    # king a piece so it can move in every direction
    def king(self):
        if self.isKing == False:
            self.isKing = True
            self.path = self.path + 'K'

    # resize the pieces according to the board image size and location, and draw them in the correct locations
    def resize(self, screen):
        if self.isSelected == False:
            self.image = pygame.transform.scale(Global.get_image(self.path + '.png'), (int(Global.boardImgRect.width/10), int(Global.boardImgRect.height/10)))
        else:
            self.image = pygame.transform.scale(Global.get_image(self.path + 'H' + '.png'), (int(Global.boardImgRect.width/10), int(Global.boardImgRect.height/10)))
        self.rect = self.image.get_rect()
        self.__place__(screen)

    # place the pieces according to their x and y location on the board.
    def __place__(self, screen):
        self.rect.center = (Global.boardImgRect.left + Global.boardImgRect.width/16 + self.x*Global.boardImgRect.width/9.135 - Global.boardImgRect.width/9/2, Global.boardImgRect.top + Global.boardImgRect.height/16 + (9-self.y)*Global.boardImgRect.height/9.14- Global.boardImgRect.height/9.14/2)
        self.draw(screen)
    
    # blit the player piece image onto the screen and add the rect to the list to be updated
    def draw(self, screen):
        screen.blit(self.image, self.rect)
        Global.toUpdate.append(self.rect)
        