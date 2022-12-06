from GameObjects.common import get_neighbours
from GameObjects.fieldCell import FieldCell, EmptyCell, ShipCell
from GameObjects.ship import Ship
from GameObjects.vector2 import Vector2
from CustomExceptions import GameCustomizeException


MIN_WIDTH = 5
MAX_WIDTH = 20
MIN_HEIGHT = 5
MAX_HEIGHT = 20
class FieldProperties:
    width: int
    height: int
    ships: list[Ship]

    def __init__(self, width, height, ships: list[Ship]):
        self.width = width
        self.height = height
        self.ships = ships
        self.check_data()

    def check_data(self):
        if self.width < MIN_WIDTH or self.width > MAX_WIDTH:
            raise GameCustomizeException(f"Ширина поля должна быть в диапазоне от {MIN_WIDTH} до {MAX_WIDTH}")
        if self.height < MIN_HEIGHT or self.height > MAX_HEIGHT:
            raise GameCustomizeException(f"Высота поля должна быть в диапазоне от {MIN_HEIGHT} до {MAX_HEIGHT}")
        if len(self.ships) == 0:
            raise GameCustomizeException("Кол-во кораблей должно быть не нулевым")



class Field:
    field: list[list[FieldCell]]
    width: int
    height: int
    ships: set[Ship]
    ships_to_place: list[Ship]

    def __init__(self, field_properties: FieldProperties):
        self.field = [[EmptyCell() for __ in range(field_properties.width)] for _ in range(field_properties.height)]
        self.width = field_properties.width
        self.height = field_properties.height
        self.ships = set()
        self.ships_to_place = [Ship(ship_len=s.len) for s in field_properties.ships]

    def __getitem__(self, key: int):
        return self.field[key]

    def clear_field(self):
        self.field = [[EmptyCell() for __ in range(self.width)] for _ in range(self.height)]
        self.ships = set()

    def is_inside(self, pos: Vector2):
        return 0 <= pos.x < self.width and 0 <= pos.y < self.height

    def try_place_ship(self, ship: Ship):
        for p in ship.parts:
            if not self.is_inside(p) or not(isinstance(self[p.y][p.x], EmptyCell)):
                return False

        for p in get_neighbours(ship.parts):
            if self.is_inside(p) and not(isinstance(self[p.y][p.x], EmptyCell)):
                return False

        for p in ship.parts:
            self[p.y][p.x] = ShipCell(ship)

        ship.on_defeat = lambda: self.ship_boom(ship)
        self.ships.add(ship)
        return True

    def remove_ship(self, ship: Ship):
        if ship in self.ships:
            for pos in ship.parts:
                self[pos.y][pos.x] = EmptyCell()
            self.ships.remove(ship)

    def try_to_shoot(self, pos: Vector2):
        if not self.is_inside(pos):
            return False
        cell = self[pos.y][pos.x]
        if cell.is_shoot_down:
            return False
        cell.shoot_down()
        return True

    def ship_boom(self, ship: Ship):
        for nei_cell in get_neighbours(ship.parts):
            self.try_to_shoot(nei_cell)

    def to_string(self, show_not_shooted=True):
        s = []
        for line in self:
            s.append(" ".join([str(x) if show_not_shooted or x.is_shoot_down else '·' for x in line]))
        return "\n".join(s)

    def __repr__(self):
        return str(self)
