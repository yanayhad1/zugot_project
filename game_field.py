import consts
import soldier
import random


def generate_screen_matrix():
    return [[consts.FREE for _ in range(consts.NUM_COLS)] for __ in range(consts.NUM_ROWS)]


def get_matrix_indexes():
    screen_indexes = []
    for row in range(len(consts.screen)):
        for col in range(len(consts.screen[row])):
            screen_indexes.append((row, col))
    return screen_indexes


# def get_random_cols_for_mines(screen_indexes):
#     mines_indexes = []
#     for mine in range(20):
#         random_chose = random.choice(screen_indexes)
#         screen_image = consts.screen[random_chose[0]][random_chose[1]]
#         while screen_image == consts.SOLDIER or screen_image == consts.FLAG:
#             random_chose = random.choice(screen_indexes)
#             screen_image = consts.screen[random_chose[0]][random_chose[1]]
#         mines_indexes.append(random_chose
#                              )
#     return mines_indexes


def get_indexes_for_object():
    matrix_indexes = get_matrix_indexes()
    object_indexes = []

    for object_index in range(20):
        choice = random.choice(matrix_indexes)
        if choice[1] in [49, 48]:
            choice = (choice[0], choice[1]-2)

        screen_position = consts.screen[choice[0]][choice[1]]

        while choice in soldier.find_soldier_legs_index(soldier.define_soldier_position()) or choice in soldier.find_soldier_body_index(soldier.define_soldier_position()) or screen_position == consts.FLAG or screen_position == consts.MINE or screen_position == consts.BUSH:
            choice = random.choice(matrix_indexes)
            screen_position = consts.screen[choice[0]][choice[1]]

        object_indexes.append(choice)

    return object_indexes


def put_objects_in_screen(object_img , objects_indexes):
    for object_index in objects_indexes:
        consts.screen[object_index[0]][object_index[1]] = object_img


def check_index_for_flag_overlap(index):
    return consts.screen[index[0]][index[1]] == consts.FLAG


def check_index_for_mine_overlap(index):
    return consts.screen[index[0]][index[1]] == consts.MINE
