from Players.player import Player
from GameObjects.field import Field
from GameObjects.fieldCell import FieldCell, ShipCell, EmptyCell
import ConsoleUI.fieldCustomizer as consoleUI
import random
import time
from GameObjects.vector2 import Vector2

COMMANDS_TO_SHOOT = ["Куда стрелять босс?", "Координаты для наводчика:",
                     "В какой квадрат бить?", "Буква-цифра?", "Куда палить?", "Командир, диктуй цифры"]
RAND = random.Random()
LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


class ConsolePlayer(Player):
    top_letters: str

    def set_field(self, field: Field, opponent_field: Field):
        self.field = field
        self.opponent_field = opponent_field
        self.top_letters = ' '.join(LETTERS[:self.field.width])

    def on_game_start(self):
        consoleUI.start_setting_ships_on_field(self.field)

    def print_fields(self):
        f1 = self.field.to_string().split('\n')
        f2 = self.opponent_field.to_string(show_not_shooted=False).split('\n')
        print(f"\t{self.top_letters}\t\t\t{self.top_letters}")
        for i in range(len(f1)):
            print(f"{i + 1}\t{f1[i]}\t\t{i + 1}\t{f2[i]}")

    def make_move(self):
        print("Enter - продолжить")
        input()
        while True:
            self.print_fields()
            coord = self.read_coord()
            if coord is not None:
                if not(self.opponent_field.try_to_shoot(coord)):
                    print("\n\n\n\n\n\n\n\nУже стреляли туда!")
                else:
                    if isinstance(self.opponent_field[coord.y][coord.x], ShipCell):
                        print("\n\n\n\n\n\n\n\nЕсть пробитие!")
                        continue
                    else:
                        break
            print("\n\n\n\n\n\n\n\nКоординаты неверны, босс! Давайте еще раз!")


        print("\n\n\n\n\n\n\n\nМимо!")
        self.print_fields()
        time.sleep(2)
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

    def read_coord(self):
        print(COMMANDS_TO_SHOOT[RAND.randint(0, len(COMMANDS_TO_SHOOT) - 1)])
        target_input = input().upper().strip()
        if len(target_input) < 2:
            return None
        let = LETTERS.find(target_input[0])
        if let == -1:
            return None
        ni = 0
        for i in range(len(target_input)):
            if target_input[i].isnumeric():
                ni = i
                break
        if ni is None:
            return None
        num = 0
        while ni < len(target_input) and target_input[ni].isnumeric():
            num = 10 * num + int(target_input[ni])
            ni += 1
        num -= 1
        if 0 <= let < self.field.width and 0 <= num < self.field.height:
            return Vector2(let, num)

        return None
