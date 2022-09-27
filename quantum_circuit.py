import math

from PyQt6.QtCore import QRect, Qt, QRectF, QLine
from PyQt6.QtGui import QPainter, QBrush, QColor, QFont, QFontMetrics
from PyQt6.QtWidgets import QWidget

# TODO: label outputs and inputs
class Block:
    def __init__(self, label, num_inputs, num_outputs):
        self.x = -1
        self.y = -1
        self.label = label
        self.inputs = [None for i in range(num_inputs)] # tuple: (other_block, output_idx)
        self.outputs = [None for i in range(num_outputs)] # tuple: (other_block, input_idx)
        self.padding = 40, 20

        self.selected_color = QColor(243, 236, 26)
        self.pressed_color = QColor(243, 236, 26)
        self.default_color = QColor(80, 80, 80)
        self.text_color = QColor(250, 250, 250)
        self.socket_color = QColor(40, 40, 40)
        self.line_color = QColor(40, 40, 40)

        self.font = QFont('Decorative', 10)
        self.socket_size = 10
        self.socket_spacing = 20

        self.selected = False
        self.selected_input = -1
        self.selected_output = -1
        self.selection_offset_x = 0
        self.selection_offset_y = 0

        self.socket_drag_x = -1
        self.socket_drag_y = -1

    def on_selected(self, event):
        self.selected = True

        i = 0
        for r in self.get_input_rects_f():
            if r.contains(event.position()):
                self.selected_input = i
                # self.socket_drag_x = event.position().x()
                # self.socket_drag_y = event.position().y()
                return
            i+=1
        self.selected_input = -1

        i = 0
        for r in self.get_output_rects_f():
            if r.contains(event.position()):
                self.selected_output = i
                self.socket_drag_x = event.position().x()
                self.socket_drag_y = event.position().y()
                return
            i += 1
        self.selected_output = -1

        self.selection_offset_x = event.position().x() - self.x
        self.selection_offset_y = event.position().y() - self.y

    def on_selected_movement(self, event):
        if self.selected_input >= 0:
            print("dragging input not allowed")
            # self.socket_drag_x = event.position().x()
            # self.socket_drag_y = event.position().y()
        elif self.selected_output >= 0:
            if self.selected_output is not None:
                self.sever_output(self.selected_output)
            self.socket_drag_x = event.position().x()
            self.socket_drag_y = event.position().y()
        else:
            self.set_x(event.position().x() - self.selection_offset_x)
            self.set_y(event.position().y() - self.selection_offset_y)

    def on_deselected(self, event, blocks):
        if self.selected_input >= 0:
            if self.get_input_rects_f()[self.selected_input].contains(event.position()):
                self.sever_input(self.selected_input)
        elif self.selected_output >= 0:
            for b in blocks:
                i = 0
                for r in b.get_input_rects_f():
                    if b.is_input_clear(i):
                        if r.contains(event.position()):
                            self.outputs[self.selected_output] = (b, i)
                            b.inputs[i] = (self, self.selected_output)
                    i+=1
        self.selected = False
        self.selection_offset_x = 0
        self.selection_offset_y = 0
        self.selected_input = -1
        self.selected_output = -1

    def on_hover(self, event):
        # TODO: show x on input socket with connection
        pass

    def sever_input(self, selected_input):
        if self.inputs[selected_input] is None: return
        input_block = self.inputs[selected_input][0]
        input_idx = self.inputs[selected_input][1]
        input_block.outputs[input_idx] = None
        self.inputs[selected_input] = None

    def sever_output(self, selected_output):
        if self.outputs[selected_output] is None: return
        output_block = self.outputs[selected_output][0]
        output_idx = self.outputs[selected_output][1]
        output_block.inputs[output_idx] = None
        self.outputs[selected_output] = None

    def is_input_clear(self, input_idx):
        return self.inputs[input_idx] is None

    def get_x(self):
        return max(0, self.x)

    def get_y(self):
        return max(0, self.y)

    def set_x(self, x):
        self.x = max(0, x)

    def set_y(self, y):
        self.y = max(0, y)

    def get_rect(self):
        return QRect(self.get_x(), self.get_y(), self.get_width(), self.get_height())

    def get_rect(self, max_x, max_y):
        return QRect(min(max_x, max(0, self.x)), min(max_y, max(0, self.y)), self.get_width(), self.get_height())

    def get_rect_f(self):
        return QRectF(self.get_x(), self.get_y(), self.get_width(), self.get_height())

    def get_width(self):
        return max(self.get_text_width() + self.padding[0] * 2, self.get_output_width(), self.get_input_width())

    def get_height(self):
        return self.get_text_height() + self.padding[1] * 2

    def get_text_width(self):
        fm = QFontMetrics(self.font)
        return fm.horizontalAdvance(self.label)

    def get_input_width(self):
        return len(self.inputs) * self.socket_size + (len(self.inputs) + 1) * self.socket_spacing

    def get_output_width(self):
        return len(self.outputs) * self.socket_size + (len(self.outputs) + 1) * self.socket_spacing

    def get_text_height(self):
        fm = QFontMetrics(self.font)
        return fm.height()

    def get_input_x(self, i):
        return (self.get_width() - self.get_input_width()) / 2 + self.get_x() + self.socket_spacing * (i + 1) + self.socket_size * i

    def get_output_x(self, i):
        return (self.get_width() - self.get_output_width()) / 2 + self.get_x() + self.socket_spacing * (i + 1) + self.socket_size * i

    def get_input_y(self):
        return self.get_y()

    def get_output_y(self):
        return self.get_y() + self.get_height() - self.socket_size

    def get_input_rects(self):
        return [QRect(self.get_input_x(i), self.get_input_y(), self.socket_size, self.socket_size) for i in range(len(self.inputs))]

    def get_input_rects_f(self):
        return [QRectF(self.get_input_x(i), self.get_input_y(), self.socket_size, self.socket_size) for i in range(len(self.inputs))]

    def get_output_rects(self):
        return [QRect(self.get_output_x(i), self.get_output_y(), self.socket_size, self.socket_size) for i in range(len(self.inputs))]

    def get_output_rects_f(self):
        return [QRectF(self.get_output_x(i), self.get_output_y(), self.socket_size, self.socket_size) for i in range(len(self.inputs))]

    def draw(self, width, height, painter, event):
        r = self.get_rect(width, height)

        fill_color = self.default_color
        painter.fillRect(r, QBrush(fill_color))

        painter.setPen(self.text_color)
        painter.setFont(self.font)
        painter.drawText(r, Qt.AlignmentFlag.AlignCenter, self.label)

        for r in self.get_input_rects():
            painter.fillRect(r, QBrush(self.socket_color))
        for r in self.get_output_rects():
            painter.fillRect(r, QBrush(self.socket_color))

        painter.setPen(self.line_color)
        if self.selected:
            # if self.selected_input >= 0:
            #     painter.drawLine(self.get_input_x(self.selected_input) + self.socket_size / 2, self.get_input_y() + self.socket_size / 2, self.socket_drag_x, self.socket_drag_y)
            if self.selected_output >= 0:
                painter.drawLine(self.get_output_x(self.selected_output) + self.socket_size / 2, self.get_output_y() + self.socket_size / 2, self.socket_drag_x, self.socket_drag_y)

        i = 0
        for o in self.outputs:
            if o is not None:
                block = o[0]
                idx = o[1]
                center_offset =  + self.socket_size / 2
                painter.drawLine(self.get_output_x(i) + center_offset, self.get_output_y() + center_offset, block.get_input_x(idx) + center_offset, block.get_input_y() + center_offset)
            i+=1



