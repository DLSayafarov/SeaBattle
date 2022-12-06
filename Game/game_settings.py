from GameObjects.field import FieldProperties
from Players.player_properties import PlayerProperties

class GameSettings:
    field_properties: FieldProperties
    player_properties: PlayerProperties

    def __init__(self, field_properties: FieldProperties, player_properties: PlayerProperties):
        self.field_properties = field_properties
        self.player_properties = player_properties