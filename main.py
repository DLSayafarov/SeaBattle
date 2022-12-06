from PyQt5 import QtCore, QtGui, QtWidgets
import gui.ui as ui


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui.configurate_ui(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
