from GameObjects.ship import Ship


class FieldCell:
    is_shoot_down: bool = False
    char = " "
    char_shooted = " "

    def shoot_down(self):
        if self.is_shoot_down:
            raise Warning("Already shoot down")
        self.is_shoot_down = True

    def __str__(self):
        return [self.char, self.char_shooted][self.is_shoot_down]


class EmptyCell(FieldCell):
    char = "·"
    char_shooted = "®"


class ShipCell(FieldCell):
    ship: Ship
    char = "O"
    char_shooted = "@"

    def shoot_down(self):
        if self.is_shoot_down:
            raise Warning("Already shoot down")
        self.is_shoot_down = True
        self.ship.shoot_down()

    def __init__(self, ship: Ship):
        self.ship = ship
