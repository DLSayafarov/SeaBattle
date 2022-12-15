from game_objects.fieldCell import FieldCell, ShipCell, EmptyCell, CellType
from game_objects.rotation import Rotation
from game_objects.ship import Ship


def get_ship_image_path(ship: Ship):
    return f"gui/sprites/ships/{ship.len}{'h' * int(ship.rotation == Rotation.Horizontal)}.png"


def get_particle_by_cell(field_cell: FieldCell):
    if field_cell.is_shoot_down:
        if isinstance(field_cell, EmptyCell):
            return f"gui/sprites/miss.png"
        if isinstance(field_cell, ShipCell):
            return f"gui/sprites/hit.png"
    return None


def get_one_cell_object_by_cell_type(cell_type: CellType):
    if cell_type == CellType.MineCell:
        return f"gui/sprites/mine.png"
    if cell_type == CellType.MinesweeperCell:
        return f"gui/sprites/minesweeper.png"