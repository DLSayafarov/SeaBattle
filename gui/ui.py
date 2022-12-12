from abc import ABC
from typing import Callable
from PyQt5 import QtWidgets


class UI(ABC):
    @staticmethod
    def setup_ui(MainWindow: QtWidgets.QMainWindow, on_ui_change: Callable):
        pass

    def clear(self):
        pass