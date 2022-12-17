from PyQt5 import QtWidgets

from gui.menu_ui import MenuUI
from gui.ui import UI

CURRENT_UI: UI = None


def on_ui_changed(new_ui: UI):
    global CURRENT_UI
    if CURRENT_UI is not None:
        CURRENT_UI.clear()
    CURRENT_UI = new_ui


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    MainWindow.setFixedSize(1500, 800)
    MenuUI.setup_ui(MainWindow, on_ui_changed)
    MainWindow.show()
    sys.exit(app.exec_())
