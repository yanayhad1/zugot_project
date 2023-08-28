import screen
import pygame

game_state = {
    "is_game_running": True
}


def main():
    pygame.init()

    while game_state["is_game_running"]:
        handle_user_events()

        screen.draw_game()

    pygame.quit()


def handle_user_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_state["is_game_running"] = False


if __name__ == '__main__':
    main()
