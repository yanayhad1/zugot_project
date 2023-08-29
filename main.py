import database
import screen
import consts
import game_field
import soldier
import pygame
import time

game_state = {
    "is_game_running": True,
    "mines": [],
    "is_mines_show": False,
    "mines_show_count": 0,
    "is_won": False,
    "is_lose": False,

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

    # print(consts.screen)
    # print(mines_indexes, soldier.find_soldier_body_index(), soldier.find_soldier_legs_index())

    while game_state["is_game_running"]:
        if game_state["is_won"] or game_state["is_lose"]:
            time.sleep(3)
            break

        handle_user_events()

        if soldier.is_won():
            game_state["is_won"] = True
        if soldier.is_lose():
            game_state["is_lose"] = True

        screen.draw_game(game_state)

        if game_state["is_mines_show"]:
            time.sleep(2)
            game_state["is_mines_show"] = False

    pygame.quit()


def handle_user_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_state["is_game_running"] = False

        if game_state["is_won"] or game_state["is_lose"]:
            continue

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
            elif event.key == pygame.K_a: # key 'a'
                start = time.time()
        if event == pygame.KEYUP:
            if event == pygame.K_1:
                STOP = time.time()
                sec = start - STOP
                print(sec)



if __name__ == '__main__':
    main()
