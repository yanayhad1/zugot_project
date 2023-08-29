import pygame

NUM_ROWS = 25
NUM_COLS = 50

SIZE = 10

WINDOW_WIDTH = NUM_COLS * SIZE
WINDOW_HEIGHT = NUM_ROWS * SIZE

GAME_BACKGROUND_COLOR = (1, 50, 32)
MINES_BACKGROUND_COLOR = (40, 40, 40)

UP = 'UP'
DOWN = 'DOWN'
LEFT = 'LEFT'
RIGHT = 'RIGHT'

screen = []
FREE = 'free'
MINE = pygame.image.load("./bin/mine.png")
MINE = pygame.transform.scale(MINE, (30, 10))
FLAG = pygame.image.load("./bin/flag.png")
FLAG = pygame.transform.scale(FLAG, (30, 40))
FLAG_SIZES = (WINDOW_WIDTH - 30, WINDOW_HEIGHT - 40)
SOLDIER = pygame.image.load("./bin/soldier.png")
SOLDIER = pygame.transform.scale(SOLDIER, (40, 40))
BUSH = pygame.image.load("bin/grass.png")
BUSH = pygame.transform.scale(BUSH, (30, 30))

