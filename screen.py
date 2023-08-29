import consts
import pygame
import game_field
import soldier

screen = pygame.display.set_mode((consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))
consts.screen = game_field.generate_screen_matrix()


def draw_matrix(matrix, with_rec):
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if not with_rec:
                matrix_element = matrix[row][col]

                if matrix_element != consts.FREE:
                    if matrix_element == consts.FLAG:
                        draw_object(consts.FLAG, (consts.WINDOW_WIDTH - 30, consts.WINDOW_HEIGHT - 40))
                    elif matrix_element == consts.BUSH:
                        draw_object(consts.BUSH, (col * consts.SIZE, row * consts.SIZE))
                    elif matrix_element == consts.SOLDIER:
                        draw_object(consts.SOLDIER, (col * consts.SIZE, row * consts.SIZE))
            else:
                pygame.draw.rect(screen, (0, 0, 0),
                                 (col * consts.SIZE, row * consts.SIZE, consts.SIZE - 1, consts.SIZE - 1))


def draw_mines(mines_indexes):
    for row_idx, col_idx in mines_indexes:
        draw_object(consts.MINE, (col_idx * consts.SIZE, row_idx * consts.SIZE))


def draw_object(object_img, object_indexes):
    screen.blit(object_img, (object_indexes[0], object_indexes[1]))


def draw_game(game_state):
    if game_state["is_mines_show"]:
        screen.fill(consts.MINES_BACKGROUND_COLOR)

        draw_matrix(consts.screen, game_state["is_mines_show"])

        draw_object(consts.SOLDIER, soldier.define_soldier_position())
        draw_object(consts.FLAG, consts.FLAG_SIZES)
        draw_mines(game_state["mines"])

    else:
        screen.fill(consts.GAME_BACKGROUND_COLOR)

        draw_matrix(consts.screen, game_state["is_mines_show"])

    pygame.display.flip()
