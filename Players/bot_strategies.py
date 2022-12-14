import enum
from abc import ABC
from random import Random
from GameObjects.field import Field
from GameObjects.automatic_ship_placer import AutomaticShipPlacer
from GameObjects.fieldCell import ShipCell
from GameObjects.rotation import Rotation
from GameObjects.ship import Ship
from GameObjects.vector2 import Vector2
from Players.difficulty import Difficulty


class StrategyStage(enum.IntEnum):
    Searching = 0
    Hunting = 1


class BotGameStrategy(ABC):
    def __init__(self, own_field: Field, other_field: Field):
        self.own_field = own_field
        self.other_field = other_field
        self.stage = StrategyStage.Searching

    def make_move(self) -> (int, int):
        pass


class BotShipPlacementStrategy(ABC):
    def __init__(self, own_field: Field, other_field: Field):
        self.own_field = own_field
        self.other_field = other_field

    def place_ships(self):
        pass


class BotGameStrategyEasy(BotGameStrategy):
    def make_move(self) -> (int, int):
        if self.stage == StrategyStage.Searching:
            return self.search()
        return self.hunt()

    def search(self):
        available_cells = []
        for i in range(self.other_field.height):
            for j in range(self.other_field.width):
                if not self.other_field.field[i][j].is_shoot_down:
                    available_cells.append((j, i))
        x, y = available_cells[Random().randint(0, len(available_cells) - 1)]
        if isinstance(self.other_field.field[y][x], ShipCell):
            self.stage = StrategyStage.Hunting
        return x, y

    def hunt(self) -> (int, int):
        shot_down_ship_cells = []
        for i in range(self.other_field.height):
            for j in range(self.other_field.width):
                cell = self.other_field.field[i][j]
                if (cell.is_shoot_down
                        and isinstance(cell, ShipCell)
                        and cell.ship.is_alive):
                    shot_down_ship_cells.append((j, i))

        if len(shot_down_ship_cells) == 0:
            self.stage = StrategyStage.Searching
            return self.search()

        av_dir = []
        if len(shot_down_ship_cells) == 1:
            x, y = shot_down_ship_cells[0]
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if (i * j == 0
                            and self.other_field.is_inside(Vector2(x + j, y + i))
                            and not self.other_field.field[y + i][x + j].is_shoot_down):
                        av_dir.append((j, i))
        else:
            dy = int(shot_down_ship_cells[0][1] - shot_down_ship_cells[1][1] != 0)
            dx = int(shot_down_ship_cells[0][0] - shot_down_ship_cells[1][0] != 0)
            av_dir = [(dx, dy), (-dx, dy), (dx, -dy), (-dx, -dy)]

        print(shot_down_ship_cells)
        print(av_dir)
        for j, i in av_dir:
            for x, y in shot_down_ship_cells:
                if (self.other_field.is_inside(Vector2(x + j, y + i))
                        and not self.other_field.field[y + i][x + j].is_shoot_down):
                    return x + j, y + i

        raise Exception("Bot strategy exception")


class BotGameStrategyHard(BotGameStrategy):
    def make_move(self):
        return self.get_most_possible()

    def get_most_possible(self):
        alive_ships_lens = [x.len for x in self.other_field.ships if x.is_alive]
        probabilities = [[0] * self.other_field.width for _ in range(self.other_field.height)]
        for i in range(self.other_field.height):
            for j in range(self.other_field.width):
                for ship_len in alive_ships_lens:
                    for rot in [Rotation.Horizontal, Rotation.Vertical]:
                        ship = Ship(ship_len=ship_len, rotation=rot, pos=Vector2(j, i))
                        probability = self.get_ship_probability(ship)
                        if probability == 0:
                            continue
                        for pv in ship.parts:
                            probabilities[pv.y][pv.x] += probability
        prop, x, y = 0, 0, 0
        for i in range(self.other_field.height):
            for j in range(self.other_field.width):
                if probabilities[i][j] > prop and not self.other_field.field[i][j].is_shoot_down:
                    prop = probabilities[i][j]
                    x = j
                    y = i
        [print(*x, sep='\t') for x in probabilities]
        return x, y

    def get_ship_probability(self, ship):
        prop = 1
        for v in ship.parts:
            x, y = v.x, v.y
            if not self.other_field.is_inside(v):
                return 0
            cell = self.other_field.field[y][x]
            if cell.is_shoot_down:
                if isinstance(cell, ShipCell) and cell.ship.is_alive:
                    prop += 9999
                else:
                    return 0
        return prop





class BotShipPlacementStrategyEasy(BotShipPlacementStrategy):
    def place_ships(self):
        while not AutomaticShipPlacer.try_set_ships_randomly(self.own_field):
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

