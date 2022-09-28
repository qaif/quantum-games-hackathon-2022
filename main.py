import sys

from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QHBoxLayout, QPushButton, QVBoxLayout
from PyQt6.QtCore import Qt

from game_manager import GameManager, Snake, GlobalDirection
from grid import Grid, GridWidget
from probe import ProbeWidget


class ActionsWidget(QWidget):
    def __init__(self, game_manager):
        super().__init__()
        self.game_manager = game_manager

        layout = QHBoxLayout()

        probe_button = QPushButton()
        probe_button.setText("Probe")
        probe_button.clicked.connect(self.on_probe)
        layout.addWidget(probe_button)

        # TODO: disable button when no selection
        strike_button = QPushButton()
        strike_button.setText("Strike")
        strike_button.clicked.connect(self.on_strike)
        layout.addWidget(strike_button)

        self.setLayout(layout)

    def on_probe(self):
        print("probe")
        self.game_manager.on_probe()

    def on_strike(self):
        print("strike")
        self.game_manager.on_strike()


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.grid = Grid(10, 50)
        self.snake = Snake(self.grid)
        self.game_manager = GameManager(self.grid, self.snake)
        # self.game_manager = GameManager()

        actions_widget_height = 60

        mw = QWidget()
        layout = QHBoxLayout()
        mw.setLayout(layout)
        self.setCentralWidget(mw)

        # grid = Grid(10, 50)
        grid_widget = GridWidget(self.grid)
        actions_widget = ActionsWidget(self.game_manager)
        actions_widget.setFixedHeight(actions_widget_height)

        # circuit = CircuitBuilderWidget(100, 100)
        probe = ProbeWidget(100, 100)

        self.setGeometry(0, 0, self.grid.width + self.grid.width, self.grid.height + actions_widget_height)
        self.setWindowTitle('Quantum Snake')

        left_widget = QWidget()
        left_layout = QVBoxLayout()
        left_layout.addWidget(grid_widget)
        left_layout.addWidget(actions_widget)
        left_widget.setLayout(left_layout)

        layout.addWidget(left_widget)
        layout.addWidget(probe)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_W or event.key() == Qt.Key.Key_Up:
            self.snake.move(GlobalDirection.UP)
        elif event.key() == Qt.Key.Key_D or event.key() == Qt.Key.Key_Right:
            self.snake.move(GlobalDirection.RIGHT)
        elif event.key() == Qt.Key.Key_S or event.key() == Qt.Key.Key_Down:
            self.snake.move(GlobalDirection.DOWN)
        elif event.key() == Qt.Key.Key_A or event.key() == Qt.Key.Key_Left:
            self.snake.move(GlobalDirection.LEFT)
        event.accept()


def main():
    app = QApplication(sys.argv)
    # grid = GridWidget(Grid(10, 50))
    window = Window()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
