from GameObjects.field import Field


class Player:
    own_field: Field
    other_field: Field

    def __init__(self, own_field: Field, other_field: Field):
        self.turn_delay = 1.5
        self.own_field = own_field
        self.other_field = other_field

    def make_move(self):
        pass
