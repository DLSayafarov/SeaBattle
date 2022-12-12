from PyQt5 import QtWidgets


def show_warning(e: Exception):
    errorMessage = QtWidgets.QErrorMessage()
    errorMessage.showMessage(str(e))
    errorMessage.exec()
