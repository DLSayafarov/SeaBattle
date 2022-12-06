from menu_ui import *

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    ui.game_field_width
    ui.game_field_height
    ui.ships_len
    ui.mines_count
    ui.minesweepers_count
    ui.second_player_hotseat_rb
    ui.second_player_bot_rb
    ui.bot_game_difficult_easy_rb
    ui.bot_game_difficult_hard_rb
    ui.game_start_button

    MainWindow.show()
    sys.exit(app.exec_())
