import pygame

NUM_ROWS = 25
NUM_COLS = 50

SIZE = 10

WINDOW_WIDTH = NUM_COLS * SIZE
WINDOW_HEIGHT = NUM_ROWS * SIZE

BACKGROUND_COLOR = (0, 255, 0)

screen = []
MINE = pygame.image.load("./bin/mine.png")
MINE = pygame.transform.scale(MINE, (30, 10))
FLAG = pygame.image.load("./bin/flag.png")
SOLDIER = pygame.image.load("./bin/soldier.png")
SOLDIER = pygame.transform.scale(SOLDIER, (40, 20))