class QuantumCircuit(QWidget):
    def __init__(self, width, height):
        super().__init__()

        self.border_color = QColor(80, 80, 80)

        self.blocks = [
            Block("test", 3, 3),
            Block("test2", 3, 3),
        ]

        self.selected_block = None

        self.setGeometry(0, 0, width, height)

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)

        for block in self.blocks:
            block.draw(self.width(), self.height(), painter, event)

        painter.setPen(self.border_color)
        painter.drawRect(0, 0, self.width() - 2, self.height() - 2)
        painter.end()

    def mouseMoveEvent(self, event):
        if self.selected_block is None: return
        # self.selected_block.set_x(event.position().x() - self.selected_block.selection_offset_x)
        # self.selected_block.set_y(event.position().y() - self.selected_block.selection_offset_y)
        self.selected_block.on_selected_movement(event)
        self.update()

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            for block in self.blocks:
                if block.get_rect_f().contains(event.position()):
                    # TODO: check for input or output pressed
                    self.selected_block = block
                    self.selected_block.on_selected(event)
                    self.update()
                    return
            # self.update()

    def mouseReleaseEvent(self, event):
        if self.selected_block is None: return
        self.selected_block.on_deselected(event, self.blocks)
        self.selected_block = None
        self.update()
        # ensure that the left button was pressed *and* released within the
        # geometry of the widget; if so, emit the signal;
        # if (self.selected_block is not None and
        #         event.button() == Qt.MouseButton.LeftButton
        # ):
        #     self.selected_block
        #     self.update()
        #     self.on_click(self.grid.pressed_node)
        # self.grid.pressed_node.pressed = False
        # self.grid.pressed_node = None