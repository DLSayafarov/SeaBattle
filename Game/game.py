import enum
from typing import Callable, Union

from Game.game_settings import GameSettings
from GameObjects.field import Field, Ship, Vector2
from GameObjects.automatic_ship_placer import AutomaticShipPlacer
from Players.player import Player
from Players.bot import Bot


class GameState(enum.IntEnum):
    Menu = 0
    ShipPlacing = 1
    Confirmation = 2
    Battle = 3


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
        if self.game_settings.second_player_properties.is_real_player:
            self.player2 = Player(self.fields[1], self.fields[0])
        else:
            self.player2 =Bot(self.fields[1], self.fields[0], game_settings.second_player_properties)

    def start(self):
        self.game_state = GameState.ShipPlacing

    def place_ship_automatically(self):
        if self.game_state != GameState.ShipPlacing:
            raise Exception("Ошибка состояний игры")
        if not AutomaticShipPlacer.try_set_ships_randomly(field=self.fields[self.turn]):
            raise Warning("Не удалось расставить корабли автоматически")

    def try_place_ship(self, ship: Ship, x=-1, y=-1):
        if self.game_state != GameState.ShipPlacing:
            raise Exception("Ошибка состояний игры")
        if x != -1:
            ship.pos = Vector2(x, y)
        return self.fields[self.turn].try_place_ship(ship)

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
