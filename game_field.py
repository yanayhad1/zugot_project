import consts
import random


def generate_screen_matrix(screen=consts.screen):
    for rows in range(25):
        screen.append([])
    for row in screen:
        for cols in range(50):
            row.append([])


def get_matrix_indexes(screen=consts.screen):
    screen_indexes = []
    for row in range(len(screen)):
        for col in range(len(screen[row])):
            screen_indexes.append((row, col))
    return screen_indexes


def get_random_cols_for_mines(screen_indexes):
    mines_indexes = []
    for mine in range(20):
        random_chose = random.choice(screen_indexes)
        screen_image = consts.screen[random_chose[0]][random_chose[1]]
        while screen_image == soldier or screen_image == flag:
            random_chose = random.choice(screen_indexes)
            screen_image = consts.screen[random_chose[0]][random_chose[1]]
        mines_indexes.append(random_chose
                             )
    return mines_indexes
