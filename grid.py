import math
from enum import Enum

from PyQt6.QtGui import QPainter, QColor, QBrush
from PyQt6.QtWidgets import QWidget
from PyQt6.QtCore import QRect, Qt
from utility import shrink

class Grid:
    def __init__(self, size, node_size):
        self.size = size
        self.node_size = node_size
        self.width = (size + 1) * node_size
        self.height = (size + 1) * node_size
        self.nodes = [GridNode(i, self) for i in range(size * size)]
        self.hovered_node = None
        self.pressed_node = None
        # self.released_node = None

    def draw(self, painter, event):
        for n in self.nodes:
            n.draw(painter, event)

    def get_coord_x(self, idx):
        return idx % self.size

    def get_coord_y(self, idx):
        return math.floor(idx / self.size)

    def get_canvas_x(self, idx):
        return self.get_coord_x(idx) * self.node_size

    def get_canvas_y(self, idx):
        return self.get_coord_y(idx) * self.node_size

    def get_idx_from_coord(self, x, y):
        return y * self.size + x

    def get_coord_from_canvas(self, x, y):
        return min(self.size - 1, max(0, math.floor(x / self.node_size))), min(self.size - 1, max(0, math.floor(y / self.node_size)))

    def get_idx_from_canvas(self, x, y):
        coords = self.get_coord_from_canvas(x, y)
        return self.get_idx_from_coord(coords[0], coords[1])

    def get_rect(self, idx):
        x1 = self.get_canvas_x(idx)
        y1 = self.get_canvas_y(idx)
        return QRect(x1, y1, self.node_size, self.node_size)

class OccupierType(Enum):
    NONE = 0
    SNAKE = 1
    PROBE = 2
class GridNode:
    def __init__(self, idx, grid):
        self.idx = idx
        self.grid = grid

        self.hovered = False
        self.pressed = False
        # self.released = False

        self.selected_color = QColor(243, 236, 26)
        self.pressed_color = QColor(243, 236, 26)
        self.default_color = QColor(80, 80, 80)
        self.snake_color = QColor(243, 236, 26)
        self.probe_color = QColor(139, 206, 210)

        # self.outline_color = QColor(0, 0, 0)
        # self.fill_color = QColor(0, 0, 0)

        self.x = grid.get_coord_x(idx)
        self.y = grid.get_coord_y(idx)
        self.occupier = OccupierType.NONE

    def draw(self, painter, event):
        r = self.grid.get_rect(self.idx)

        fill_color = self.default_color
        if self.pressed: fill_color = self.pressed_color
        elif self.occupier == OccupierType.SNAKE: fill_color = self.snake_color
        elif self.occupier == OccupierType.PROBE: fill_color = self.probe_color
        painter.fillRect(r, QBrush(fill_color))

        outline_color = self.default_color
        if self.hovered: outline_color = self.selected_color
        painter.setPen(outline_color)
        painter.drawRect(shrink(r, 2))

    def on_hovered_enter(self):
        self.hovered = True

    def on_hovered_exit(self):
        self.hovered = False

    # def get_x(self, idx):
    #     return idx % self.size

class GridWidget(QWidget):
    def __init__(self, grid):
        super().__init__()

        self.setMouseTracking(True)

        self.grid = grid
        self.setGeometry(0, 0, grid.width, grid.height)
        # self.setWindowTitle('Quantum Snake')
        # self.show()

    def mouseMoveEvent(self, event):
        if self.grid.hovered_node is not None: self.grid.hovered_node.on_hovered_exit()

        new = self.grid.nodes[self.grid.get_idx_from_canvas(event.position().x(), event.position().y())]
        # print('new hovered idx: ', new.idx)
        # if new == self.grid.hovered_node: return

        self.grid.hovered_node = new
        self.grid.hovered_node.on_hovered_enter()

        self.update()
        # self.label.setText('Mouse coords: ( %d : %d )' % (event.x(), event.y()))

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.grid.pressed_node = self.grid.nodes[self.grid.get_idx_from_canvas(event.position().x(), event.position().y())]
            self.grid.pressed_node.pressed = True
            print("pressed node: ", self.grid.pressed_node.idx)
            self.update()

    def mouseReleaseEvent(self, event):
        # ensure that the left button was pressed *and* released within the
        # geometry of the widget; if so, emit the signal;
        if (self.grid.pressed_node is not None and
                event.button() == Qt.MouseButton.LeftButton
                # and event.position() in self.rect()):
                and self.grid.pressed_node == self.grid.nodes[self.grid.get_idx_from_canvas(event.position().x(), event.position().y())]
        ):
            print("clicked node: ", self.grid.pressed_node.idx)
            self.update()
            self.on_click(self.grid.pressed_node)
        self.grid.pressed_node.pressed = False
        self.grid.pressed_node = None

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)

        self.grid.draw(painter, event)

        painter.end()

    def on_click(self, pressed_node):
        # TODO
        pass