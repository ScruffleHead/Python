import pygame, sys, random, time
from pygame.locals import *
pygame.init()

WinWidth = 500
WinHeight = 400
TubeDistance = 40

windowSurface = pygame.display.set_mode((WinWidth, WinHeight), 0, 32)
pygame.display.set_caption("Box Sorting")

RED = (255, 0, 0)
ORANGE = (255, 112, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
LIGHTBLUE = (0, 255, 255)
DARKBLUE = (0, 0, 255)
PURPLE = (153, 0, 255)
PINK = (247, 52, 198)
GREY = (50, 50, 50)
BROWN = (92, 54, 0)
LIGHTGREY = (204, 204, 204)
BLACK = (0, 0, 0)

lvl1 = (["orng", "ylw", "grn", "ylw"],                              #These tuples store the layout of each level. Each smaller list inside of it is a tube
["grn", "orng", "grn", "orng"],
["grn", "ylw", "orng", "ylw"],
["blnk", "blnk", "blnk", "blnk"],
["blnk", "blnk", "blnk", "blnk"])

lvl2 = (["blu", "orng", "grn", "ylw"],
["blu", "ylw", "orng", "grn"],
["blu", "orng", "ylw", "orng"],
["blu", "ylw", "grn", "grn"],
["blnk", "blnk", "blnk", "blnk"],
["blnk", "blnk", "blnk", "blnk"])

lvl3 = (["ylw", "blu", "grn", "prpl"],
["blu", "prpl", "grn", "prpl"],
["orng", "ylw", "grn", "grn"],
["orng", "ylw", "blu", "ylw"],
["orng", "orng", "blu", "prpl"],
["blnk", "blnk", "blnk", "blnk"],
["blnk", "blnk", "blnk", "blnk"])

lvl4 = (["pnk", "orng", "ylw", "grn"],
["red", "prpl", "blu", "grn"],
["red", "ylw", "grn", "orng"],
["red", "blu", "blu", "orng"],
["prpl", "ylw", "prpl", "pnk"],
["blu", "red", "pnk", "prpl"],
["grn", "ylw", "orng", "pnk"],
["blnk", "blnk", "blnk", "blnk"],
["blnk", "blnk", "blnk", "blnk"])

lvl5 = (["grn", "red", "prpl", "blu"],
["orng", "ylw", "grn", "blu"],
["orng", "blu", "red", "prpl"],
["red", "ylw", "ylw", "prpl"],
["blu", "orng", "orng", "prpl"],
["grn", "ylw", "red", "grn"],
["blnk", "blnk", "blnk", "blnk"],
["blnk", "blnk", "blnk", "blnk"])

lvl6 = (["blu", "red", "ylw", "red"],
["prpl", "grn", "grn", "blu"],
["ylw", "pnk", "orng", "grn"],
["orng", "prpl", "pnk", "prpl"],
["ylw", "blu", "pnk", "orng"],
["red", "pnk", "prpl", "ylw"],
["orng", "grn", "blu", "red"],
["blnk", "blnk", "blnk", "blnk"],
["blnk", "blnk", "blnk", "blnk"])

lvl7 = (["ylw", "red", "prpl", "grn"],
["ylw", "ylw", "blu", "prpl"],
["brwn", "blu", "prpl", "pnk"],
["pnk", "red", "orng", "ylw"],
["prpl", "orng", "red", "grn"],
["pnk", "brwn", "grn", "pnk"],
["grn", "brwn", "red", "blu"],
["blu", "orng", "brwn", "orng"],
["blnk", "blnk", "blnk", "blnk"],
["blnk", "blnk", "blnk", "blnk"])

lvl8 = (["pnk", "prpl", "orng", "brwn"],
["red", "blu", "ltblu", "orng"],
["ltblu", "pnk", "blu", "red"],
["orng", "ylw", "pnk", "blu"],
["ylw", "ltblu", "orng", "prpl"],
["brwn", "ltblu", "prpl", "red"],
["grn", "grn", "prpl", "blu"],
["red", "pnk", "grn", "brwn"],
["ylw", "ylw", "grn", "brwn"],
["blnk", "blnk", "blnk", "blnk"],
["blnk", "blnk", "blnk", "blnk"])

lvl9 = (["orng", "grn", "brwn", "grn"],
["prpl", "ylw", "orng", "ylw"],
["blu", "brwn", "pnk", "orng"],
["prpl", "red", "pnk", "grn"],
["ylw", "red", "prpl", "pnk"],
["blu", "brwn", "blu", "red"],
["ylw", "prpl", "grn", "red"],
["blu", "pnk", "brwn", "orng"],
["blnk", "blnk", "blnk", "blnk"],
["blnk", "blnk", "blnk", "blnk"])

lvl10 = (["brwn", "red", "pnk", "grn"],
["pnk", "prpl", "brwn", "ltblu"],
["grn", "orng", "red", "ylw"],
["prpl", "ylw", "ltblu", "prpl"],
["blu", "brwn", "grn", "ltblu"],
["orng", "blu", "blu", "ylw"],
["red", "orng", "grn", "red"],
["pnk", "orng", "ylw", "prpl"],
["brwn", "blu", "pnk", "ltblu"],
["blnk", "blnk", "blnk", "blnk"],
["blnk", "blnk", "blnk", "blnk"])

win = (["brwn", "brwn", "brwn", "ltblu"],
["ltblu", "ltblu", "ltblu", "brwn"],
["ltblu", "ltblu", "brwn", "ltblu"],
["ltblu", "ltblu", "ltblu", "brwn"],
["brwn", "brwn", "brwn", "ltblu"],
["ltblu", "ltblu", "ltblu", "ltblu"],
["brwn", "brwn", "brwn", "brwn"],
["ltblu", "ltblu", "ltblu", "ltblu"],
["brwn", "brwn", "brwn", "brwn"],
["ltblu", "brwn", "ltblu", "ltblu"],
["ltblu", "ltblu", "brwn", "ltblu"],
["brwn", "brwn", "brwn", "brwn"])

colours = {"orng": ORANGE, "ylw": YELLOW, "blu": DARKBLUE, "grn": GREEN, "prpl": PURPLE, "ltblu": LIGHTBLUE, "red": RED, "pnk": PINK, "brwn": BROWN}

lvls = (lvl1, lvl2, lvl3, lvl4, lvl5, lvl6, lvl7, lvl8, lvl9, lvl10, win)

pos = 0
selected = None
lvl = list(lvl1)
lvlnum = 0

def findX(x):                                               #Returns the x coordinate of a desired tube
    return WinWidth/2 - (len(lvl) * TubeDistance/2 - TubeDistance/2) + x * TubeDistance

def drawBox(x, colour, y):                                  #Draws a box at the desired coordinates
    if colour != "blnk":
        pygame.draw.rect(windowSurface, colours[colour], pygame.Rect(x-10, y-10, 20, 20))
        pygame.draw.rect(windowSurface, BLACK, pygame.Rect(x-10, y-10, 20, 20), 2)

def drawTube(x):                                            #Draws a tube at the desired coordinates
    pygame.draw.line(windowSurface, LIGHTGREY, (x - 15, WinHeight / 2 + 50), (x - 15, WinHeight / 2 - 50), 3)
    pygame.draw.line(windowSurface, LIGHTGREY, (x - 15, WinHeight / 2 + 50), (x + 15, WinHeight / 2 + 50), 3)
    pygame.draw.line(windowSurface, LIGHTGREY, (x + 15, WinHeight / 2 + 50), (x + 15, WinHeight / 2 - 50), 3)

def drawWindow():                                           #Function that draws everything onto the screen
    windowSurface.fill(GREY)
    position = findX(pos)
    for i in range(0, len(lvl)):
        drawTube(findX(i))
    pygame.draw.polygon(windowSurface, LIGHTGREY, ((position-10, WinHeight/2 - 70), (position+10, WinHeight/2 - 70), (position, WinHeight/2 - 60)))
    for b in range(0, len(lvl)):
        for s in range(0, 4):
            drawBox(findX(b), lvl[b][s], WinHeight/2 - 40 + 25*s)
    if selected != None:
        drawBox(findX(pos), selected, WinHeight/2 - 85)
    pygame.display.update()

def findTop():                                              #Function that finds the highest box in the selected tube
    for i in range(0, 4):
        if lvl[pos][i] != "blnk":
            return i
        elif i == 3:
            return None

def detectWin():
    for l in lvl:
        sameBox = l[0]
        for i in range(1, 4):
            if sameBox != l[i]:
                return False
    return True

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                if pos > 0:
                    pos -= 1
            if event.key == K_RIGHT:
                if pos < len(lvl)-1:
                    pos += 1
            if event.key == K_DOWN:
                if selected == None:
                    if findTop() != None:
                        selected = lvl[pos][findTop()]
                        lvl[pos][findTop()] = "blnk"
                        originTube = pos
                elif lvl[pos][0] == "blnk":
                    if findTop() == None or lvl[pos][findTop()] == selected or pos == originTube:
                        for i in range(0, 4):
                            if lvl[pos][i] != "blnk":
                                break
                        if findTop() != None:
                            lvl[pos][i-1] = selected
                        else:
                            lvl[pos][i] = selected
                        selected = None
            if event.key == K_q and lvlnum != 10:
                lvlnum += 1
                lvl = list(lvls[lvlnum])
                pos = 0
    drawWindow()
    if detectWin():
        time.sleep(1)
        lvlnum += 1
        lvl = list(lvls[lvlnum])
        pos = 0