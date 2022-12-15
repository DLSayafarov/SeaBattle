from game_objects.field import Field, Ship, Vector2
from game_objects.fieldCell import CellType
from game_objects.rotation import Rotation
from random import Random


class AutomaticPlacer:
    ATTEMPTS_TO_PLACE = 100
    ATTEMPTS_TO_RANDOMLY_SET = 100

    @staticmethod
    def try_place_ship(field: Field, ship: Ship):
        rand = Random()
        for i in range(AutomaticPlacer.ATTEMPTS_TO_PLACE):
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
        for j in range(AutomaticPlacer.ATTEMPTS_TO_RANDOMLY_SET):
            set_suc = True
            while field.ships_to_place:
                ship = next(iter(field.ships_to_place))
                if not AutomaticPlacer.try_place_ship(field, ship):
                    set_suc = False
                    field.clear_ships()
                    break
            if set_suc:
                return True
        return False

    @staticmethod
    def try_place_ocb(field: Field, ocb_type: CellType):
        rand = Random()
        for i in range(AutomaticPlacer.ATTEMPTS_TO_PLACE):
            x = rand.randint(0, field.width - 1)
            y = rand.randint(0, field.height - 1)
            res = field.try_place_one_cell_object(ocb_type, x, y)
            if res:
                return True
        return False

    @staticmethod
    def try_set_ocb_randomly(field: Field):
        for j in range(AutomaticPlacer.ATTEMPTS_TO_RANDOMLY_SET):
            set_suc = True
            while field.one_cell_objects_to_place:
                ocb_type = next(iter(field.one_cell_objects_to_place))
                if not AutomaticPlacer.try_place_ocb(field, ocb_type):
                    set_suc = False
                    field.clear_ocb()
                    break
            if set_suc:
                return True
        return False
