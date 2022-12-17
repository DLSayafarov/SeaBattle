from random import Random
from typing import Callable
from PyQt5 import QtWidgets, QtGui, QtCore
import gui.ui_base.game_ui as game_ui
from game.game import Game, GameState
import gui.dialog_window as DW
from game_objects.fieldCell import CellType
from gui.ui import UI
from gui.field_drawer import FieldDrawer


HIT_PHRASES = ["Есть пробитие!", "Сюдаааа!!!", "В яблочко!", "Изи", "Есть попадание!", "Подстрелил!"]
MISS_PHRASES = ["Oh sheesh", "Мимо!", "Не попал!", "Сплоховал!"]


def get_hit_phrase():
    return HIT_PHRASES[Random().randint(0, len(HIT_PHRASES) - 1)]


def get_miss_phrase():
    return MISS_PHRASES[Random().randint(0, len(MISS_PHRASES) - 1)]


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
        self.ui.first_field_label.mousePressEvent = self._on_own_field_click
        width, height = self.game.game_settings.field_properties.width, self.game.game_settings.field_properties.height
        self.cell_size = 500 // max(width, height)
        self.game.on_game_state_change = lambda: self._on_game_change()
        self.ui.accept_turn.clicked.connect(self._on_accept_turn_button_click)

    def _draw_fields(self, show_all=False):
        for lb in self.ui.first_field_label.children() + self.ui.second_field_label.children():
            lb.deleteLater()

        field1, field2 = self.game.fields
        if self.game.turn == 1:
            (field1, field2) = (field2, field1)
        width, height = self.game.game_settings.field_properties.width, self.game.game_settings.field_properties.height
        FieldDrawer.draw_field(self.ui.first_field_label, width, height)
        FieldDrawer.draw_field(self.ui.second_field_label, width, height)
        FieldDrawer.draw_objects(self.ui.first_field_label, field1)
        FieldDrawer.draw_objects(self.ui.second_field_label, field2, not show_all)
        FieldDrawer.draw_particles(self.ui.first_field_label, field1)
        FieldDrawer.draw_particles(self.ui.second_field_label, field2)

    def _on_enemy_field_click(self, event: QtGui.QMouseEvent):
        if self.game.game_state == GameState.EndGame:
            return
        self.ui.state_label.setText("")
        if self.game.game_state == GameState.Waiting:
            self.game.accept_turn_end()
            return
        in_label_pos = event.globalPos() - self.ui.second_field_label.mapToGlobal(QtCore.QPoint(0, 0))
        x, y = in_label_pos.x() / self.cell_size, in_label_pos.y() / self.cell_size
        x, y = round(x - 0.5), round(y - 0.5)
        result = self.game.try_shoot(x, y)
        if result == CellType.ShipCell:
            self.ui.state_label.setStyleSheet("color: green;")
            self.ui.state_label.setText(get_hit_phrase())
        elif result == CellType.EmptyCell:
            self.ui.state_label.setStyleSheet("color: red;")
            self.ui.state_label.setText(get_miss_phrase())

    def _on_game_change(self):
        self._draw_fields()
        if self.game.game_state == GameState.Confirmation:
            if self.game.game_settings.second_player_properties.is_real_player:
                self.ui.turn_acception_label.setText(f"Игрок {self.game.turn + 1}")
                self.ui.confirm_window.show()
        elif self.game.game_state in [GameState.Battle, GameState.Waiting]:
            self.ui.turn_label.setText(f"ход игрока {self.game.turn + 1}")
        elif self.game.game_state == GameState.EndGame:
            self.ui.state_label.setStyleSheet("color: green;")
            self.ui.state_label.setText(f"Игрок {self.game.turn + 1} победил!")
            if not self.game.game_settings.second_player_properties.is_real_player:
                self.game.turn = 0
            self._draw_fields(True)
        elif self.game.game_state == GameState.Declassifying:
            text = "кораблём" if self.game.need_declassify == CellType.ShipCell else "миной"
            self.ui.turn_label.setText(f"Выберите клетку с {text} для расскрытия")

    def _on_own_field_click(self, event: QtGui.QMouseEvent):
        if self.game.game_state != GameState.Declassifying:
            return
        in_label_pos = event.globalPos() - self.ui.first_field_label.mapToGlobal(QtCore.QPoint(0, 0))
        x, y = in_label_pos.x() / self.cell_size, in_label_pos.y() / self.cell_size
        x, y = round(x - 0.5), round(y - 0.5)
        self.game.try_declassify_cell(x, y)

    def _on_accept_turn_button_click(self):
        self.game.confirm_turn_start()
        self.ui.confirm_window.hide()

    def _on_back_button_click(self):
        DW.show_accept_window("Выйти в меню?", on_accept=self._back_to_menu)

    def _back_to_menu(self):
        from gui.menu_ui import MenuUI
        MenuUI.setup_ui(self.main_window, self.on_ui_change)

    def clear(self):
        self.ui = None
        self.game = None
        self.main_window = None
