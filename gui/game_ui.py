from typing import Callable
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QLabel

import gui.ui_base.game_ui as game_ui
from GameObjects.vector2 import Vector2
from gui.drag_widgets.ship_drag_widget import ShipWidget
from Game.game import Game, GameState
import gui.dialog_window as DW
from gui.ui import UI
from gui.ui_base.field_drawer import FieldDrawer


class GameUI(UI):
    def __init__(self, MainWindow: QtWidgets.QMainWindow, on_ui_change: Callable, game: Game):
        self.game = game
        self.main_window = MainWindow
        self.ui = game_ui.Ui_MainWindow()
        self.cell_size = 1
        self.on_ui_change = on_ui_change

    @staticmethod
    def setup_ui(MainWindow: QtWidgets.QMainWindow, on_ui_change: Callable, game: Game = None):
        ui = GameUI(MainWindow, on_ui_change, game)
        on_ui_change(ui)
        ui._setup_ui()
        return ui

    def _setup_ui(self):
        self.ui.setupUi(self.main_window)
        self.ui.back_button.clicked.connect(self._on_back_button_click)
        self._draw_fields()
        self.ui.second_field_label.mousePressEvent = self._on_enemy_field_click
        width, height = self.game.game_settings.field_properties.width, self.game.game_settings.field_properties.height
        self.cell_size = 500 // max(width, height)

    def _draw_fields(self):
        for lb in self.ui.first_field_label.children() + self.ui.second_field_label.children():
            lb.deleteLater()

        field1, field2 = self.game.fields
        if self.game.turn == 1:
            (field1, field2) = (field2, field1)
        width, height = self.game.game_settings.field_properties.width, self.game.game_settings.field_properties.height

        FieldDrawer.draw_field(self.ui.first_field_label, width, height)
        FieldDrawer.draw_field(self.ui.second_field_label, width, height)

        FieldDrawer.draw_objects(self.ui.first_field_label, field1)
        FieldDrawer.draw_objects(self.ui.second_field_label, field2, True)

        FieldDrawer.draw_particles(self.ui.first_field_label, field1)
        FieldDrawer.draw_particles(self.ui.second_field_label, field2)

    def _on_enemy_field_click(self, event: QtGui.QMouseEvent):
        in_label_pos = event.globalPos() - self.ui.second_field_label.mapToGlobal(QtCore.QPoint(0, 0))
        x, y = in_label_pos.x() / self.cell_size, in_label_pos.y() / self.cell_size
        x, y = round(x - 0.5), round(y - 0.5)
        self.game.turn = (self.game.turn + 1) % 2
        self.game.fields[self.game.turn].try_to_shoot(Vector2(x, y))
        self._draw_fields()

    def _on_back_button_click(self):
        DW.show_accept_window("Выйти в меню?", on_accept=self._back_to_menu)

    def _back_to_menu(self):
        from gui.menu_ui import MenuUI
        MenuUI.setup_ui(self.main_window, self.on_ui_change)

    def clear(self):
        self.ui = None

    def __del__(self):
        print("deleted", self)
