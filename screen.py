import consts
import pygame

screen = pygame.display.set_mode((consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))


def draw_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            pygame.draw.rect(screen, (0, 0, 0), (j * consts.SIZE, i * consts.SIZE, consts.SIZE - 1, consts.SIZE - 1))


def draw_mines(miens_indexes):
    for row_idx, col_idx in miens_indexes:
        screen.blit(consts.MINE, (row_idx * consts.SIZE, col_idx * consts.SIZE))


def draw_game():
    screen.fill(consts.BACKGROUND_COLOR)

    draw_matrix([[0 for _ in range(consts.NUM_COLS)] for __ in range(consts.NUM_ROWS)])

    draw_mines([(10, 10), (5, 5)])

    pygame.display.flip()
