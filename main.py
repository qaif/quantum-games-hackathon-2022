import sys

from PyQt6.QtGui import QPainter
from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QHBoxLayout, QPushButton, QVBoxLayout, QLabel, \
    QScrollArea
from PyQt6.QtCore import Qt

from game_manager import GameManager, Snake, GlobalDirection, GameState, GameStateType, Grid
from probe import ProbeWidget, ProbeInfo, ProbeState


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
        if self.grid.pressed_node is not None and event.button() == Qt.MouseButton.LeftButton:
            if self.grid.pressed_node == self.grid.nodes[self.grid.get_idx_from_canvas(event.position().x(), event.position().y())]:
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


class ScoreWidget(QWidget):
    def __init__(self, game_state):
        super().__init__()
        self.game_state = game_state
        self.game_state.add_on_score_changed_listener(self.on_score_changed)

        base_layout = QHBoxLayout()
        self.setLayout(base_layout)

        self.lives = QLabel("3")
        base_layout.addWidget(QLabel("Lives: "))
        base_layout.addWidget(self.lives)

        self.probes = QLabel("0")
        base_layout.addWidget(QLabel("Probes: "))
        base_layout.addWidget(self.probes)

        self.length = QLabel("2")
        base_layout.addWidget(QLabel("Length: "))
        base_layout.addWidget(self.length)

    def on_score_changed(self):
        self.lives.setText(str(self.game_state.lives))
        self.probes.setText(str(self.game_state.probes))
        self.length.setText(str(self.game_state.length))


class ActionsWidget(QWidget):
    def __init__(self, game_state):
        super().__init__()
        self.game_state = game_state
        # self.game_manager = game_manager
        # self.probe_info = probe_info
        self.game_state.add_on_state_changed_listener(self.on_game_state_changed)

        layout = QHBoxLayout()

        self.probe_button = QPushButton()
        self.probe_button.setText("Probe Start")
        self.probe_button.clicked.connect(self.on_probe)
        layout.addWidget(self.probe_button)

        self.strike_button = QPushButton()
        self.strike_button.setText("Strike")
        self.strike_button.clicked.connect(self.on_strike)
        layout.addWidget(self.strike_button)

        self.restart_button = QPushButton()
        self.restart_button.setText("Restart")
        self.restart_button.clicked.connect(self.on_restart)
        self.restart_button.hide()
        layout.addWidget(self.restart_button)

        self.setLayout(layout)

    def on_game_state_changed(self, last, state):
        if state == GameStateType.TURN_START:
            self.restart_button.hide()
            self.probe_button.setDisabled(False)
            self.strike_button.setDisabled(False)
        elif state == GameStateType.TURN_END:
            pass
        elif state == GameStateType.PROBE_START:
            self.probe_button.setDisabled(True)
            self.strike_button.setDisabled(True)
        elif state == GameStateType.PROBE_END:
            pass
        elif state == GameStateType.STRIKE_START:
            # self.probe_button.setDisabled(True)
            # self.strike_button.setDisabled(True)
            pass
        elif state == GameStateType.STRIKE_CORRECT_GUESS:
            self.probe_button.setDisabled(True)
            self.strike_button.setDisabled(True)
        elif state == GameStateType.STRIKE_END:
            pass
        elif state == GameStateType.GAME_OVER:
            self.probe_button.setDisabled(True)
            self.probe_button.hide()
            self.strike_button.setDisabled(True)
            self.strike_button.hide()
            self.restart_button.show()
        elif state == GameStateType.RESTART:
            self.probe_button.setDisabled(False)
            self.strike_button.setDisabled(False)
            self.restart_button.hide()

    def on_probe(self):
        print("probe")
        self.game_state.set_game_state(GameStateType.PROBE_START)
        # self.game_manager.on_probe_start()
        # self.probe_info.set_probe_state(ProbeState.INPUT_PROBE_VECTOR)

    def on_strike(self):
        print("strike")
        self.game_state.set_game_state(GameStateType.STRIKE_START)
        # self.game_manager.on_strike()

    def on_restart(self):
        print("restart")
        self.game_state.set_game_state(GameStateType.RESTART)


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.game_state = GameState()
        self.grid = Grid(self.game_state, 10, 50)
        self.snake = Snake(self.game_state, self.grid)
        self.probe_info = ProbeInfo(self.game_state)
        self.game_manager = GameManager(self.game_state, self.grid, self.snake, self.probe_info)

        score_widget_height = 30
        actions_widget_height = 60

        mw = QWidget()
        layout = QHBoxLayout()
        mw.setLayout(layout)
        self.setCentralWidget(mw)

        score_widget = ScoreWidget(self.game_state)
        score_widget.setFixedHeight(score_widget_height)

        grid_widget = GridWidget(self.grid)

        actions_widget = ActionsWidget(self.game_state)
        actions_widget.setFixedHeight(actions_widget_height)

        left_widget = QWidget()
        # left_widget = QScrollArea()
        left_layout = QVBoxLayout()
        left_layout.addWidget(score_widget)
        left_layout.addWidget(grid_widget)
        left_layout.addWidget(actions_widget)
        left_widget.setLayout(left_layout)
        left_widget.setMaximumWidth(grid_widget.width())
        left_layout.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        # right_widget = QScrollArea()
        # right_layout = QVBoxLayout()
        probe = ProbeWidget(self.game_state, self.probe_info)
        probe.setMinimumWidth(336)
        # probe.setMaximumWidth(400)

        layout.addWidget(left_widget)
        layout.addWidget(probe)

        self.setGeometry(0, 0, self.grid.width + probe.width(), self.grid.height + actions_widget_height * 2 + score_widget_height)
        self.setWindowTitle('Quantum Snake')

        self.probe_info.set_probe_state(ProbeState.NONE)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_W or event.key() == Qt.Key.Key_Up:
            self.game_manager.on_move(GlobalDirection.UP)
        elif event.key() == Qt.Key.Key_D or event.key() == Qt.Key.Key_Right:
            self.game_manager.on_move(GlobalDirection.RIGHT)
        elif event.key() == Qt.Key.Key_S or event.key() == Qt.Key.Key_Down:
            self.game_manager.on_move(GlobalDirection.DOWN)
        elif event.key() == Qt.Key.Key_A or event.key() == Qt.Key.Key_Left:
            self.game_manager.on_move(GlobalDirection.LEFT)
        event.accept()


def main():
    app = QApplication(sys.argv)
    # grid = GridWidget(Grid(10, 50))
    window = Window()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
