from typing import Union


class Vector2:
    x: int
    y: int

    def __init__(self, x: Union[int, 'Vector2'], y: int = 0):
        if isinstance(x, Vector2):
            self.x = x.x
            self.y = x.y
            return
        self.x = x
        self.y = y

    def __add__(self, other: 'Vector2') -> 'Vector2':
        return Vector2(self.x + other.x, self.y + other.y)

    def __mul__(self, quotient: float) -> 'Vector2':
        return Vector2(int(self.x * quotient), int(self.y * quotient))

    def pair(self) -> tuple[int, int]:
        return self.x, self.y

    def __hash__(self):
        return self.x.__hash__() ^ self.y.__hash__()

    def __eq__(self, other: 'Vector2'):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return "({0},{1})".format(self.x, self.y)

    def __repr__(self):
        return str(self)
