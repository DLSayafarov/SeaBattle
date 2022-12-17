import game_objects.common as Common
from game_objects.fieldCell import FieldCell, EmptyCell, ShipCell, CellType
from game_objects.ship import Ship
from game_objects.vector2 import Vector2


MIN_WIDTH = 5
MAX_WIDTH = 20
MIN_HEIGHT = 5
MAX_HEIGHT = 20


class FieldProperties:
    width: int
    height: int
    ships_lens: list[int]

    def __init__(self, width, height, ship_lens: list[int], mines_count: int, minesweepers_count: int):
        FieldProperties.check_data(width, height, ship_lens, mines_count, minesweepers_count)
        self.width = width
        self.height = height
        self.ships_lens = ship_lens
        self.one_cell_objects = [CellType.MineCell for _ in range(mines_count)]
        self.one_cell_objects += [CellType.MinesweeperCell for _ in range(minesweepers_count)]

    @staticmethod
    def check_data(width, height, ship_lens: list[int], mines_count: int, minesweepers_count: int):
        if width < MIN_WIDTH or width > MAX_WIDTH:
            raise Warning(f"Ширина поля должна быть в диапазоне от {MIN_WIDTH} до {MAX_WIDTH}")
        if height < MIN_HEIGHT or height > MAX_HEIGHT:
            raise Warning(f"Высота поля должна быть в диапазоне от {MIN_HEIGHT} до {MAX_HEIGHT}")
        if len(ship_lens) == 0:
            raise Warning("Кол-во кораблей должно быть не нулевым")
        if mines_count < 0:
            raise Warning("Кол-во мин должно быть неотрицательным")
        if minesweepers_count < 0:
            raise Warning("Кол-во минных тральщиков должно быть неотрицательным")


class Field:
    field: list[list[FieldCell]]
    width: int
    height: int
    ships: set[Ship]
    ships_to_place: set[Ship]
    one_cell_objects_to_place: list[FieldCell]
    one_cell_objects: list[FieldCell]

    def __init__(self, field_properties: FieldProperties):
        self.field = [[EmptyCell() for __ in range(field_properties.width)] for _ in range(field_properties.height)]
        self.width = field_properties.width
        self.height = field_properties.height
        self.ships = set()
        self.ships_to_place = set([Ship(ship_len=x) for x in field_properties.ships_lens])
        self.one_cell_objects_to_place = [FieldCell.get_by_cell_type(x)() for x in field_properties.one_cell_objects]
        self.one_cell_objects = []

    def __getitem__(self, key: int):
        return self.field[key]

    def clear_ships(self):
        for s in list(self.ships):
            self.remove_ship(s)

    def clear_ocb(self):
        for i in range(self.height):
            for j in range(self.width):
                if self[i][j].cell_type in [CellType.MineCell, CellType.MinesweeperCell]:
                    self.remove_one_cell_object(self[i][j])

    def is_inside(self, pos: Vector2):
        return 0 <= pos.x < self.width and 0 <= pos.y < self.height

    def try_place_one_cell_object(self, object_cell: FieldCell):
        x, y = object_cell.pos.x, object_cell.pos.y
        if object_cell not in self.one_cell_objects_to_place:
            return False

        if not self.is_inside(Vector2(x, y)) or self[y][x].cell_type != CellType.EmptyCell:
            return False

        for p in Common.get_neighbours(Vector2(x, y)):
            if self.is_inside(p) and self[p.y][p.x].cell_type != CellType.EmptyCell:
                return False

        self[y][x] = object_cell
        self.one_cell_objects.append(object_cell)
        self.one_cell_objects_to_place.remove(object_cell)
        return True

    def try_place_ship(self, ship: Ship):
        if ship not in self.ships_to_place:
            return False

        for p in ship.parts:
            if not self.is_inside(p) or self[p.y][p.x].cell_type != CellType.EmptyCell:
                return False

        for p in Common.get_neighbours(ship.parts):
            if self.is_inside(p) and self[p.y][p.x].cell_type != CellType.EmptyCell:
                return False

        for p in ship.parts:
            self[p.y][p.x] = ShipCell(ship)
            self[p.y][p.x].pos = p

        ship.on_defeat = lambda: self.ship_boom(ship)
        self.ships.add(ship)
        self.ships_to_place.remove(ship)
        return True

    def remove_ship(self, ship: Ship):
        if ship in self.ships:
            for pos in ship.parts:
                self[pos.y][pos.x] = EmptyCell()
            self.ships.remove(ship)
            self.ships_to_place.add(ship)

    def remove_one_cell_object(self, object_cell: FieldCell):
        if object_cell in self.one_cell_objects:
            self[object_cell.pos.y][object_cell.pos.x] = EmptyCell()
            self.one_cell_objects.remove(object_cell)
            self.one_cell_objects_to_place.append(object_cell)

    def try_to_shoot(self, pos: Vector2):
        if not self.is_inside(pos):
            return CellType.NotCell
        cell = self[pos.y][pos.x]
        if cell.is_shoot_down:
            return CellType.NotCell
        cell.shoot_down()
        return self[pos.y][pos.x].cell_type

    def ship_boom(self, ship: Ship):
        for nei_cell in Common.get_neighbours(ship.parts):
            self.try_to_shoot(nei_cell)

    def to_string(self, show_not_shooted=True):
        s = []
        for line in self:
            s.append(" ".join([str(x) if show_not_shooted or x.is_shoot_down else '·' for x in line]))
        return "\n".join(s)

    def declassified_cell(self, x: int, y: int):
        self[y][x].is_declassified = True

    def __repr__(self):
        return self.to_string()
