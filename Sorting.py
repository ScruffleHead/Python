import pygame, sys, random
from pygame.locals import *
pygame.init()

RED = (255, 0, 0)
ORANGE = (255, 112, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
LIGHTBLUE = (0, 255, 255)
DARKBLUE = (0, 0, 255)
PURPLE = (153, 0, 255)
PINK = (247, 52, 198)
GREY = (100, 100, 100)
BROWN = (92, 54, 0)

lvl1 = ([orng, ylw, grn, ylw], [grn, orng, grn, orng], [grn, ylw, orng, ylw], [])

selected = None