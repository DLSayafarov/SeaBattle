from typing import Callable
from PyQt5 import QtWidgets, QtCore
import gui.ui_base.ship_placing_ui as ship_placing_ui
from gui.drag_widgets.one_cell_object_drag_widget import OneCellObjectWidget
from gui.drag_widgets.ship_drag_widget import ShipWidget
from game.game import Game, GameState
import gui.dialog_window as DW
from gui.ui import UI
from gui.field_drawer import FieldDrawer


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

    def _on_one_cell_object_taking(self, ocb_widget: OneCellObjectWidget):
        self.game.try_remove_one_cell_object(ocb_widget.cell)

    def _on_one_cell_object_realise(self, ocb_widget: OneCellObjectWidget):
        x, y = self._get_pos_in_field(ocb_widget.pos())
        if self.game.try_place_one_cell_object(ocb_widget.cell, x, y):
            pos_in_field = QtCore.QPoint(x * self.cell_size, y * self.cell_size)
            new_pos = self.ui.field_label.pos() + pos_in_field
            ocb_widget.move(new_pos)
        else:
            self.ui.other_objects_area_layout.layout().addWidget(ocb_widget)

    def _get_pos_in_field(self, ship_widget_pos: QtCore.QPoint):
        temp_pos = ship_widget_pos - self.ui.field_label.pos()
        x, y = temp_pos.x() / self.cell_size, temp_pos.y() / self.cell_size
        return round(x), round(y)

    def _on_auto_ship_place_button_click(self):
        try:
            self.game.place_ship_automatically()
        except Warning as e:
            DW.show_warning_window(e)
        else:
            for ship_widget in self.ships_widgets:
                in_field_pos = QtCore.QPoint(ship_widget.ship.pos.x * self.cell_size,
                                             ship_widget.ship.pos.y * self.cell_size)
                ship_widget.setParent(ship_widget.base_parent_widget)
                ship_widget.set_pixmap()
                ship_widget.move(self.ui.field_label.pos() + in_field_pos)

    def _on_auto_ocb_place_button_click(self):
        try:
            self.game.place_one_cell_objects_automatically()
        except Warning as e:
            DW.show_warning_window(e)
        else:
            for ocb_widget in self.one_cell_objects_widgets:
                in_field_pos = QtCore.QPoint(ocb_widget.cell.pos.x * self.cell_size,
                                             ocb_widget.cell.pos.y * self.cell_size)
                ocb_widget.setParent(ocb_widget.base_parent_widget)
                ocb_widget.set_pixmap()
                ocb_widget.move(self.ui.field_label.pos() + in_field_pos)

    def _on_reset_button_click(self):
        for ship_widget in self.ships_widgets:
            if self.game.try_remove_ship(ship_widget.ship):
                self.ui.ship_area_layout.layout().addWidget(ship_widget)

        for ocb_widget in self.one_cell_objects_widgets:
            if self.game.try_remove_one_cell_object(ocb_widget.cell):
                self.ui.other_objects_area_layout.layout().addWidget(ocb_widget)

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
        self.ui.auto_ocb_place_button.clicked.connect(self._on_auto_ocb_place_button_click)
        self.ui.reset_button.clicked.connect(self._on_reset_button_click)
        self.ships_widgets = [ShipWidget(x, self.cell_size, self._on_ship_taking,
                                         self._on_ship_realise, self.main_window)
                              for x in self.game.fields[self.game.turn].ships_to_place]
        for x in self.ships_widgets:
            self.ui.ship_area_layout.layout().addWidget(x)

        self.one_cell_objects_widgets = [OneCellObjectWidget(x, self.cell_size,
                                                             self._on_one_cell_object_taking,
                                                             self._on_one_cell_object_realise, self.main_window)
                                         for x in self.game.fields[self.game.turn].one_cell_objects_to_place]
        for x in self.one_cell_objects_widgets:
            self.ui.other_objects_area_layout.layout().addWidget(x)

    def _draw_field(self):
        width, height = self.game.game_settings.field_properties.width, self.game.game_settings.field_properties.height
        FieldDrawer.draw_field(self.ui.field_label, width, height)
        self.cell_size = 500 // max(width, height)

    def _on_accept_button_click(self):
        try:
            self.game.accept_ship_placement()
        except Warning as e:
            DW.show_warning_window(e)
        else:
            if self.game.game_state == GameState.ShipPlacing:
                new_ui = ShipPlacingUI.setup_ui(self.main_window, self.on_ui_change, self.game)
                new_ui.ui.turn_label.setText("игрок 2")
            else:
                from gui.game_ui import GameUI
                GameUI.setup_ui(self.main_window, self.on_ui_change, self.game)

    def clear(self):
        for x in self.ships_widgets:
            x.deleteLater()
        for x in self.one_cell_objects_widgets:
            x.deleteLater()
        self.ships_widgets = None
        self.ui = None
