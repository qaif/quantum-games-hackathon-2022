import math
from enum import Enum

from PyQt6.QtGui import QPainter, QColor, QBrush
from PyQt6.QtWidgets import QWidget
from PyQt6.QtCore import QRect, Qt
from utility import shrink


class Grid:
    def __init__(self, size, node_size):
        self.on_updated_listeners = []
        self.size = size
        self.node_size = node_size
        # self.width = (size + 1) * node_size
        self.width = size * node_size
        self.height = (size + 1) * node_size
        # self.height = (size) * node_size
        self.nodes = [GridNode(i, self) for i in range(size * size)]
        self.hovered_node = None
        self.pressed_node = None
        # self.released_node = None
        self.selected_node = None

    def draw(self, painter, event):
        for n in self.nodes:
            n.draw(painter, event)

    def get_coord_x(self, idx):
        return idx % self.size

    def get_coord_y(self, idx):
        return math.floor(idx / self.size)

    def get_coords(self, idx):
        return idx % self.size, math.floor(idx / self.size)

    def get_canvas_x(self, idx):
        return self.get_coord_x(idx) * self.node_size

    def get_canvas_y(self, idx):
        return self.get_coord_y(idx) * self.node_size

    def get_idx_from_coord(self, x, y):
        return y * self.size + x

    def get_coord_from_canvas(self, x, y):
        return min(self.size - 1, max(0, math.floor(x / self.node_size))), min(self.size - 1,
                                                                               max(0, math.floor(y / self.node_size)))

    def get_idx_from_canvas(self, x, y):
        coords = self.get_coord_from_canvas(x, y)
        return self.get_idx_from_coord(coords[0], coords[1])

    def get_rect(self, idx):
        x1 = self.get_canvas_x(idx)
        y1 = self.get_canvas_y(idx)
        return QRect(x1, y1, self.node_size, self.node_size)

    def up(self, idx):
        if idx < self.size: return -1
        return idx - self.size

    def left(self, idx):
        if idx % self.size == 0: return -1
        return idx - 1

    def right(self, idx):
        if idx % self.size == self.size - 1: return -1
        return idx + 1

    def down(self, idx):
        if idx >= self.size * (self.size - 1): return -1
        return idx + self.size

    def set_occupier(self, idx, type):
        self.nodes[idx].occupier = type
        self.on_updated()

    def add_on_updated_listener(self, listener):
        self.on_updated_listeners.append(listener)

    def on_updated(self):
        for listener in self.on_updated_listeners:
            listener()


class OccupierType(Enum):
    NONE = 0
    SNAKE = 1
    SNAKE_HEAD_V = 2
    SNAKE_HEAD_H = 3
    PROBE = 4
    PREY = 5


