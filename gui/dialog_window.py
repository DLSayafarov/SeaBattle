from typing import Callable
from PyQt5.QtWidgets import QErrorMessage, QMessageBox


def show_warning_window(e: Exception):
    errorMessage = QErrorMessage()
    errorMessage.showMessage(str(e))
    errorMessage.exec()


def show_accept_window(text: str, on_accept: Callable = None, on_cancel: Callable = None):
    msgBox = QMessageBox()
    msgBox.setText(text)
    msgBox.addButton("Нет", QMessageBox.NoRole)
    msgBox.addButton("Да", QMessageBox.YesRole)
    result = msgBox.exec_()
    if result:
        if on_accept is not None:
            on_accept()
    else:
        if on_cancel is not None:
            on_cancel()
