import consts
import pygame

import game_field


def put_soldier_on_screen():
    consts.screen[1][1] = consts.SOLDIER


def define_soldier_position():
    for row in range(len(consts.screen)):
        for col in range(len(consts.screen[row])):
            position = consts.screen[row][col]
            if position == consts.SOLDIER:
                return row, col


def find_soldier_legs_index(soldier_position):
    # soldier_position = define_soldier_position()
    soldier_legs_position = [(soldier_position[0] + 3, soldier_position[1]),
                             (soldier_position[0] + 3, soldier_position[1] + 1),
                             (soldier_position[0] + 3, soldier_position[1] + 2)]
    return soldier_legs_position


def find_soldier_body_index(soldier_position):
    soldier_body_index = [soldier_position,
                          (soldier_position[0], soldier_position[1] + 1),
                          (soldier_position[0], soldier_position[1] + 2),
                          (soldier_position[0] + 1, soldier_position[1]),
                          (soldier_position[0] + 1, soldier_position[1] + 1),
                          (soldier_position[0] + 1, soldier_position[1] + 2),
                          (soldier_position[0] + 2, soldier_position[0]),
                          (soldier_position[0] + 2, soldier_position[1] + 1),
                          (soldier_position[0] + 2, soldier_position[1] + 2)]
    return soldier_body_index


def check_if_soldier_out_of_matrix(soldier_position):
    output = False
    screen_indexes = game_field.get_matrix_indexes()
    soldier_body = find_soldier_body_index(soldier_position)
    soldier_legs = find_soldier_legs_index(soldier_position)
    for body_part in soldier_body:
        if body_part not in screen_indexes:
            output = True
    for leg in soldier_legs:
        if leg not in screen_indexes:
            output = True
    return output


def move_soldier(mode):
    current_soldier_index = define_soldier_position()

    if mode == consts.UP:
        if not check_if_soldier_out_of_matrix((current_soldier_index[0] - 1, current_soldier_index[1])):
            consts.screen[current_soldier_index[0]][current_soldier_index[1]] = consts.FREE
            consts.screen[current_soldier_index[0] - 1][current_soldier_index[1]] = consts.SOLDIER
    elif mode == consts.DOWN:
        if not check_if_soldier_out_of_matrix((current_soldier_index[0] + 1, current_soldier_index[1])):
            consts.screen[current_soldier_index[0]][current_soldier_index[1]] = consts.FREE
            consts.screen[current_soldier_index[0] + 1][current_soldier_index[1]] = consts.SOLDIER
    elif mode == consts.RIGHT:
        if not check_if_soldier_out_of_matrix((current_soldier_index[0], current_soldier_index[1] + 1)):
            consts.screen[current_soldier_index[0]][current_soldier_index[1]] = consts.FREE
            consts.screen[current_soldier_index[0]][current_soldier_index[1] + 1] = consts.SOLDIER
    elif mode == consts.LEFT:
        if not check_if_soldier_out_of_matrix((current_soldier_index[0], current_soldier_index[1] - 1)):
            consts.screen[current_soldier_index[0]][current_soldier_index[1]] = consts.FREE
            consts.screen[current_soldier_index[0]][current_soldier_index[1] - 1] = consts.SOLDIER


def is_lose():
    output = False
    legs_position = find_soldier_legs_index(define_soldier_position())
    for leg in legs_position:
        if consts.screen[leg[0]][leg[1]] == consts.MINE:
            output = True
            break
    return output


def is_won():
    output = False
    counter = 0
    body_position = find_soldier_body_index(define_soldier_position())
    for body_part in body_position:
        if body_part in consts.FLAG_INDEXES:
            output = True
            break
    return output

