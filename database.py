import pandas as pd
import consts


def get_game_data(game_num):
    game_data = pd.read_csv(consts.DATABASE_NAME)

    return {
        "screen": game_data["screen"][game_num],
        "mines": game_data["mines"][game_num],
        "soldier_position": game_data["soldier_position"][game_num]
    }


def get_whole_data_game():
    game_data = pd.read_csv(consts.DATABASE_NAME)

    whole_data_game = []

    for data_num in range(len(game_data)):
        whole_data_game.append({"screen": game_data["screen"][data_num], "mines": game_data["mines"][data_num],
                                "soldier_position": game_data["soldier_position"][data_num]})

    return whole_data_game
