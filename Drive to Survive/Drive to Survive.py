import pygame, sys, random
from pygame.locals import *
pygame.init()
mainClock = pygame.time.Clock()

WinHeight = 550
WinWidth = 450

windowSurface = pygame.display.set_mode((WinWidth, WinHeight), 0, 32)
pygame.display.set_caption("Drive to Survive")

Green = (0, 100, 0)
Grey = (100, 100, 100)
Black = (0, 0, 0)
White = (255, 255, 255)

blueCars = [pygame.Rect(WinWidth / 2 - 185 + 75 * random.randint(1, 3), -70, 70, 120)]
driveSpeed = 4
player = pygame.Rect(WinWidth / 2 - 35, 320, 70, 120)
redCar = pygame.image.load("redcar.gif")
blueCar = pygame.image.load("bluecar.gif")

def drawRoad():                                                                                                                     #This function draws the road and the cars onto the screen
    windowSurface.fill(Green)
    pygame.draw.rect(windowSurface, Grey, pygame.Rect(110, -4, WinWidth - 220, WinHeight + 8))
    pygame.draw.rect(windowSurface, Black, pygame.Rect(110, -4, WinWidth - 220, WinHeight + 8), 3)
    for i in range(0, 8):
        pygame.draw.line(windowSurface, White, (WinWidth / 2 + 37.5, i*70+6), (WinWidth / 2 + 37.5, i*70+56), 3)
    for i in range(0, 8):
        pygame.draw.line(windowSurface, White, (WinWidth / 2 - 37.5, i*70+6), (WinWidth / 2 - 37.5, i*70+56), 3)
    windowSurface.blit(redCar, player)
    for car in blueCars:
        windowSurface.blit(blueCar, car)

def carsMove():                                                                                                                    #Moves the blue cars and checks for collisions
    for car in blueCars:
        car.top += speed
        if player.colliderect(car):
            pygame.display.update()
            mainClock.tick(1.5)
            pygame.quit()
            sys.exit()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:                                                                                                   #This controls movement of the red car
            if event.key == K_LEFT and player.left > 115:
                player.left -= 37
                drawRoad()
                carsMove()
                pygame.display.update()
                mainClock.tick(30)
                player.left -= 38
            if event.key == K_RIGHT and player.right < WinWidth - 115:
                player.left += 37
                drawRoad()
                carsMove()
                pygame.display.update()
                mainClock.tick(30)
                player.left += 38

    if blueCars[0].top > WinHeight:                                                                                                 #Adds new blue cars when they reach the bottom of the screen
        blueCars.clear()
        for i in range(0, random.randint(1, 2)):
            blueCars.append(pygame.Rect(WinWidth / 2 - 185 + 75 * random.randint(1, 3), -70, 70, 120))

    speed = round(driveSpeed)

    carsMove()

    driveSpeed += 0.005
    drawRoad()
    pygame.display.update()
    mainClock.tick(40) 