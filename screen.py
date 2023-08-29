import consts
import pygame
import game_field
import soldier

screen = pygame.display.set_mode((consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))
consts.screen = game_field.generate_screen_matrix()


def draw_matrix(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            matrix_element = matrix[row][col]

            # pygame.draw.rect(screen, (0, 0, 0),
            # (col * consts.SIZE, row * consts.SIZE, consts.SIZE - 1, consts.SIZE - 1))

            if matrix_element != consts.FREE:
                if matrix_element == consts.FLAG:
                    draw_object(consts.FLAG, (consts.WINDOW_WIDTH - 30, consts.WINDOW_HEIGHT - 40))
                elif matrix_element == consts.MINE:
                    draw_object(consts.MINE, (col * consts.SIZE, row * consts.SIZE))
                else:
                    draw_object(matrix_element, (col * consts.SIZE, row * consts.SIZE))


def draw_object(object_img, object_indexes):
    screen.blit(object_img, (object_indexes[0], object_indexes[1]))


def draw_game():
    screen.fill(consts.BACKGROUND_COLOR)

    draw_matrix(consts.screen)

    pygame.display.flip()
