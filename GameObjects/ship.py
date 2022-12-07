from GameObjects.vector2 import Vector2
from GameObjects.rotation import Rotation
from typing import Callable

MAX_SHIP_LEN = 10


class Ship:
    pos: Vector2
    hp: int
    _len: int
    rotation: Rotation
    # _parts: list[Vector2]

    @property
    def parts(self):
        return list(self.get_parts())

    @property
    def len(self):
        return self._len

    def get_parts(self):
        p = (0, 1) if self.rotation == Rotation.Vertical else (1, 0)
        vp = Vector2(p[0], p[1])
        cp = Vector2(self.pos)
        i = 0
        while i < self._len:
            yield cp
            i += 1
            cp += vp

    def __init__(self, pos: Vector2 = Vector2(0, 0), ship_len: int = None, rotation: Rotation = Rotation.Horizontal,
                 on_defeat: Callable = None):
        self._len = ship_len
        self.rotation = rotation
        self.pos = pos
        self.hp = ship_len
        self.on_defeat = on_defeat
        self._parts = []
        if self._len > MAX_SHIP_LEN or self._len < 0:
            raise Warning(f"Длина корабля должна быть в пределах от 1 до {MAX_SHIP_LEN}")

    def shoot_down(self):
        self.hp -= 1
        if self.hp == 0:
            self.on_defeat()
