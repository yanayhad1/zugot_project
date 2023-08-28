import consts
import pygame
import random
import game_field

screen = pygame.display.set_mode((consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))
game_field.generate_screen_matrix()


def get_indexes_for_bushes():
    matrix_indexes = game_field.get_matrix_indexes()
    bushes_indexes = []
    for bush in range(20):
        choise = random.choice(matrix_indexes)
        screen_position = consts.screen[choise[0]][choise[1]]
        while screen_position == consts.SOLDIER or screen_position == consts.FLAG or screen_position == consts.MINE:
            choise = random.choice(matrix_indexes)
            screen_position = screen[choise[0]][choise[1]]
        bushes_indexes.append(choise)
    return bushes_indexes


def draw_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            pygame.draw.rect(screen, (0, 0, 0), (j * consts.SIZE, i * consts.SIZE, consts.SIZE - 1, consts.SIZE - 1))


def draw_mines(miens_indexes):
    screen.blit(consts.MINE, (miens_indexes[0] * consts.SIZE, miens_indexes[1] * consts.SIZE))


mines_indexes = game_field.get_random_cols_for_mines(game_field.get_matrix_indexes())
bush_indexes = get_indexes_for_bushes()
def draw_game():
    screen.fill(consts.BACKGROUND_COLOR)
    draw_matrix([[0 for _ in range(consts.NUM_COLS)] for __ in range(consts.NUM_ROWS)])
    game_field.generate_screen_matrix()
    screen.blit(consts.SOLDIER, (-15, 0))
    screen.blit(consts.FLAG, (470, 210))
    for mine in mines_indexes:
        draw_mines(mine)
    for bush in bush_indexes:
        screen.blit(consts.BUSH, (bush[0] * consts.SIZE, bush[1] * consts.SIZE))


    pygame.display.flip()
