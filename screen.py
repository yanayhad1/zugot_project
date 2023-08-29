import consts
import pygame
import game_field
import soldier

screen = pygame.display.set_mode((consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))
consts.screen = game_field.generate_screen_matrix()


def draw_message(message, font_size, color, location):
    font = pygame.font.SysFont(consts.FONT_NAME, font_size)
    text_img = font.render(message, True, color)
    screen.blit(text_img, location)


def draw_lose_message():
    draw_message(consts.LOSE_MESSAGE, consts.LOSE_FONT_SIZE,
                 consts.LOSE_COLOR, consts.LOSE_LOCATION)


def draw_win_message():
    draw_message(consts.WIN_MESSAGE, consts.WIN_FONT_SIZE,
                 consts.WIN_COLOR, consts.WIN_LOCATION)


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


def draw_game(game_state):
    screen.fill(consts.BACKGROUND_COLOR)

    draw_matrix(consts.screen)

    if game_state["is_won"]:
        draw_win_message()
    if game_state["is_lose"]:
        draw_lose_message()

    pygame.display.flip()
