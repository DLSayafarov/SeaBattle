import enum


class Difficulty(enum.IntEnum):
    Easy = 0
    Hard = 1


class PlayerProperties:
    is_real_player: bool
    bot_game_difficulty: Difficulty
    bot_ship_placing_difficulty: Difficulty
