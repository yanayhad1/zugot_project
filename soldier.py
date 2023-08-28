import consts
import pygame

import game_field


def put_soldier_on_screen():
    consts.screen[1][1] = consts.SOLDIER


def define_soldier_position():
    soldier_position = (0, 0)
    for row in range(len(consts.screen)):
        for col in range(len(consts.screen[row])):
            position = consts.screen[row][col]
            if position == consts.SOLDIER:
                soldier_position = (row - 1, col - 1)
    return soldier_position


def find_soldier_legs_index():
    soldier_position = define_soldier_position()
    soldier_legs_position = [(soldier_position[0] - 3, soldier_position[1]),
                             (soldier_position[0] - 3, soldier_position[1] + 1)]
    return soldier_legs_position


def find_soldier_body_index():
    soldier_position = define_soldier_position()
    soldier_body_index = [soldier_position, (soldier_position[0], soldier_position[1] + 1),
                          (soldier_position[0] + 1, soldier_position[1]),
                          (soldier_position[0] + 1, soldier_position[1] + 1)]
    return soldier_body_index


def check_if_soldier_out_of_matrix():
    output = False
    screen_indexes = game_field.get_matrix_indexes()
    soldier_body = find_soldier_body_index()
    soldier_legs = find_soldier_legs_index()
    for body_part in soldier_body:
        if body_part not in screen_indexes:
            output = True
    for leg in soldier_legs:
        if leg not in screen_indexes:
            output = True
    return output
