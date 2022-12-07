from GameObjects.field import Field
from Players.___consolePlayer import ConsolePlayer


def set_opponent():
    print("Тип соперника:\n1.Другой игрок (hot seat)\n2.Бот")
    tp = int(input())
    if tp == 1:
        return ConsolePlayer()
    else:
        raise Exception()
