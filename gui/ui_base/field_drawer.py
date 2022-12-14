from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import QPoint
from PyQt5.QtWidgets import QLabel

from game_objects.field import Field
from gui.ui_base import images_source


class FieldDrawer:
    @staticmethod
    def draw_field(label: QLabel, width: int, height: int):
        pixmap = QtGui.QPixmap("gui/sprites/field.png").scaled(500, 500)

        scale_w = 20 / width
        scale_h = 20 / height
        scale = min(scale_h, scale_w)
        cell_size = 500 // max(width, height)

        pixmap = pixmap.scaled(int(pixmap.width() * scale), int(pixmap.height() * scale))

        label.setPixmap(pixmap)

        if width != height and label.width() == label.height():
            to_center = QPoint(label.width() / 2, label.height() / 2)
            to_center_in_new = QPoint(cell_size * width / 2, cell_size * height / 2)
            label.move(label.pos() + to_center - to_center_in_new)

            if width < height:
                label.setFixedWidth(500 * (width / height))
            elif width > height:
                label.setFixedHeight(500 * (height / width))

        return label

    @staticmethod
    def draw_objects(label: QLabel, field: Field, only_marked=False):
        cell_size = 500 // max(field.width, field.height)
        scale = cell_size / 80
        labels = []

        for ship in field.ships:
            if only_marked and ship.is_alive:
                continue
            ship_label = QLabel(label)
            pixmap = QtGui.QPixmap(images_source.get_ship_image_path(ship))
            size = [pixmap.width() * scale, pixmap.height() * scale]
            ship_label.setFixedSize(*size)
            ship_label.setPixmap(pixmap.scaled(*size, QtCore.Qt.IgnoreAspectRatio))
            x, y = cell_size * ship.pos.x, cell_size * ship.pos.y
            ship_label.move(x, y)
            ship_label.show()
            labels.append(ship_label)

        return labels

    @staticmethod
    def draw_particles(label: QLabel, field: Field):
        cell_size = 500 // max(field.width, field.height)
        scale = cell_size / 80
        labels = []

        for y in range(field.height):
            for x in range(field.width):
                pixmap = QtGui.QPixmap(images_source.get_particle_by_cell(field.field[y][x]))
                if images_source.get_particle_by_cell(field.field[y][x]) is None:
                    continue

                particle_label = QLabel(label)
                size = [pixmap.width() * scale, pixmap.height() * scale]
                particle_label.setFixedSize(*size)
                particle_label.setPixmap(pixmap.scaled(*size, QtCore.Qt.IgnoreAspectRatio))
                particle_label.move(cell_size * x, cell_size * y)
                particle_label.show()
                labels.append(particle_label)

        return labels

