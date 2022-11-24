from GameObjects.field import Field
import ConsoleUI.gameCustomizer as GameCustomizer
import ConsoleUI.fieldCustomizer as FieldCustomizer
from CustomExceptions import GameCustomizeException
from Players.consolePlayer import ConsolePlayer


def start_game():
    players = []
    fields = []
    players.append(ConsolePlayer())
    players.append(GameCustomizer.set_opponent())
    players_count = 1
    while True:
        try:
            field_properties = FieldCustomizer.start_setting_field()
            fields.append(Field(field_properties))
            fields.append(Field(field_properties))
            players[0].set_field(*fields)
            players[1].set_field(*fields[::-1])
            players[0].on_game_start()
            players[1].on_game_start()
        except GameCustomizeException as e:
            print(f"\n\n!!{e}!!")
            print("Попробуйте указать другие игровые правила\n")
        else:
            break

    if isinstance(players[-1], ConsolePlayer):
        pass
    turn = 1
    while True:
        turn = 1 - turn
        print(f"Ход {turn + 1} игрока")
        players[turn].make_move()