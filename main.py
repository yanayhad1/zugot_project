import time

import screen
import consts
import game_field
import soldier
import pygame

game_state = {
    "is_game_running": True,
    "mines": [],
    "is_mines_show": False,
    "mines_show_count": 0
}


def main():
    pygame.init()
    consts.screen = game_field.generate_screen_matrix()
    consts.screen[0][0] = consts.SOLDIER
    consts.screen[-1][-1] = consts.FLAG
    mines_indexes = game_field.get_indexes_for_object()
    game_field.put_objects_in_screen(consts.MINE, mines_indexes)
    game_state["mines"] = mines_indexes
    bush_indexes = game_field.get_indexes_for_object()
    game_field.put_objects_in_screen(consts.BUSH, bush_indexes)

    while game_state["is_game_running"]:
        handle_user_events()

        screen.draw_game(game_state)

        if game_state["is_mines_show"]:
            time.sleep(2)
            game_state["is_mines_show"] = False

    pygame.quit()


def handle_user_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_state["is_game_running"] = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                soldier.move_soldier(consts.UP)
            elif event.key == pygame.K_DOWN:
                soldier.move_soldier(consts.DOWN)
            elif event.key == pygame.K_LEFT:
                soldier.move_soldier(consts.LEFT)
            elif event.key == pygame.K_RIGHT:
                soldier.move_soldier(consts.RIGHT)
            elif event.key == pygame.K_SPACE:
                if game_state["mines_show_count"] == 0:
                    game_state["is_mines_show"] = True
                    game_state["mines_show_count"] = 1


if __name__ == '__main__':
    main()
