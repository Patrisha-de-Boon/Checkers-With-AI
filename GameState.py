import pygame  # load pygame keywords
import sys     # let python use the file system
import os      # help python identify the OS
import Global


def RunGame(screen, boardImg):
    while not Quit:
        # display the board behind everything centered in the screen
        screen.blit(boardImg, (Global.Height/2 - boardImg.rect.height/2, Global.Width/2 -  boardImg.rect.width/2))

        
