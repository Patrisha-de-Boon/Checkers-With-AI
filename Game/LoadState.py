import pygame  # load pygame keywords
import sys     # let python use the file system
import os      # help python identify the OS
import Global  # includes variables meant to be common to multiple files
import SaveAndLoad.py

# redraw the entire screen and everything on it
def redraw(screen, saveTextList):
    Global.drawBackground(screen)
    screen.blit(titleText, titleRect)
    for save in saveTextList:
        screen.blit(save[0], save[1])

# Note, this relies on a max of 9 save files (numbered 1 through 9)
def resize(screen, SaveList):
    screen = pygame.display.set_mode((width, height), pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.RESIZABLE)
    Global.Width = width
    Global.Height = height

    global titleText
    global titleRect

    titleSize = int(Global.Height/12)
    titleFont = pygame.font.Font(os.path.join('Assets', 'Fonts', 'ahellya.ttf'), titleSize)
    titleText = titleFont.render("Load A Save Game", True, Global.BLACK)
    titleRect = pygame.Rect(Global.Width/2 - titleFont.size("Load A Save Game")[0], Global.Width.Height/16, titleFont.size("Load A Save Game")[0], titleFont.size("Load A Save Game")[1])

    saveSize = int(Global.Height/16)
    saveFont = pygame.font.Font(os.path.join('Assets', 'Fonts', 'ahellya.ttf'), saveSize)
    
    saveTextList = []
    i = 1
    for save in SaveList:
        saveNum = 0
        if save[5] =! '.':
            saveNum = int(save[4] + save[5])
        else:
            saveNum = int(save[4])
        saveText = saveFont.render("Save" + str(saveNum), True, Global.BLACK)
        saveRect = pygame.Rect(titleRect.left, titleRect.bottom + saveSize*2*i, saveFont.size("Save" + str(saveNum))[0], saveFont.size("Save" + str(saveNum))[1])
        saveTextList.append((saveText, saveRect))

# process user input through mouse input
def processMouseInput(screen, event, saveTextList):
    deselect = True
    for save in SaveTextList:
        if save[1].collide(event.pos):
            deselect = False
            return True, save[0]

    if deselect:
        

# run the load menu state
def RunLoadMenu(screen):
    SaveList = os.listdir(os.path.join('Saves'))
    if not SaveList:
        return 1 # go back to the menu state if there are no saves
    
    saveTextList = resize(screen, SaveList)
    redraw(screen, saveTextList)
