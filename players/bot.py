from game_objects.field import Field
from game_objects.fieldCell import CellType
from players.player_properties import PlayerProperties
from players.bot_strategies import BotGameStrategy, BotShipPlacementStrategy, \
    get_bot_game_strategy, get_bot_ship_placement_strategy


class Bot:
    own_field: Field
    other_field: Field
    game_strategy: BotGameStrategy
    ship_placement_strategy: BotShipPlacementStrategy
    is_real_player = False

    def __init__(self, own_field: Field, other_field: Field, player_properties: PlayerProperties):
        self.turn_delay = 0
        self.own_field = own_field
        self.other_field = other_field
        self.game_strategy = (get_bot_game_strategy(player_properties.bot_game_difficulty)
                              (self.own_field, self.other_field))
        self.ship_placement_strategy = (get_bot_ship_placement_strategy(player_properties.bot_ship_placing_difficulty)
                                        (self.own_field, self.other_field))

    def make_move(self):
        return self.game_strategy.make_move()

    def place_ships(self):
        self.ship_placement_strategy.place_ships()

    def declassify_cell(self, cell_type: CellType):
        if cell_type == cell_type.ShipCell:
            for ship in self.own_field.ships:
                for pos in ship.parts:
                    if not self.own_field[pos.y][pos.x].is_declassified:
                        return pos.x, pos.y
        if cell_type == cell_type.MineCell:
            for mine in self.own_field.one_cell_objects:
                if mine.cell_type == CellType.MineCell and not mine.is_declassified:
                    pos = mine.pos
                    return pos.x, pos.y
        raise Exception("Ошибка запроса раскрытия клетки")
