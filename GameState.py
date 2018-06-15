import pygame  # load pygame keywords
import sys     # let python use the file system
import os      # help python identify the OS
import Global  # includes variables meant to be common to multiple files



def RunGame(screen):
    while not Quit:
        # display the board behind everything centered in the screen
        screen.blit(Global.boardImg, (Global.Height/2 - boardImg.rect.height/2, Global.Width/2 -  boardImg.rect.width/2))



        
