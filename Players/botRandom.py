from GameObjects.field import Field
from

class Player:
    field: Field
    opponent_field: Field

    def make_move(self):
        pass

    def set_field(self, field: Field, opponent_field: Field):
        self.field = field
        self.opponent_field = opponent_field

    def on_game_start(self):
        consoleUI.start_setting_ships_on_field(self.field)

    def print_fields(self):
        f1 = self.field.to_string().split('\n')
        f2 = self.opponent_field.to_string(show_not_shooted=False).split('\n')
        print(f"\t{self.top_letters}\t\t\t{self.top_letters}")
        for i in range(len(f1)):
            print(f"{i + 1}\t{f1[i]}\t\t{i + 1}\t{f2[i]}")