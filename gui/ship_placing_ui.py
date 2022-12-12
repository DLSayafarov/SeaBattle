from typing import Callable
from PyQt5 import QtWidgets, QtGui, QtCore
import gui.ui_base.ship_placing_ui as ship_placing_ui
from gui.drag_widgets.drag_widget import ShipWidget
from Game.game import Game, GameState
import gui.warning_window as WW
from gui.ui import UI


class ShipPlacingUI(UI):
    def __init__(self, MainWindow: QtWidgets.QMainWindow, on_ui_change: Callable, game: Game):
        self.game = game
        self.main_window = MainWindow
        self.ui = ship_placing_ui.Ui_MainWindow()
        self.cell_size = 1
        self.ships_widgets: list[ShipWidget] = []
        self.on_ui_change = on_ui_change

    def _on_back_button_click(self):
        from gui.menu_ui import MenuUI
        MenuUI.setup_ui(self.main_window, self.on_ui_change)
        del self

    def _on_ship_taking(self, ship_widget: ShipWidget):
        self.game.try_remove_ship(ship_widget.ship)

    def _on_ship_realise(self, ship_widget: ShipWidget):
        x, y = self._get_pos_in_field(ship_widget.pos())
        if self.game.try_place_ship(ship_widget.ship, x, y):
            pos_in_field = QtCore.QPoint(x * self.cell_size, y * self.cell_size)
            new_pos = self.ui.field_label.pos() + pos_in_field
            ship_widget.move(new_pos)
        else:
            self.ui.ship_area_layout.layout().addWidget(ship_widget)

    def _get_pos_in_field(self, ship_widget_pos: QtCore.QPoint):
        temp_pos = ship_widget_pos - self.ui.field_label.pos()
        x, y = temp_pos.x() / self.cell_size, temp_pos.y() / self.cell_size
        return round(x), round(y)

    def _on_auto_ship_place_button_click(self):
        try:
            self.game.place_ship_automatically()
        except Warning as e:
            WW.show_warning(e)
        else:
            for ship_widget in self.ships_widgets:
                in_field_pos = QtCore.QPoint(ship_widget.ship.pos.x * self.cell_size,
                                             ship_widget.ship.pos.y * self.cell_size)
                ship_widget.setParent(ship_widget.base_parent_widget)
                ship_widget.set_pixmap()
                ship_widget.move(self.ui.field_label.pos() + in_field_pos)

    def _on_reset_button_click(self):
        for ship_widget in self.ships_widgets:
            if self.game.try_remove_ship(ship_widget.ship):
                self.ui.ship_area_layout.layout().addWidget(ship_widget)

    @staticmethod
    def setup_ui(MainWindow: QtWidgets.QMainWindow, on_ui_change: Callable, game: Game = None):
        ui = ShipPlacingUI(MainWindow, on_ui_change, game)
        ui._setup_ui()
        on_ui_change(ui)
        return ui

    def _setup_ui(self):
        self.ui.setupUi(self.main_window)
        self._draw_field()
        self.ui.back_button.clicked.connect(self._on_back_button_click)
        self.ui.accept_button.clicked.connect(self._on_accept_button_click)
        self.ui.auto_ship_place_button.clicked.connect(self._on_auto_ship_place_button_click)
        self.ui.reset_button.clicked.connect(self._on_reset_button_click)
        self.ships_widgets = [ShipWidget(x, self.cell_size, self._on_ship_taking,
                                         self._on_ship_realise, self.main_window)
                              for x in self.game.fields[self.game.turn].ships_to_place]
        for x in self.ships_widgets:
            self.ui.ship_area_layout.layout().addWidget(x)

    def _draw_field(self):
        pixmap = QtGui.QPixmap("gui/sprites/field.png").scaled(500, 500)
        width, height = self.game.game_settings.field_properties.width, self.game.game_settings.field_properties.height
        scale_w = 20 / width
        scale_h = 20 / height
        scale = min(scale_h, scale_w)
        self.cell_size = 500 // max(width, height)

        pixmap = pixmap.scaled(int(pixmap.width() * scale), int(pixmap.height() * scale))

        self.ui.field_label.setPixmap(pixmap)
        if width < height:
            self.ui.field_label.setFixedWidth(500 * (width / height))
        elif width > height:
            self.ui.field_label.setFixedHeight(500 * (height / width))

        window_center = QtCore.QPoint(self.main_window.width() // 2, self.main_window.height() // 2)
        w_h = QtCore.QPoint(self.ui.field_label.width() // 2, self.ui.field_label.height() // 2)
        self.ui.field_label.move(window_center - w_h)

    def _on_accept_button_click(self):
        try:
            self.game.accept_ship_placement()
        except Warning as e:
            WW.show_warning(e)
        else:
            if self.game.game_state == GameState.ShipPlacing:
                new_ui = ShipPlacingUI.setup_ui(self.main_window, self.on_ui_change, self.game)
                new_ui.ui.turn_label.setText("игрок 2")
            else:
                print(self.game.fields[0])
                print()
                print(self.game.fields[1])
                from gui.menu_ui import MenuUI
                MenuUI.setup_ui(self.main_window, self.on_ui_change)

    def clear(self):
        for x in self.ships_widgets:
            x.deleteLater()
        del self.ships_widgets

    def __del__(self):
        print("deleted", self)
