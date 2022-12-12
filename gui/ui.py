from abc import ABC
from typing import Callable
from PyQt5 import QtWidgets
from PyQt5.QtCore import QObject


class UI(ABC):
    def __init__(self):
        self.ui = None

    @staticmethod
    def setup_ui(MainWindow: QtWidgets.QMainWindow, on_ui_change: Callable):
        pass

    def clear(self):
        pass
