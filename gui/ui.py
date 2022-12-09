from PyQt5 import QtWidgets, QtGui, QtCore
from Game.game_settings import GameSettings, FieldProperties, PlayerProperties
from GameObjects.ship import Ship
from Players.difficulty import Difficulty
import gui.menu_ui as menu_ui
import gui.ship_placing_ui as ship_placing_ui
from gui.drag_widgets.drag_widget import ShipWidget
from Game.game import Game, GameState

MENU_UI = menu_ui.Ui_MainWindow()
SHIP_PLACING_UI = ship_placing_ui.Ui_MainWindow()
MAIN_WINDOW: QtWidgets.QWidget
GAME_SETTINGS: GameSettings
CELL_SIZE = 1
GAME: Game
SHIPS_WIDGETS: list[ShipWidget]


def show_warning(e: Exception):
    errorMessage = QtWidgets.QErrorMessage()
    errorMessage.showMessage(str(e))
    errorMessage.exec()


def set_game_and_field_settings():
    try:
        game_field_width = int(MENU_UI.game_field_width.text())
        game_field_height = int(MENU_UI.game_field_height.text())
        ships_lens = [int(x) for x in MENU_UI.ships_lens.text().split()]
        MENU_UI.mines_count
        MENU_UI.minesweepers_count
    except:
        raise Warning("Некорректные настройки")

    fp = FieldProperties(game_field_width, game_field_height, ships_lens)
    pp = PlayerProperties()
    pp.is_real_player = MENU_UI.second_player_hotseat_rb.isChecked()
    if not pp.is_real_player:
        pp.bot_game_difficulty = Difficulty(0 if MENU_UI.bot_game_difficult_easy_rb.isChecked() else 1)
        pp.bot_ship_placing_difficulty = Difficulty(0 if MENU_UI.bot_ship_placing_difficult_easy_rb.isChecked() else 1)

    global GAME_SETTINGS
    GAME_SETTINGS = GameSettings(fp, pp)


def on_start_button_click():
    try:
        set_game_and_field_settings()
    except Exception as e:
        show_warning(e)
    else:
        global GAME
        GAME = Game(GAME_SETTINGS, lambda: None)
        GAME.start()
        setup_ship_placing_ui()


def on_back_button_click():
    on_ship_placing_ui_exit()
    setup_menu_Ui()


def setup_menu_Ui():
    MENU_UI._setupUi(MAIN_WINDOW)
    MENU_UI.second_player_bot_rb.clicked.connect(MENU_UI.bot_settings.show)
    MENU_UI.second_player_hotseat_rb.clicked.connect(MENU_UI.bot_settings.hide)
    MENU_UI.game_start_button.clicked.connect(on_start_button_click)


def on_ship_taking(ship_widget: ShipWidget):
    GAME.try_remove_ship(ship_widget.ship)


def get_pos_in_field(ship_widget_pos: QtCore.QPoint):
    temp_pos = ship_widget_pos - SHIP_PLACING_UI.field_label.pos()
    x, y = temp_pos.x() / CELL_SIZE, temp_pos.y() / CELL_SIZE
    return round(x), round(y)


def on_ship_realise(ship_widget: ShipWidget):
    x, y = get_pos_in_field(ship_widget.pos())
    if GAME.try_place_ship(ship_widget.ship, x, y):
        pos_in_field = QtCore.QPoint(x * CELL_SIZE, y * CELL_SIZE)
        new_pos = SHIP_PLACING_UI.field_label.pos() + pos_in_field
        ship_widget.move(new_pos)
    else:
        SHIP_PLACING_UI.ship_area_layout.layout().addWidget(ship_widget)


def on_auto_ship_place_button_click():
    try:
        GAME.place_ship_automatically()
    except Warning as e:
        show_warning(e)
    else:
        for ship_widget in SHIPS_WIDGETS:
            in_field_pos = QtCore.QPoint(ship_widget.ship.pos.x * CELL_SIZE, ship_widget.ship.pos.y * CELL_SIZE)
            ship_widget.setParent(ship_widget.base_parent_widget)
            ship_widget.set_pixmap()
            ship_widget.move(SHIP_PLACING_UI.field_label.pos() + in_field_pos)


def on_reset_button_click():
    for ship_widget in SHIPS_WIDGETS:
        if GAME.try_remove_ship(ship_widget.ship):
            SHIP_PLACING_UI.ship_area_layout.layout().addWidget(ship_widget)


def setup_ship_placing_ui():
    SHIP_PLACING_UI._setupUi(MAIN_WINDOW)
    draw_field()
    SHIP_PLACING_UI.back_button.clicked.connect(on_back_button_click)
    SHIP_PLACING_UI.accept_button.clicked.connect(on_accept_button_click)
    SHIP_PLACING_UI.auto_ship_place_button.clicked.connect(on_auto_ship_place_button_click)
    SHIP_PLACING_UI.reset_button.clicked.connect(on_reset_button_click)
    global SHIPS_WIDGETS
    SHIPS_WIDGETS = [ShipWidget(x, CELL_SIZE, on_ship_taking, on_ship_realise, MAIN_WINDOW)
             for x in GAME.fields[GAME.turn].ships_to_place]
    for x in SHIPS_WIDGETS:
        SHIP_PLACING_UI.ship_area_layout.layout().addWidget(x)


def draw_field():
    pixmap = QtGui.QPixmap("gui/sprites/field.png").scaled(500, 500)
    width, height = GAME_SETTINGS.field_properties.width, GAME_SETTINGS.field_properties.height
    scale_w = 20 / width
    scale_h = 20 / height
    scale = min(scale_h, scale_w)
    global CELL_SIZE
    CELL_SIZE = 500 // max(width, height)

    pixmap = pixmap.scaled(int(pixmap.width() * scale), int(pixmap.height() * scale))

    SHIP_PLACING_UI.field_label.setPixmap(pixmap)
    if width < height:
        SHIP_PLACING_UI.field_label.setFixedWidth(500 * (width / height))
    elif width > height:
        SHIP_PLACING_UI.field_label.setFixedHeight(500 * (height / width))

    window_center = QtCore.QPoint(MAIN_WINDOW.width() // 2, MAIN_WINDOW.height() // 2)
    w_h = QtCore.QPoint(SHIP_PLACING_UI.field_label.width() // 2, SHIP_PLACING_UI.field_label.height() // 2)
    SHIP_PLACING_UI.field_label.move(window_center - w_h)


def on_accept_button_click():
    try:
        GAME.accept_ship_placement()
    except Warning as e:
        show_warning(e)
    else:
        on_ship_placing_ui_exit()
        if GAME.game_state == GameState.ShipPlacing:
            setup_ship_placing_ui()
            SHIP_PLACING_UI.turn_label.setText("игрок 2")
        else:
            print(GAME.fields[0])
            print()
            print(GAME.fields[1])
            setup_menu_Ui()


def on_ship_placing_ui_exit():
    for x in SHIPS_WIDGETS:
        x.deleteLater()


def configurate_ui(MainWindow: QtWidgets.QMainWindow):
    global MAIN_WINDOW
    MAIN_WINDOW = MainWindow
    setup_menu_Ui()
