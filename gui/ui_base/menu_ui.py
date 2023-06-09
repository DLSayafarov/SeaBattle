from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def __init__(self):
        self.centralwidget = None
        self.game_start_button = None
        self.widget_5 = None
        self.widget_6 = None
        self.label_8 = None
        self.second_player_hotseat_rb = None
        self.second_player_bot_rb = None
        self.bot_settings = None
        self.label_11 = None
        self.widget_3 = None
        self.bot_ship_placing_difficult_hard_rb = None
        self.bot_ship_placing_difficult_easy_rb = None
        self.label_10 = None
        self.widget_2 = None
        self.bot_game_difficult_hard_rb = None
        self.bot_game_difficult_easy_rb = None
        self.label_9 = None
        self.widget_11 = None
        self.label_6 = None
        self.mines_count = None
        self.label_4 = None
        self.ships_lens = None
        self.label_5 = None
        self.game_field_height = None
        self.game_field_width = None
        self.label_3 = None
        self.label_7 = None
        self.minesweepers_count = None
        self.label_2 = None
        self.label = None

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
        self.game_start_button = QtWidgets.QPushButton(self.centralwidget)
        self.game_start_button.setGeometry(QtCore.QRect(650, 650, 200, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.game_start_button.sizePolicy().hasHeightForWidth())
        self.game_start_button.setSizePolicy(sizePolicy)
        self.game_start_button.setMinimumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPixelSize(1.333 * 15)
        font.setBold(False)
        font.setWeight(50)
        self.game_start_button.setFont(font)
        self.game_start_button.setObjectName("game_start_button")
        self.widget_5 = QtWidgets.QWidget(self.centralwidget)
        self.widget_5.setGeometry(QtCore.QRect(780, 300, 421, 271))
        self.widget_5.setObjectName("widget_5")
        self.widget_6 = QtWidgets.QWidget(self.widget_5)
        self.widget_6.setGeometry(QtCore.QRect(0, 0, 261, 121))
        self.widget_6.setObjectName("widget_6")
        self.label_8 = QtWidgets.QLabel(self.widget_6)
        self.label_8.setGeometry(QtCore.QRect(10, 0, 141, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPixelSize(1.333 * 16)
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_8.setFont(font)
        self.label_8.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_8.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_8.setTextFormat(QtCore.Qt.RichText)
        self.label_8.setScaledContents(True)
        self.label_8.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.label_8.setObjectName("label_8")
        self.second_player_hotseat_rb = QtWidgets.QRadioButton(self.widget_6)
        self.second_player_hotseat_rb.setGeometry(QtCore.QRect(20, 50, 271, 31))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPixelSize(1.333 * 13)
        self.second_player_hotseat_rb.setFont(font)
        self.second_player_hotseat_rb.setChecked(True)
        self.second_player_hotseat_rb.setObjectName("second_player_hotseat_rb")
        self.second_player_bot_rb = QtWidgets.QRadioButton(self.widget_6)
        self.second_player_bot_rb.setGeometry(QtCore.QRect(20, 80, 271, 31))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPixelSize(1.333 * 13)
        self.second_player_bot_rb.setFont(font)
        self.second_player_bot_rb.setChecked(False)
        self.second_player_bot_rb.setObjectName("second_player_bot_rb")
        self.bot_settings = QtWidgets.QWidget(self.widget_5)
        self.bot_settings.hide()
        self.bot_settings.setGeometry(QtCore.QRect(0, 120, 411, 161))
        self.bot_settings.setObjectName("widget_4")
        self.label_11 = QtWidgets.QLabel(self.bot_settings)
        self.label_11.setGeometry(QtCore.QRect(10, 10, 261, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPixelSize(1.333 * 16)
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_11.setFont(font)
        self.label_11.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_11.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_11.setTextFormat(QtCore.Qt.RichText)
        self.label_11.setScaledContents(True)
        self.label_11.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.label_11.setObjectName("label_11")
        self.widget_3 = QtWidgets.QWidget(self.bot_settings)
        self.widget_3.setGeometry(QtCore.QRect(170, 40, 211, 111))
        self.widget_3.setObjectName("widget_3")
        self.bot_ship_placing_difficult_hard_rb = QtWidgets.QRadioButton(self.widget_3)
        self.bot_ship_placing_difficult_hard_rb.setGeometry(QtCore.QRect(10, 80, 91, 30))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPixelSize(1.333 * 13)
        self.bot_ship_placing_difficult_hard_rb.setFont(font)
        self.bot_ship_placing_difficult_hard_rb.setChecked(False)
        self.bot_ship_placing_difficult_hard_rb.setObjectName("bot_ship_placing_difficult_hard_rb")
        self.bot_ship_placing_difficult_easy_rb = QtWidgets.QRadioButton(self.widget_3)
        self.bot_ship_placing_difficult_easy_rb.setGeometry(QtCore.QRect(10, 50, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPixelSize(1.333 * 13)
        self.bot_ship_placing_difficult_easy_rb.setFont(font)
        self.bot_ship_placing_difficult_easy_rb.setChecked(True)
        self.bot_ship_placing_difficult_easy_rb.setObjectName("bot_ship_placing_difficult_easy_rb")
        self.label_10 = QtWidgets.QLabel(self.widget_3)
        self.label_10.setGeometry(QtCore.QRect(10, 10, 201, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPixelSize(1.333 * 14)
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_10.setFont(font)
        self.label_10.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_10.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_10.setTextFormat(QtCore.Qt.RichText)
        self.label_10.setScaledContents(True)
        self.label_10.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.label_10.setObjectName("label_10")
        self.widget_2 = QtWidgets.QWidget(self.bot_settings)
        self.widget_2.setGeometry(QtCore.QRect(0, 40, 161, 111))
        self.widget_2.setObjectName("widget_2")
        self.bot_game_difficult_hard_rb = QtWidgets.QRadioButton(self.widget_2)
        self.bot_game_difficult_hard_rb.setGeometry(QtCore.QRect(20, 80, 91, 30))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPixelSize(1.333 * 13)
        self.bot_game_difficult_hard_rb.setFont(font)
        self.bot_game_difficult_hard_rb.setChecked(False)
        self.bot_game_difficult_hard_rb.setObjectName("bot_game_difficult_hard_rb")
        self.bot_game_difficult_easy_rb = QtWidgets.QRadioButton(self.widget_2)
        self.bot_game_difficult_easy_rb.setGeometry(QtCore.QRect(20, 50, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPixelSize(1.333 * 13)
        self.bot_game_difficult_easy_rb.setFont(font)
        self.bot_game_difficult_easy_rb.setChecked(True)
        self.bot_game_difficult_easy_rb.setObjectName("bot_game_difficult_easy_rb")
        self.label_9 = QtWidgets.QLabel(self.widget_2)
        self.label_9.setGeometry(QtCore.QRect(20, 10, 131, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPixelSize(1.333 * 14)
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_9.setFont(font)
        self.label_9.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_9.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_9.setTextFormat(QtCore.Qt.RichText)
        self.label_9.setScaledContents(True)
        self.label_9.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.label_9.setObjectName("label_9")
        self.widget_11 = QtWidgets.QWidget(self.centralwidget)
        self.widget_11.setGeometry(QtCore.QRect(380, 300, 401, 271))
        self.widget_11.setObjectName("widget_11")
        self.label_6 = QtWidgets.QLabel(self.widget_11)
        self.label_6.setGeometry(QtCore.QRect(10, 170, 51, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPixelSize(1.333 * 16)
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_6.setFont(font)
        self.label_6.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_6.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_6.setTextFormat(QtCore.Qt.RichText)
        self.label_6.setScaledContents(True)
        self.label_6.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.label_6.setObjectName("label_6")
        self.mines_count = QtWidgets.QLineEdit(self.widget_11)
        self.mines_count.setGeometry(QtCore.QRect(70, 180, 40, 30))
        font = QtGui.QFont()
        font.setPixelSize(1.333 * 10)
        font.setStrikeOut(False)
        self.mines_count.setFont(font)
        self.mines_count.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.mines_count.setMaxLength(2)
        self.mines_count.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.mines_count.setAlignment(QtCore.Qt.AlignCenter)
        self.mines_count.setPlaceholderText("")
        self.mines_count.setObjectName("mines_count")
        self.label_4 = QtWidgets.QLabel(self.widget_11)
        self.label_4.setGeometry(QtCore.QRect(210, 0, 16, 41))
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
        self.ships_lens = QtWidgets.QLineEdit(self.widget_11)
        self.ships_lens.setGeometry(QtCore.QRect(10, 110, 341, 31))
        font = QtGui.QFont()
        font.setPixelSize(1.333 * 10)
        self.ships_lens.setFont(font)
        self.ships_lens.setMaxLength(42)
        self.ships_lens.setObjectName("ships_len")
        self.label_5 = QtWidgets.QLabel(self.widget_11)
        self.label_5.setGeometry(QtCore.QRect(10, 60, 211, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPixelSize(1.333 * 16)
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_5.setFont(font)
        self.label_5.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_5.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_5.setTextFormat(QtCore.Qt.RichText)
        self.label_5.setScaledContents(True)
        self.label_5.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.label_5.setObjectName("label_5")
        self.game_field_height = QtWidgets.QLineEdit(self.widget_11)
        self.game_field_height.setGeometry(QtCore.QRect(230, 10, 40, 30))
        font = QtGui.QFont()
        font.setPixelSize(1.333 * 10)
        font.setStrikeOut(False)
        self.game_field_height.setFont(font)
        self.game_field_height.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.game_field_height.setMaxLength(2)
        self.game_field_height.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.game_field_height.setAlignment(QtCore.Qt.AlignCenter)
        self.game_field_height.setPlaceholderText("")
        self.game_field_height.setObjectName("game_field_height")
        self.game_field_width = QtWidgets.QLineEdit(self.widget_11)
        self.game_field_width.setGeometry(QtCore.QRect(160, 10, 40, 30))
        font = QtGui.QFont()
        font.setPixelSize(1.333 * 10)
        font.setStrikeOut(False)
        self.game_field_width.setFont(font)
        self.game_field_width.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.game_field_width.setMaxLength(2)
        self.game_field_width.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.game_field_width.setAlignment(QtCore.Qt.AlignCenter)
        self.game_field_width.setPlaceholderText("")
        self.game_field_width.setObjectName("game_field_width")
        self.label_3 = QtWidgets.QLabel(self.widget_11)
        self.label_3.setGeometry(QtCore.QRect(10, 0, 141, 41))
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
        self.label_7 = QtWidgets.QLabel(self.widget_11)
        self.label_7.setGeometry(QtCore.QRect(10, 220, 221, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPixelSize(1.333 * 16)
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_7.setFont(font)
        self.label_7.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_7.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_7.setTextFormat(QtCore.Qt.RichText)
        self.label_7.setScaledContents(True)
        self.label_7.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.label_7.setObjectName("label_7")
        self.minesweepers_count = QtWidgets.QLineEdit(self.widget_11)
        self.minesweepers_count.setGeometry(QtCore.QRect(230, 230, 40, 30))
        font = QtGui.QFont()
        font.setPixelSize(1.333 * 10)
        font.setStrikeOut(False)
        self.minesweepers_count.setFont(font)
        self.minesweepers_count.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.minesweepers_count.setMaxLength(2)
        self.minesweepers_count.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.minesweepers_count.setAlignment(QtCore.Qt.AlignCenter)
        self.minesweepers_count.setPlaceholderText("")
        self.minesweepers_count.setObjectName("minesweepers_count")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(630, 220, 251, 41))
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
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(530, 60, 445, 104))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPixelSize(1.333 * 30)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.game_start_button.setText(_translate("MainWindow", "Начать игру"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p>Второй игрок:</p></body></html>"))
        self.second_player_hotseat_rb.setText(_translate("MainWindow", "другой человек (hot seat)"))
        self.second_player_bot_rb.setText(_translate("MainWindow", "бот"))
        self.label_11.setText(_translate("MainWindow", "<html><head/><body><p>Уровень сложности бота:</p></body></html>"))
        self.bot_ship_placing_difficult_hard_rb.setText(_translate("MainWindow", "200 iq"))
        self.bot_ship_placing_difficult_easy_rb.setText(_translate("MainWindow", "рандом"))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p>расстановка кораблей</p></body></html>"))
        self.bot_game_difficult_hard_rb.setText(_translate("MainWindow", "200 iq"))
        self.bot_game_difficult_easy_rb.setText(_translate("MainWindow", "рандом"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p>уровень игры</p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p>мин:</p></body></html>"))
        self.mines_count.setText(_translate("MainWindow", "3"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p>x</p></body></html>"))
        self.ships_lens.setText(_translate("MainWindow", "4 3 3 2 2 2 1 1 1 1"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p>корабли (их длины):</p></body></html>"))
        self.game_field_height.setText(_translate("MainWindow", "10"))
        self.game_field_width.setText(_translate("MainWindow", "10"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p>размер поля:</p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p>минных тральщиков:</p></body></html>"))
        self.minesweepers_count.setText(_translate("MainWindow", "1"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p>Настройки игры</p></body></html>"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Достаточно морской</p><p align=\"center\">Достаточно бой</p></body></html>"))


