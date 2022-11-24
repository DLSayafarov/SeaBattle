from random import Random
from GameObjects.fieldCell import FieldCell, ShipCell, EmptyCell
from GameObjects.field import Field, FieldProperties
from GameObjects.ship import Ship
from CustomExceptions import GameCustomizeException
from GameObjects.vector2 import Vector2
from GameObjects.enums import Rotation

classic_ship_set = [Ship(ship_len=4),
                    Ship(ship_len=3), Ship(ship_len=3),
                    Ship(ship_len=2), Ship(ship_len=2), Ship(ship_len=2),
                    Ship(ship_len=1), Ship(ship_len=1), Ship(ship_len=1), Ship(ship_len=1)]


classic_game_rules_field_properties = FieldProperties(10, 10, classic_ship_set)


def start_setting_field():
    print("Игровых поле:\n1. Классическое\n2. Кастомное")
    game_rules_type = int(input())
    if game_rules_type == 1:
        print("Установлены классические игровые правила\n")
        return classic_game_rules_field_properties

    print("Кастомные так кастомные, давай настраивать")
    print("Высота поля: ", end="")
    h = int(input())
    print("Ширина поля: ", end="")
    w = int(input())
    print("Набор кораблей:\n1. Классический\n2. Кастомный")
    ships_set_type = int(input())
    ship_set = classic_ship_set
    if ships_set_type == 2:
        print("Введите через пробел длины кораблей")
        ship_lens = map(int, input().split())
        ship_set = [Ship(ship_len=x) for x in ship_lens]
    if sum([s.len for s in ship_set]) * 2 + 2 > h * w:
        raise GameCustomizeException("Поле слишком мало для данного набора кораблей")
    print("Установлены кастомные игровые правила\n")
    return FieldProperties(w, h, ship_set)


MAX_PRINT_SHIPS_SET_LINE_LENGTH = 20


def print_ships_set(ships_set: list[Ship]):
    ships_lens = sorted([s.len for s in ships_set], reverse=True)
    ll = 0
    for x in ships_lens:
        ll += x + 2
        if ll >= MAX_PRINT_SHIPS_SET_LINE_LENGTH:
            ll = x + 2
            print()
        print(f"{ShipCell.char}" * x, end="  ")
    print()


def start_setting_ships_on_field(field: Field):
    print("Набор кораблей:")
    print_ships_set(field.ships_to_place)
    print("Расставить корабли\n1. Автоматически\n2. В ручную")
    ship_setting_type = int(input())
    if ship_setting_type == 1:
        if not(try_set_ships_randomly(field)):
            raise GameCustomizeException("Не получилось расставить корабли автоматически")
        print("Корабли расставлены автоматически\n")
    else:
        set_ships_manual(field)


SETTING_SHIP_CHAR = 'Œ'


def print_field_with_setting_ship(field: Field, setting_ship: Ship):
    output_list = [[str(x) for x in field_line] for field_line in field]
    for part in setting_ship.parts:
        if field.is_inside(part):
            output_list[part.y][part.x] = SETTING_SHIP_CHAR
    for line in output_list:
        print("\t".join(line))


D_VECTORS = [Vector2(0, -1), Vector2(-1, 0), Vector2(0, 1), Vector2(1, 0)]


def set_ships_manual(field: Field):
    control_guide = "Ручная расстановка кораблей:\nWASD - перемещение корабля, R - вращение\nQE - переключение меж кораблями\nEnter - поставить корабль\nF - закончить расстановку\n"
    cur_ship = field.ships_to_place[0]
    cur_ship_index = 0
    while True:
        print(control_guide)
        print()
        print("Выбранный корабль: ", SETTING_SHIP_CHAR * cur_ship.len)
        print_field_with_setting_ship(field, cur_ship)
        command = input().strip().lower()
        if command == "":
            command = "enter"

        if command in "wasd":
            d = D_VECTORS["wasd".index(command)]
            new_pos = Vector2((cur_ship.pos.x + d.x) % field.width, (cur_ship.pos.y + d.y) % field.height)
            cur_ship.pos = new_pos
            continue

        if command == 'r':
            cur_ship.rotation = Rotation((cur_ship.rotation + 1) % 2)
            continue

        if command == "enter":
            if not(field.try_place_ship(cur_ship)):
                print("!!Невозможно поставить корабль сюда!!")
                input()
            else:
                cur_ship_index = (cur_ship_index + 1) % len(field.ships_to_place)
                cur_ship = field.ships_to_place[cur_ship_index]
                field.remove_ship(cur_ship)
            continue

        if command in "qe":
            if not(field.try_place_ship(cur_ship)):
                cur_ship.pos = Vector2(0, 0)
            d = -1 if command == "q" else 1
            cur_ship_index = (cur_ship_index + d) % len(field.ships_to_place)
            cur_ship = field.ships_to_place[cur_ship_index]
            field.remove_ship(cur_ship)
            continue

        if command == "f":
            if len(field.ships) == len(field.ships_to_place) - 1 and field.try_place_ship(cur_ship):
                break
            print("\n!!Не все корабли расставлены!!")
            input()
            continue

    print("Корабли успешно расставлены!")


ATTEMPTS_TO_PLACE_SHIP = 100
ATTEMPTS_TO_RANDOMLY_SET_SHIPS = 1000


def try_place_ship(field: Field, ship: Ship):
    rand = Random()
    for i in range(ATTEMPTS_TO_PLACE_SHIP):
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


def try_set_ships_randomly(field: Field):
    for j in range(ATTEMPTS_TO_RANDOMLY_SET_SHIPS):
        set_suc = True
        for ship in field.ships_to_place:
            if not try_place_ship(field, ship):
                set_suc = False
                field.clear_field()
                break
        if set_suc:
            return True
    return False





