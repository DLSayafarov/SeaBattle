from GameObjects.vector2 import Vector2
from typing import Union


def get_neighbours(pos: Union[Vector2, list[Vector2]]):
    if isinstance(pos, Vector2):
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                yield pos + Vector2(i, j)
    else:
        for x in get_neighbours_for_cells(pos):
            yield x


def get_neighbours_for_cells(cells):
    pos_s = set(cells)
    for p in cells:
        for nei in get_neighbours(p):
            if nei not in pos_s:
                pos_s.add(nei)
                yield nei
