# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '1.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def __init__(self):
        self.centralwidget = None
        self.first_field_label = None
        self.label_3 = None
        self.label_2 = None
        self.turn_label = None
        self.back_button = None
        self.second_field_label = None
        self.label_4 = None
        self.label = None
        self.state_label = None
        self.confirm_window = None
        self.turn_label_4 = None
        self.turn_label_5 = None
        self.accept_turn = None
        self.turn_acception_label = None

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1500, 800)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.first_field_label = QtWidgets.QLabel(self.centralwidget)
        self.first_field_label.setGeometry(QtCore.QRect(180, 150, 500, 500))
        self.first_field_label.setObjectName("first_field")
        self.first_field_label.setAlignment(QtCore.Qt.AlignTop)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(460, 110, 221, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPixelSize(1.333 * 16)
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_3.setFont(font)
        self.label_3.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_3.setTextFormat(QtCore.Qt.RichText)
        self.label_3.setScaledContents(True)
        self.label_3.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 40, 651, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPixelSize(1.333 * 20)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_2.setFont(font)
        self.label_2.setTextFormat(QtCore.Qt.RichText)
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.turn_label = QtWidgets.QLabel(self.centralwidget)
        self.turn_label.setGeometry(QtCore.QRect(340 - 300, 660, 191 + 600, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.turn_label.sizePolicy().hasHeightForWidth())
        self.turn_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPixelSize(1.333 * 16)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.turn_label.setFont(font)
        self.turn_label.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.turn_label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.turn_label.setTextFormat(QtCore.Qt.PlainText)
        self.turn_label.setScaledContents(True)
        self.turn_label.setAlignment(QtCore.Qt.AlignCenter)
        self.turn_label.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.turn_label.setObjectName("turn_label")
        self.back_button = QtWidgets.QPushButton(self.centralwidget)
        self.back_button.setGeometry(QtCore.QRect(700, 720, 91, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.back_button.sizePolicy().hasHeightForWidth())
        self.back_button.setSizePolicy(sizePolicy)
        self.back_button.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        self.back_button.setFont(font)
        self.back_button.setObjectName("back_button")
        self.second_field_label = QtWidgets.QLabel(self.centralwidget)
        self.second_field_label.setGeometry(QtCore.QRect(810, 150, 500, 500))
        self.second_field_label.setObjectName("second_field")
        self.second_field_label.setAlignment(QtCore.Qt.AlignTop)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(810, 110, 251, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPixelSize(1.333 * 16)
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_4.setFont(font)
        self.label_4.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_4.setTextFormat(QtCore.Qt.RichText)
        self.label_4.setScaledContents(True)
        self.label_4.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.label_4.setObjectName("label_4")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(700, 360, 91, 81))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("gui/sprites/cannon.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.state_label = QtWidgets.QLabel(self.centralwidget)
        self.state_label.setGeometry(QtCore.QRect(810, 660, 501, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.state_label.sizePolicy().hasHeightForWidth())
        self.state_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPixelSize(1.333 * 16)
        font.setBold(False)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.state_label.setFont(font)
        self.state_label.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.state_label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.state_label.setText("")
        self.state_label.setTextFormat(QtCore.Qt.PlainText)
        self.state_label.setScaledContents(True)
        self.state_label.setAlignment(QtCore.Qt.AlignCenter)
        self.state_label.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.state_label.setObjectName("turn_label_2")
        self.confirm_window = QtWidgets.QWidget(self.centralwidget)
        self.confirm_window.setEnabled(True)
        self.confirm_window.setGeometry(QtCore.QRect(170, 140, 1151, 521))
        self.confirm_window.setAutoFillBackground(False)
        self.confirm_window.setStyleSheet(".QWidget\n"
"{\n"
"background-color: #607d8b;\n"
"border-radius: 10%;\n"
"}")
        self.confirm_window.setObjectName("confirm_window")
        self.turn_label_4 = QtWidgets.QLabel(self.confirm_window)
        self.turn_label_4.setGeometry(QtCore.QRect(0, 130, 1151, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.turn_label_4.sizePolicy().hasHeightForWidth())
        self.turn_label_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPixelSize(1.333 * 16)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.turn_label_4.setFont(font)
        self.turn_label_4.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.turn_label_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.turn_label_4.setTextFormat(QtCore.Qt.PlainText)
        self.turn_label_4.setScaledContents(True)
        self.turn_label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.turn_label_4.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.turn_label_4.setObjectName("turn_label_4")
        self.turn_label_5 = QtWidgets.QLabel(self.confirm_window)
        self.turn_label_5.setGeometry(QtCore.QRect(0, 320, 1151, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.turn_label_5.sizePolicy().hasHeightForWidth())
        self.turn_label_5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPixelSize(1.333 * 16)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.turn_label_5.setFont(font)
        self.turn_label_5.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.turn_label_5.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.turn_label_5.setTextFormat(QtCore.Qt.PlainText)
        self.turn_label_5.setScaledContents(True)
        self.turn_label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.turn_label_5.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.turn_label_5.setObjectName("turn_label_5")
        self.accept_turn = QtWidgets.QPushButton(self.confirm_window)
        self.accept_turn.setGeometry(QtCore.QRect(490, 370, 161, 71))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.accept_turn.sizePolicy().hasHeightForWidth())
        self.accept_turn.setSizePolicy(sizePolicy)
        self.accept_turn.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPixelSize(1.333 * 20)
        self.accept_turn.setFont(font)
        self.accept_turn.setAutoFillBackground(False)
        self.accept_turn.setStyleSheet("")
        self.accept_turn.setObjectName("accept_turn")
        self.turn_acception_label = QtWidgets.QLabel(self.confirm_window)
        self.turn_acception_label.setGeometry(QtCore.QRect(0, 170, 1151, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.turn_acception_label.sizePolicy().hasHeightForWidth())
        self.turn_acception_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPixelSize(1.333 * 16)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.turn_acception_label.setFont(font)
        self.turn_acception_label.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.turn_acception_label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.turn_acception_label.setTextFormat(QtCore.Qt.PlainText)
        self.turn_acception_label.setScaledContents(True)
        self.turn_acception_label.setAlignment(QtCore.Qt.AlignCenter)
        self.turn_acception_label.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.turn_acception_label.setObjectName("turn_acception_label")
        self.confirm_window.hide()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p>ваше прекрасное поле</p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p>достаточно морской и достаточно бой...</p></body></html>"))
        self.turn_label.setText(_translate("MainWindow", "ход игрока 1"))
        self.back_button.setText(_translate("MainWindow", "< Меню"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p>загнивающее поле врага</p></body></html>"))
        self.turn_label_4.setText(_translate("MainWindow", "Ваш ход,"))
        self.turn_label_5.setText(_translate("MainWindow", "Вы готовы?"))
        self.accept_turn.setText(_translate("MainWindow", "Естесна!"))
        self.turn_acception_label.setText(_translate("MainWindow", "Игрок 2"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
