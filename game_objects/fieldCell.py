import enum
from abc import ABC
from game_objects.ship import Ship
from game_objects.vector2 import Vector2


class CellType(enum.IntEnum):
    EmptyCell = 0
    ShipCell = 1
    MineCell = 2
    MinesweeperCell = 3
    NotCell = 69


class FieldCell(ABC):
    cell_type: CellType
    is_shoot_down: bool = False
    char = " "
    char_shooted = " "
    is_declassified = False
    pos: Vector2

    def __init__(self, pos=Vector2(-1, -1)):
        self.pos = pos

    def shoot_down(self):
        if self.is_shoot_down:
            raise Warning("Already shoot down")
        self.is_shoot_down = True
        self.is_declassified = True

    def __str__(self):
        return [self.char, self.char_shooted][self.is_shoot_down]

    @staticmethod
    def get_by_cell_type(cell_type: CellType):
        return CELL_BY_TYPE[cell_type]


class EmptyCell(FieldCell):
    char = "·"
    char_shooted = "®"
    cell_type = CellType.EmptyCell


class ShipCell(FieldCell):
    ship: Ship
    char = "O"
    char_shooted = "@"
    cell_type = CellType.ShipCell

    def shoot_down(self):
        super().shoot_down()
        self.ship.shoot_down()

    def __init__(self, ship: Ship):
        super().__init__()
        self.ship = ship


class MineCell(FieldCell):
    char = "b"
    char_shooted = "B"
    cell_type = CellType.MineCell


class MinesweeperCell(FieldCell):
    char = "m"
    char_shooted = "M"
    cell_type = CellType.MinesweeperCell


CELL_BY_TYPE = {CellType.EmptyCell: EmptyCell,
                CellType.ShipCell: ShipCell,
                CellType.MineCell: MineCell,
                CellType.MinesweeperCell: MinesweeperCell}
