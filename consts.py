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
FLAG_INDEXES = [(21, 46), (22, 46), (23, 46), (21, 47), (22, 47), (23, 47), (21, 48), (22, 48), (23, 48), (21, 49), (22, 49), (23, 49)]
LOSE_MESSAGE = "You Lost!"
LOSE_FONT_SIZE = int(0.15 * WINDOW_WIDTH)
LOSE_COLOR = (0,0,0)
LOSE_LOCATION = \
    (0.2 * WINDOW_WIDTH, WINDOW_HEIGHT / 2 - (LOSE_FONT_SIZE / 2))
WIN_MESSAGE = "You Won!"
WIN_FONT_SIZE = LOSE_FONT_SIZE
WIN_COLOR = (89, 89, 89)
WIN_LOCATION = \
    (0.2 * WINDOW_WIDTH, WINDOW_HEIGHT / 2 - (WIN_FONT_SIZE / 2))

DATABASE_NAME = './database.csv'

FONT_NAME = "Calibri"
