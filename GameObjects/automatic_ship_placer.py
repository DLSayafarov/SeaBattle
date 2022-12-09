from GameObjects.field import Field, Ship, Vector2
from GameObjects.rotation import Rotation
from random import Random


class AutomaticShipPlacer:
    ATTEMPTS_TO_PLACE_SHIP = 100
    ATTEMPTS_TO_RANDOMLY_SET_SHIPS = 1000

    @staticmethod
    def try_place_ship(field: Field, ship: Ship):
        rand = Random()
        for i in range(AutomaticShipPlacer.ATTEMPTS_TO_PLACE_SHIP):
            ship.rotation = Rotation(rand.randint(0, 1))
            max_x = field.width - 1 - (ship.len - 1) * (1 - ship.rotation)
            max_y = field.height - 1 - (ship.len - 1) * ship.rotation
            x = rand.randint(0, max_x)
            y = rand.randint(0, max_y)
            ship.pos = Vector2(x, y)
            res = field.try_place_ship(ship)
            if res:
                return True
        return False

    @staticmethod
    def try_set_ships_randomly(field: Field):
        for j in range(AutomaticShipPlacer.ATTEMPTS_TO_RANDOMLY_SET_SHIPS):
            set_suc = True
            while field.ships_to_place:
                ship = next(iter(field.ships_to_place))
                if not AutomaticShipPlacer.try_place_ship(field, ship):
                    set_suc = False
                    field.clear_field()
                    break
            if set_suc:
                return True
        return False
