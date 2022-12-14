from game_objects.field import FieldProperties
from players.player_properties import PlayerProperties


class GameSettings:
    field_properties: FieldProperties
    second_player_properties: PlayerProperties

    def __init__(self, field_properties: FieldProperties, player_properties: PlayerProperties):
        self.field_properties = field_properties
        self.second_player_properties = player_properties