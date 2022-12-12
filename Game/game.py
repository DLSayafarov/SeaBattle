import asyncio
import enum
import threading
import time
from typing import Callable, Union

from Game.game_settings import GameSettings
from GameObjects.field import Field, Ship, Vector2
from GameObjects.automatic_ship_placer import AutomaticShipPlacer
from GameObjects.fieldCell import ShipCell
from Players.player import Player
from Players.bot import Bot


class ShootResult(enum.IntEnum):
    Miss = 0
    Ship = 1
    Err = 2


class GameState(enum.IntEnum):
    Menu = 0
    ShipPlacing = 1
    Waiting = 2
    Battle = 3
    Confirmation = 4
    EndGame = 5


class Game:
    game_settings: GameSettings
    game_state: GameState
    on_game_state_change: Callable
    turn: int
    player1: Player
    player2: Union[Player, Bot]

    def __init__(self, game_settings: GameSettings, on_game_state_change: Callable):
        self.game_settings = game_settings
        self.game_state = GameState.Menu
        self.on_game_state_change = on_game_state_change
        self.turn = 0
        self.fields = [Field(game_settings.field_properties), Field(game_settings.field_properties)]
        self.player1 = Player(self.fields[0], self.fields[1])
        self.turn_delay = 2
        if self.game_settings.second_player_properties.is_real_player:
            self.player2 = Player(self.fields[1], self.fields[0])
        else:
            self.player2 = Bot(self.fields[1], self.fields[0], game_settings.second_player_properties)

    def start(self):
        self.game_state = GameState.ShipPlacing

    def place_ship_automatically(self):
        if self.game_state != GameState.ShipPlacing:
            raise Exception("Ошибка состояний игры")
        if not AutomaticShipPlacer.try_set_ships_randomly(field=self.get_current_player().own_field):
            raise Warning("Не удалось расставить корабли автоматически")

    def try_place_ship(self, ship: Ship, x=-1, y=-1):
        if self.game_state != GameState.ShipPlacing:
            raise Exception("Ошибка состояний игры")
        if x != -1:
            ship.pos = Vector2(x, y)
        return self.get_current_player().own_field.try_place_ship(ship)

    def try_remove_ship(self, ship: Ship):
        if self.game_state != GameState.ShipPlacing:
            raise Exception("Ошибка состояний игры")
        try:
            self.fields[self.turn].remove_ship(ship)
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

    def get_current_player(self):
        return [self.player1, self.player2][self.turn]

    def try_shoot(self, x, y) -> ShootResult:
        if self.game_state != GameState.Battle:
            return ShootResult.Err
        suc = self.get_current_player().other_field.try_to_shoot(Vector2(x, y))
        if not suc:
            return ShootResult.Err

        if isinstance(self.get_current_player().other_field.field[y][x], ShipCell):
            if any(1 for x in self.get_current_player().other_field.ships if x.hp > 0):
                return ShootResult.Ship
            self._change_state_to(GameState.EndGame)
            return ShootResult.Err
        threading.Thread(target=self._change_turn_with_delay).start()
        return ShootResult.Miss

    def _change_turn_with_delay(self):
        self._change_state_to(GameState.Waiting)
        time.sleep(self.turn_delay)
        self._change_turn()

    def _change_turn(self):
        if isinstance(self.player2, Player):
            self._change_state_to(GameState.Confirmation)
        self.turn = (self.turn + 1) % 2

    def _change_state_to(self, state: GameState):
        self.game_state = state
        self.on_game_state_change()

    def confirm_turn_changing(self):
        if self.game_state != GameState.Confirmation:
            raise Exception("Ошибка состояний игры")
        self._change_state_to(GameState.Battle)


