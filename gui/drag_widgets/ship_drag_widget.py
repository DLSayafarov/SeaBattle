from PyQt5 import QtWidgets, QtGui, QtCore
from typing import Callable
from game_objects.ship import Ship
from game_objects.rotation import Rotation
from gui.ui_base import images_source


class ShipWidget(QtWidgets.QLabel):
    def __init__(self, ship: Ship, cell_size: int, on_widget_taking: Callable[[QtWidgets.QWidget], None],
                 on_widget_realise: Callable[[QtWidgets.QWidget], None], *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.mouse_click_offset = None
        self.scale = cell_size / 80
        self.ship = ship
        self.base_parent_widget = self.parentWidget()
        self.on_widget_taking = on_widget_taking
        self.on_widget_realise = on_widget_realise
        self.set_pixmap()

    def set_pixmap(self):
        pixmap = QtGui.QPixmap(images_source.get_ship_image_path(self.ship))
        size = [pixmap.width() * self.scale, pixmap.height() * self.scale]
        self.setFixedSize(*size)
        self.setPixmap(pixmap.scaled(*size, QtCore.Qt.IgnoreAspectRatio))
        self.show()

    def mousePressEvent(self, event: QtGui.QMouseEvent):
        global_pos = self.mapToGlobal(QtCore.QPoint(0, 0))
        self.setParent(self.base_parent_widget)

        main_window_global_pos = self.base_parent_widget.mapToGlobal(QtCore.QPoint(0, 0))
        self.mouse_click_offset = event.globalPos() - global_pos
        self.move(global_pos - main_window_global_pos)
        self.on_widget_taking(self)
        self.show()
        self.grabMouse()
        self.grabKeyboard()

    def mouseReleaseEvent(self, ev: QtGui.QMouseEvent):
        self.on_widget_realise(self)
        self.releaseMouse()
        self.releaseKeyboard()

    def mouseMoveEvent(self, event: QtGui.QMouseEvent):
        new_pos = event.windowPos() - self.mouse_click_offset
        self.move(new_pos.toPoint())

    def keyPressEvent(self, ev: QtGui.QKeyEvent):
        if ev.key() == QtCore.Qt.Key.Key_R:
            self.ship.rotation = Rotation((self.ship.rotation + 1) % 2)
            self.set_pixmap()



