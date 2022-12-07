from abc import ABC
from GameObjects.field import Field
from GameObjects.automatic_ship_placer import AutomaticShipPlacer
from Players.difficulty import Difficulty


class BotGameStrategy(ABC):
    def __init__(self, own_field: Field, other_field: Field):
        self.own_field = own_field
        self.other_field = other_field

    def make_move(self):
        pass


class BotShipPlacementStrategy(ABC):
    def __init__(self, own_field: Field, other_field: Field):
        self.own_field = own_field
        self.other_field = other_field

    def place_ships(self):
        pass


class BotGameStrategyEasy(BotGameStrategy):
    def make_move(self):
        pass


class BotGameStrategyHard(BotGameStrategy):
    def make_move(self):
        pass


class BotShipPlacementStrategyEasy(BotShipPlacementStrategy):
    def place_ships(self):
        while AutomaticShipPlacer.try_set_ships_randomly(self.own_field):
            pass


class BotShipPlacementStrategyHard(BotShipPlacementStrategy):
    def place_ships(self):
        pass


__BOT_GAME_STRATEGY_BY_DIFFICULTY = {Difficulty.Easy: BotGameStrategyEasy,
                                     Difficulty.Hard: BotGameStrategyHard}
__BOT_SHIP_PLACEMENT_STRATEGY_BY_DIFFICULTY = {Difficulty.Easy: BotShipPlacementStrategyEasy,
                                               Difficulty.Hard: BotShipPlacementStrategyHard}


def get_bot_game_strategy(difficulty: Difficulty):
    return __BOT_GAME_STRATEGY_BY_DIFFICULTY[difficulty]


def get_bot_ship_placement_strategy(difficulty: Difficulty):
    return __BOT_SHIP_PLACEMENT_STRATEGY_BY_DIFFICULTY[difficulty]

