import enum
from typing import Callable, Union

from game.game_settings import GameSettings
from game_objects.automatic_ship_placer import AutomaticPlacer
from game_objects.field import Field, Ship, Vector2
from game_objects.fieldCell import CellType, FieldCell
from players.bot import Bot
from players.player import Player


class GameState(enum.IntEnum):
    Menu = 0
    ShipPlacing = 1
    Waiting = 2
    Battle = 3
    Confirmation = 4
    Declassifying = 5
    EndGame = 6


class Game:
    game_settings: GameSettings
    game_state: GameState
    on_game_state_change: Callable
    turn: int
    player1: Union[Player, Bot]
    player2: Union[Player, Bot]

    def __init__(self, game_settings: GameSettings, on_game_state_change: Callable):
        self.game_settings = game_settings
        self.game_state = GameState.Menu
        self.on_game_state_change = on_game_state_change
        self.turn = 0
        self.fields = [Field(game_settings.field_properties), Field(game_settings.field_properties)]
        self.player1 = Player(self.fields[0], self.fields[1])
        self.turn_delay = 2
        self.need_declassify: CellType = None
        if self.game_settings.second_player_properties.is_real_player:
            self.player2 = Player(self.fields[1], self.fields[0])
        else:
            self.player2 = Bot(self.fields[1], self.fields[0], game_settings.second_player_properties)

    def start(self):
        self.game_state = GameState.ShipPlacing

    def place_ship_automatically(self):
        if self.game_state != GameState.ShipPlacing:
            raise Exception("Ошибка состояний игры")
        if not AutomaticPlacer.try_set_ships_randomly(field=self.get_current_player().own_field):
            raise Warning("Не удалось расставить корабли автоматически")

    def place_one_cell_objects_automatically(self):
        if self.game_state != GameState.ShipPlacing:
            raise Exception("Ошибка состояний игры")
        if not AutomaticPlacer.try_set_ocb_randomly(field=self.get_current_player().own_field):
            raise Warning("Не удалось расставить корабли автоматически")

    def try_place_ship(self, ship: Ship, x=-1, y=-1):
        if self.game_state != GameState.ShipPlacing:
            raise Exception("Ошибка состояний игры")
        if x != -1:
            ship.pos = Vector2(x, y)
        return self.get_current_player().own_field.try_place_ship(ship)

    def try_place_one_cell_object(self, object_cell: FieldCell, x=-1, y=-1):
        if self.game_state != GameState.ShipPlacing:
            raise Exception("Ошибка состояний игры")
        if x != -1:
            object_cell.pos = Vector2(x, y)
        return self.get_current_player().own_field.try_place_one_cell_object(object_cell)

    def try_remove_ship(self, ship: Ship):
        if self.game_state != GameState.ShipPlacing:
            raise Exception("Ошибка состояний игры")
        try:
            self.fields[self.turn].remove_ship(ship)
        except:
            return False
        return True

    def try_remove_one_cell_object(self, object_cell: FieldCell):
        if self.game_state != GameState.ShipPlacing:
            raise Exception("Ошибка состояний игры")
        try:
            self.fields[self.turn].remove_one_cell_object(object_cell)
        except:
            return False
        return True

    def accept_ship_placement(self):
        if self.game_state != GameState.ShipPlacing:
            raise Exception("Ошибка состояний игры")
        if len(self.fields[self.turn].ships_to_place) > 0:
            raise Warning("Не все корабли еще расставлены")
        if self.turn == 1:
            self.turn = 0
            self.game_state = GameState.Battle
        elif not self.game_settings.second_player_properties.is_real_player:
            self.player2.place_ships()
            self.game_state = GameState.Battle
        elif self.turn == 0 and self.game_settings.second_player_properties.is_real_player:
            self.turn = 1
        self.on_game_state_change()
        self._make_move()

    def get_current_player(self):
        return [self.player1, self.player2][self.turn]

    def try_declassify_cell(self, x: int, y: int):
        if self.game_state != GameState.Declassifying:
            raise Exception("Ошибка состояний игры")
        if (not self.get_current_player().own_field.is_inside(Vector2(x, y))
                or self.need_declassify != self.get_current_player().own_field[y][x].cell_type
                or self.get_current_player().own_field[y][x].is_declassified):
            return False
        self.get_current_player().own_field[y][x].is_declassified = True
        self._change_state_to(GameState.Waiting)
        return True

    def try_shoot(self, x, y, from_bot_req=False) -> CellType:
        if isinstance(self.get_current_player(), Bot) and not from_bot_req:
            return CellType.NotCell
        if self.game_state != GameState.Battle:
            return CellType.NotCell
        res = self.get_current_player().other_field.try_to_shoot(Vector2(x, y))
        if res == CellType.NotCell:
            return res

        if res == CellType.MineCell:
            self._on_cell_declassifying(CellType.ShipCell)
            return CellType.MineCell

        if res == CellType.MinesweeperCell:
            self._on_cell_declassifying(CellType.MineCell)
            return CellType.MinesweeperCell

        if res == CellType.ShipCell:
            if any(1 for x in self.get_current_player().other_field.ships if x.is_alive):
                self._change_state_to(GameState.Battle)
                return CellType.ShipCell
            self.end_game()
            return CellType.NotCell
        self._change_state_to(GameState.Waiting)
        return CellType.EmptyCell

    def accept_turn_end(self):
        self.turn = (self.turn + 1) % 2
        self._change_state_to(GameState.Confirmation)
        if self.game_state == GameState.Confirmation:
            self._make_move()

    def _change_state_to(self, state: GameState):
        if self.game_state == GameState.EndGame:
            return
        self.game_state = state
        self.on_game_state_change()

    def confirm_turn_start(self):
        self._change_state_to(GameState.Battle)

    def _make_move(self):
        cur_player = self.get_current_player()
        if cur_player.is_real_player:
            return
        self.confirm_turn_start()
        res = CellType.ShipCell
        while res == CellType.ShipCell:
            x, y = cur_player.make_move()
            res = self.try_shoot(x, y, True)
        self.accept_turn_end()
        self.confirm_turn_start()

    def _on_cell_declassifying(self, cell_type: CellType):
        if not self._is_any_to_declassify(cell_type):
            return
        self.need_declassify = cell_type
        self._change_state_to(GameState.Declassifying)
        if not self.get_current_player().is_real_player:
            x, y = self.get_current_player().declassify_cell(cell_type)
            self.try_declassify_cell(x, y)
            return

    def _is_any_to_declassify(self, cell_type: CellType):
        field = self.get_current_player().own_field
        if cell_type == CellType.MineCell:
            for x in field.one_cell_objects:
                if x.cell_type == cell_type and not x.is_declassified:
                    return True
        elif cell_type == CellType.ShipCell:
            for x in field.ships:
                for pos in x.parts:
                    if not field[pos.y][pos.x].is_declassified:
                        return True
        return False

    def end_game(self):
        self._change_state_to(GameState.EndGame)
