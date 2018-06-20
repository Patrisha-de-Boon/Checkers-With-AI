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
        self.necessaryMoves = {} # maps possible location of this piece to the location of the piece it will capture to get there
        self.isKing = False
        self.isSelected = False
        self.placeHolders = {}

    def showMoves(self, screen, all = True):
        if all:
            for move in self.availableMoves:
                x, y = move
                # placeHolderImg = pygame.transform.scale(Global.get_image(os.path.join('Assets', 'placeHolder' + str(Global.placeHolderType) + '.png')), (int(Global.boardImgRect.width/13), int(Global.boardImgRect.height/13)))
                # placeHolderRect = placeHolderImg.get_rect()
                # placeHolderRect.center = (Global.boardImgRect.left + Global.boardImgRect.width/16 + x*Global.boardImgRect.width/9.135 - Global.boardImgRect.width/9/2, Global.boardImgRect.top + Global.boardImgRect.height/16 + (9-y)*Global.boardImgRect.height/9.14- Global.boardImgRect.height/9.14/2)
                placeHolder = self.PlaceHolder(x,y)
                screen.blit(placeHolder.image, placeHolder.rect)
                Global.toUpdate.append(placeHolder.rect)
                self.placeHolders[placeHolder] = (x,y)

        for move in self.necessaryMoves:
            x, y = move
            # placeHolderImg = pygame.transform.scale(Global.get_image(os.path.join('Assets', 'placeHolder' + str(Global.placeHolderType) + '.png')), (int(Global.boardImgRect.width/13), int(Global.boardImgRect.height/13)))
            # placeHolderRect = placeHolderImg.get_rect()
            # placeHolderRect.center = (Global.boardImgRect.left + Global.boardImgRect.width/16 + x*Global.boardImgRect.width/9.135 - Global.boardImgRect.width/9/2, Global.boardImgRect.top + Global.boardImgRect.height/16 + (9-y)*Global.boardImgRect.height/9.14- Global.boardImgRect.height/9.14/2)
            placeHolder = self.PlaceHolder(x,y)
            screen.blit(placeHolder.image, placeHolder.rect) # TODO: blit a different image for necessary moves
            Global.toUpdate.append(placeHolder.rect)
            self.placeHolders[placeHolder] = (x,y)

    # select the piece and show all of its available moves
    def select(self, screen, canMove = True):
        self.isSelected = True
        self.resize(screen)
        if canMove:
            if not self.necessaryMoves:
                self.showMoves(screen)
            else:
                self.showMoves(screen, False)
        #TODO: highlight red if you can't move them
    
    # deselect the piece and stop showing all of its available moves
    def deselect(self, screen, redraw = True):
        self.isSelected = False
        for Object in self.placeHolders.keys():
            ############# WHY DOES THIS NOT WORK ?!?!?!?!? ##############
            # tempRect = (Object.rect.left, Object.rect.top, Object.rect.width, Object.rect.height)
            # screen.blit(Global.boardImg, Global.boardImgRect, tempRect) # blit section of board image over the placeholder
            screen.blit(Global.boardImg, Global.boardImgRect)
            Global.toUpdate.append(Object.rect)
        self.placeHolders.clear()
        if redraw:
            self.resize(screen)
    
    # move the piece to a new location on the board
    def move(self, screen, newX, newY):
        if (newX, newY) in self.availableMoves or (newX,newY) in self.necessaryMoves:
            if self.isKing == False and (self.player == 1 and newY == 8) or (self.player == 2 and newY == 1):
                self.isSelected = False
                self.king()
            if (newX, newY) in self.availableMoves:
                self.isSelected = False
                
            else:
                toCaptureCoord = self.necessaryMoves[(newX, newY)]
                if self.player == 1:
                    toCapture = Global.Player2Dict[toCaptureCoord]
                    # remove old piece
                    screen.blit(Global.boardImg, Global.boardImgRect, toCapture.rect)
                    tempRect = (toCapture.rect.left, toCapture.rect.top, toCapture.rect.width, toCapture.rect.height)
                    Global.toUpdate.append(tempRect)
                    del Global.Player2Dict[toCaptureCoord]
                    toCapture.kill()
                elif self.player == 2:
                    toCapture = Global.Player1Dict[toCaptureCoord]
                    # remove old piece
                    screen.blit(Global.boardImg, Global.boardImgRect, toCapture.rect)
                    tempRect = (toCapture.rect.left, toCapture.rect.top, toCapture.rect.width, toCapture.rect.height)
                    Global.toUpdate.append(tempRect)
                    del Global.Player1Dict[toCaptureCoord]
                    toCapture.kill()

            for Object in self.placeHolders.keys():
                ############# WHY DOES THIS NOT WORK ?!?!?!?!? ##############
                # tempRect = (Object.rect.left, Object.rect.top, Object.rect.width, Object.rect.height)
                # screen.blit(Global.boardImg, Global.boardImgRect, tempRect) # blit section of board image over the placeholder
                screen.blit(Global.boardImg, Global.boardImgRect)
                Global.toUpdate.append(Object.rect)
            self.placeHolders.clear()

            # remove old piece
            screen.blit(Global.boardImg, Global.boardImgRect, self.rect)
            tempRect = (self.rect.left, self.rect.top, self.rect.width, self.rect.height)
            Global.toUpdate.append(tempRect)
            
            # Remove old entry in dictionary
            if self.player == 1:
                del Global.Player1Dict[(self.x, self.y)]
            elif self.player == 2:
                del Global.Player2Dict[(self.x, self.y)]
            
            # change coordinates of piece
            self.x = newX
            self.y = newY
            
            # add new entry in dictionary
            if self.player == 1:
                Global.Player1Dict[(self.x, self.y)] = self
            elif self.player == 2:
                Global.Player2Dict[(self.x, self.y)] = self

            self.__place__(screen)
        

    # find and record all available moves for this piece
    def findMoves(self, screen):
        self.availableMoves.clear()
        self.necessaryMoves.clear()
        
        if self.player == 1:
            MyPieces = Global.Player1Dict
            TheirPieces = Global.Player2Dict
        elif self.player == 2:
            MyPieces = Global.Player2Dict
            TheirPieces = Global.Player1Dict

        # if the piece can move up
        if (self.player == 1 or self.isKing) and self.y+1 < 9:
            # if the piece can move left
            if self.x-1 > 0:
                # if this player's piece is not in the upper left square
                if (self.x-1, self.y+1) not in MyPieces:
                    # if there is no piece in the upper left square, add it as a possible move
                    if (self.x-1, self.y+1) not in TheirPieces:
                        self.availableMoves.append((self.x-1, self.y+1))
                    # if you can jump over the player piece, put it as a necessary move
                    elif self.y+2 < 9:
                        if self.x-2 > 0 and (self.x-2, self.y+2) not in MyPieces and (self.x-2, self.y+2) not in TheirPieces:
                            self.necessaryMoves[(self.x-2, self.y+2)] = (self.x-1, self.y+1)
            # if the piece can move right
            if self.x+1 < 9:
                # if this player's piece is not in the upper right square
                if (self.x+1, self.y+1) not in MyPieces:
                    # if there is no piece in the upper right square, add it as a possible move
                    if (self.x+1, self.y+1) not in TheirPieces:
                        self.availableMoves.append((self.x+1, self.y+1))
                    # if you can jump over the player piece, put it as a necessary move
                    elif self.y+2 < 9:
                        if self.x+2 < 9 and (self.x+2, self.y+2) not in MyPieces and (self.x+2, self.y+2) not in TheirPieces:
                            self.necessaryMoves[(self.x+2, self.y+2)] = (self.x+1, self.y+1)

        # if the piece can move down
        if (self.player == 2 or self.isKing) and self.y-1 > 0:
            # if the piece can move left
            if self.x-1 > 0:
                # if this player's piece is not in the bottom left square
                if (self.x-1, self.y-1) not in MyPieces:
                    # if there is no piece in the bottom left square, add it as a possible move
                    if (self.x-1, self.y-1) not in TheirPieces:
                        self.availableMoves.append((self.x-1, self.y-1))
                    # if you can jump over the player piece, put it as a necessary move
                    elif self.y-2 > 0:
                        if self.x-2 > 0 and (self.x-2, self.y-2) not in MyPieces and (self.x-2, self.y-2) not in TheirPieces:
                            self.necessaryMoves[(self.x-2, self.y-2)] = (self.x-1, self.y-1)
            # if the piece can move right
            if self.x+1 < 9:
                # if this player's piece is not in the bottom right square
                if (self.x+1, self.y-1) not in MyPieces:
                    # if there is no piece in the bottom right square, add it as a possible move
                    if (self.x+1, self.y-1) not in TheirPieces:
                        self.availableMoves.append((self.x+1, self.y-1))
                    # if you can jump over the player piece, put it as a necessary move
                    elif self.y-2 > 0:
                        if self.x+2 < 9 and (self.x+2, self.y-2) not in MyPieces and (self.x+2, self.y-2) not in TheirPieces:
                            self.necessaryMoves[(self.x+2, self.y-2)] = (self.x+1, self.y-1)
            
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
        