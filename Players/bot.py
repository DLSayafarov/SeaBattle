from GameObjects.field import Field
from player_properties import PlayerProperties, Difficulty
from bot_strategies import BotGameStrategy, BotShipPlacementStrategy, \
    get_bot_game_strategy, get_bot_ship_placement_strategy


class Bot:
    own_field: Field
    other_field: Field
    game_strategy: BotGameStrategy
    ship_placement_strategy: BotShipPlacementStrategy

    def __init__(self, own_field: Field, other_field: Field, player_properties: PlayerProperties):
        self.own_field = own_field
        self.other_field = other_field
        self.game_strategy = get_bot_game_strategy(player_properties.bot_game_difficulty)\
            .__init__(self.own_field, self.other_field)
        self.ship_placement_strategy = get_bot_ship_placement_strategy(player_properties.bot_ship_placing_difficulty)\
            .__init__(self.own_field, self.other_field)

    def make_move(self):
        self.game_strategy.make_move()

    def place_ships(self):
        self.ship_placement_strategy.place_ships()