class GridNode:
    def __init__(self, idx, grid):
        self.idx = idx
        self.grid = grid

        self.hovered = False
        self.pressed = False
        # self.released = False
        self.selected = False

        self.selected_color = QColor(243, 26, 26)
        self.hovered_color = QColor(243, 236, 26)
        self.pressed_color = QColor(243, 236, 26)
        self.default_color = QColor(80, 80, 80)
        self.border_color = QColor(50, 50, 50)
        self.snake_color = QColor(243, 236, 26)
        self.eye_color = QColor(50, 50, 50)
        self.probe_color = QColor(139, 206, 210)
        self.prey_color = QColor(243, 26, 26)

        # self.outline_color = QColor(0, 0, 0)
        # self.fill_color = QColor(0, 0, 0)

        self.x = grid.get_coord_x(idx)
        self.y = grid.get_coord_y(idx)
        self.occupier = OccupierType.NONE

    def draw(self, painter, event):
        r = self.grid.get_rect(self.idx)

        fill_color = self.default_color
        if self.pressed:
            fill_color = self.pressed_color
        elif self.occupier == OccupierType.SNAKE or self.occupier == OccupierType.SNAKE_HEAD_V or self.occupier == OccupierType.SNAKE_HEAD_H:
            fill_color = self.snake_color
        elif self.occupier == OccupierType.PROBE:  # TODO: draw number associated with node
            fill_color = self.probe_color
        elif self.occupier == OccupierType.PREY:
            fill_color = self.prey_color
        painter.fillRect(r, QBrush(fill_color))

        if self.occupier == OccupierType.SNAKE_HEAD_V:
            for e in self.get_v_eye_rects():
                painter.fillRect(e, QBrush(self.eye_color))
        elif self.occupier == OccupierType.SNAKE_HEAD_H:
            for e in self.get_h_eye_rects():
                painter.fillRect(e, QBrush(self.eye_color))

        outline_color = self.border_color
        if self.selected:
            outline_color = self.selected_color
        elif self.hovered:
            outline_color = self.hovered_color
        painter.setPen(outline_color)
        painter.drawRect(shrink(r, 1))

    def on_hovered_enter(self):
        self.hovered = True

    def on_hovered_exit(self):
        self.hovered = False

    def on_select(self):
        self.selected = True

    def on_deselect(self):
        self.selected = False
        self.pressed = False

    def get_v_eye_rects(self):
        s = self.grid.node_size
        width = s / 5
        height = s / 4
        x1 = self.grid.get_canvas_x(self.idx)
        y1 = self.grid.get_canvas_y(self.idx) + (s - height) / 2
        x2 = x1 + s - width
        y2 = y1
        return QRect(x1, y1, width, height), QRect(x2, y2, width, height)

    def get_h_eye_rects(self):
        s = self.grid.node_size
        width = s / 4
        height = s / 5
        x1 = self.grid.get_canvas_x(self.idx) + (s - width) / 2
        y1 = self.grid.get_canvas_y(self.idx)
        x2 = x1
        y2 = y1 + s - height
        return QRect(x1, y1, width, height), QRect(x2, y2, width, height)


class GridWidget(QWidget):
    def __init__(self, grid):
        super().__init__()

        self.setMouseTracking(True)
        self.setMinimumWidth(grid.width)

        self.grid = grid
        # self.setGeometry(grid.node_size / 2, grid.node_size / 2, grid.width, grid.height)
        # self.setWindowTitle('Quantum Snake')
        # self.show()

        self.grid.add_on_updated_listener(self.on_update)

    def on_update(self):
        self.update()

    def mouseMoveEvent(self, event):
        if self.grid.hovered_node is not None: self.grid.hovered_node.on_hovered_exit()

        new = self.grid.nodes[self.grid.get_idx_from_canvas(event.position().x(), event.position().y())]
        # print('new hovered idx: ', new.idx)
        # if new == self.grid.hovered_node: return

        self.grid.hovered_node = new
        self.grid.hovered_node.on_hovered_enter()

        # self.update()
        self.on_update()
        # self.label.setText('Mouse coords: ( %d : %d )' % (event.x(), event.y()))

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.grid.pressed_node = self.grid.nodes[
                self.grid.get_idx_from_canvas(event.position().x(), event.position().y())]
            self.grid.pressed_node.pressed = True
            print("pressed node: ", self.grid.pressed_node.idx)
            # self.update()
            self.on_update()

    def mouseReleaseEvent(self, event):
        # ensure that the left button was pressed *and* released within the
        # geometry of the widget; if so, emit the signal;
        if (self.grid.pressed_node is not None and
                event.button() == Qt.MouseButton.LeftButton
                # and event.position() in self.rect()):
                and self.grid.pressed_node == self.grid.nodes[
                    self.grid.get_idx_from_canvas(event.position().x(), event.position().y())]
        ):
            print("clicked node: ", self.grid.pressed_node.idx)
            self.update()
            if self.grid.selected_node is not None: self.grid.selected_node.on_deselect()
            self.grid.selected_node = self.grid.pressed_node
            self.grid.selected_node.on_select()
        self.grid.pressed_node.pressed = False
        self.grid.pressed_node = None

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)

        self.grid.draw(painter, event)

        painter.end()

    # def on_click(self, pressed_node):
    #     # TODO
    #     pass
