from game_objects.fieldCell import FieldCell, ShipCell, EmptyCell
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
