from PyQt5 import QtCore, QtGui, QtWidgets
from Game.game_settings import GameSettings, FieldProperties, PlayerProperties
from GameObjects.ship import Ship
from Players.player_properties import Difficulty
import gui.menu_ui as menu_ui
import gui.ship_placing_ui as ship_placing_ui

MENU_UI = menu_ui.Ui_MainWindow()
SHIP_PLACING_UI = ship_placing_ui.Ui_MainWindow()
MAIN_WINDOW = None

def set_game_and_field_settings():
    try:
        game_field_width = int(MENU_UI.game_field_width.text())
        game_field_height = int(MENU_UI.game_field_height.text())
        ships_lens = [int(x) for x in MENU_UI.ships_lens.text().split()]
        MENU_UI.mines_count
        MENU_UI.minesweepers_count
    except:
        raise Exception("Некорректные настройки")

    ships = [Ship(ship_len=x) for x in ships_lens]
    fp = FieldProperties(game_field_width, game_field_height, ships)
    pp = PlayerProperties()
    pp.is_real_player = MENU_UI.second_player_hotseat_rb.isChecked()
    if not pp.is_real_player:
        pp.bot_game_difficulty = Difficulty(0 if MENU_UI.bot_game_difficult_easy_rb.isChecked() else 1)
        pp.bot_ship_placing_difficulty = Difficulty(0 if MENU_UI.bot_ship_placing_difficult_easy_rb.isChecked() else 1)

    return GameSettings(fp, pp)


def on_start_button_click():
    try:
        gs = set_game_and_field_settings()
    except Exception as e:
        errorMessage = QtWidgets.QErrorMessage()
        errorMessage.showMessage(str(e))
        errorMessage.exec()
    else:
        SHIP_PLACING_UI.setupUi(MAIN_WINDOW)


def configurate_ui(MainWindow: QtWidgets.QMainWindow):
    global MAIN_WINDOW
    MAIN_WINDOW = MainWindow
    MENU_UI.setupUi(MainWindow)
    MENU_UI.second_player_bot_rb.clicked.connect(MENU_UI.bot_settings.show)
    MENU_UI.second_player_hotseat_rb.clicked.connect(MENU_UI.bot_settings.hide)
    MENU_UI.game_start_button.clicked.connect(on_start_button_click)
