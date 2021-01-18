import os
import pygame

WIDTH = 480
HEIGHT = 600
FPS = 60

BAR_LENGTH = WIDTH
BAR_HEIGHT = 10
BAR_UPDATE_TICK = 0.3

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
NEED_TO_REMOVE = (71, 112, 76)

GAME_FOLDER = os.path.dirname(__file__)
IMG_FOLDER = os.path.join(GAME_FOLDER, 'img')
SND_FOLDER = os.path.join(GAME_FOLDER, 'snd')

FONT_NAME = pygame.font.match_font('arial')

METEORS_FILES = ["meteorBrown_big1.png", "meteorBrown_small2.png", "meteorGrey_med1.png",
                 "meteorBrown_big2.png", "meteorBrown_tiny1.png", "meteorGrey_med2.png",
                 "meteorBrown_big3.png", "meteorBrown_tiny2.png", "meteorGrey_small1.png",
                 "meteorBrown_big4.png", "meteorGrey_big1.png", "meteorGrey_small2.png",
                 "meteorBrown_med1.png", "meteorGrey_big2.png", "meteorGrey_tiny1.png",
                 "meteorBrown_med3.png", "meteorGrey_big3.png", "meteorGrey_tiny2.png",
                 "meteorBrown_small1.png", "meteorGrey_big4.png"]

SND_FILES = ["expl3.wav", "expl6.wav"]