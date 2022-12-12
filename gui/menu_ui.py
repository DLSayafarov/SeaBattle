from typing import Callable
from PyQt5 import QtWidgets, QtGui, QtCore
from Game.game_settings import GameSettings, FieldProperties, PlayerProperties
from Players.difficulty import Difficulty
import gui.ui_base.menu_ui as menu_ui
from Game.game import Game
import gui.dialog_window as DW
from gui.ui import UI


class MenuUI(UI):
    def __init__(self, MainWindow: QtWidgets.QMainWindow, on_ui_change: Callable):
        self.main_window = MainWindow
        self.ui = menu_ui.Ui_MainWindow()
        self.on_ui_change = on_ui_change

    def _get_game_and_field_settings(self):
        try:
            game_field_width = int(self.ui.game_field_width.text())
            game_field_height = int(self.ui.game_field_height.text())
            ships_lens = [int(x) for x in self.ui.ships_lens.text().split()]
            self.ui.mines_count
            self.ui.minesweepers_count
        except:
            raise Warning("Некорректные настройки")

        fp = FieldProperties(game_field_width, game_field_height, ships_lens)
        pp = PlayerProperties()
        pp.is_real_player = self.ui.second_player_hotseat_rb.isChecked()
        if not pp.is_real_player:
            pp.bot_game_difficulty = Difficulty(0 if self.ui.bot_game_difficult_easy_rb.isChecked() else 1)
            pp.bot_ship_placing_difficulty = Difficulty(0 if self.ui.bot_ship_placing_difficult_easy_rb.isChecked() else 1)

        return GameSettings(fp, pp)

    def _on_start_button_click(self):
        try:
            game_settings = self._get_game_and_field_settings()
        except Exception as e:
            DW.show_warning_window(e)
        else:
            game = Game(game_settings, lambda: None)
            game.start()
            from gui.ship_placing_ui import ShipPlacingUI
            ShipPlacingUI.setup_ui(self.main_window, self.on_ui_change, game)

    @staticmethod
    def setup_ui(MainWindow: QtWidgets.QMainWindow, on_ui_change: Callable):
        ui = MenuUI(MainWindow, on_ui_change)
        ui._setup_ui()
        on_ui_change(ui)
        return ui

    def _setup_ui(self):
        self.ui.setupUi(self.main_window)
        self.ui.second_player_bot_rb.clicked.connect(self.ui.bot_settings.show)
        self.ui.second_player_hotseat_rb.clicked.connect(self.ui.bot_settings.hide)
        self.ui.game_start_button.clicked.connect(self._on_start_button_click)

    def __del__(self):
        print("deleted", self)
