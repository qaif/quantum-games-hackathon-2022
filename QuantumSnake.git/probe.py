from enum import Enum

import numpy as np
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QDoubleValidator, QPixmap, QPalette, QColor
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QRadioButton, QGridLayout, QLineEdit, QLabel, QPushButton, \
    QHBoxLayout, QCheckBox, QFrame, QScrollArea

from game_manager import GameStateType, ProbeDirection, ProbeInputType, ProbeState


# class ProbeDirection(Enum):
#     FORWARD = 0
#     RIGHT = 1
#     LEFT = 2


class ProbeInfo:
    def __init__(self, game_state):
        self.game_state = game_state
        self.game_state.add_on_state_changed_listener(self.on_game_state_changed)

        self.probe_idxs = []
        self.probe_directions = []

        self.input_type = ProbeInputType.NEW
        self.measured_distance = None
        self.measured_probe = None

        self.probe_vector_input = None
        self.probe_vector_output = None

        self.unitary = np.eye(len(self.probe_idxs), dtype=complex)

        self.using_unitary = True

        self.state = ProbeState.NONE

        self.on_state_changed_listeners = []

        self.on_probe_vector_changed_listeners = []
        self.on_probe_vector_output_changed_listeners = []
        self.on_distance_changed_listeners = []

    def on_game_state_changed(self, last, state):
        if state == GameStateType.TURN_START:
            pass
        elif state == GameStateType.TURN_END:
            pass
        elif state == GameStateType.PROBE_START:
            self.probe_vector_input = None
            pass
        elif state == GameStateType.PROBE_END:
            self.set_probe_state(ProbeState.NONE)
        elif state == GameStateType.STRIKE_START:
            pass
        elif state == GameStateType.STRIKE_END:
            pass
        elif state == GameStateType.GAME_OVER:
            pass
        elif state == GameStateType.RESTART:
            pass

    def set_probe_state(self, state):
        # print("changing probe state from: ", self.state, " to: ", state)
        self.state = state
        for listener in self.on_state_changed_listeners:
            listener(state)

    def add_on_state_changed_listener(self, listener):
        self.on_state_changed_listeners.append(listener)

    def init_probe_info(self, idxs, dirs):
        self.probe_idxs = idxs
        self.probe_directions = dirs
        self.set_probe_state(ProbeState.INPUT_PROBE_VECTOR)

    def is_valid_vector(self, v):
        return len(v) > 0 and sum(v) > 0

    def is_valid_unitary(self):
        n = self.unitary.shape[1]
        return (self.unitary.conj().T @ self.unitary - np.eye(n, dtype=complex) < 10**(-10)).all()

    def get_probe_vector(self):
        # TODO: normalize vector and update ui
        # TODO: make correct length

        if self.input_type == ProbeInputType.NEW:
            # self.truncate_vector()
            return self.probe_vector_input
        else:
            if len(self.probe_vector_output) > len(self.probe_idxs):
                # TODO: this should be disabled
                pass
            return self.probe_vector_output

    def get_idx_of_direction(self, direction):
        i = 0
        for d in self.probe_directions:
            if d == direction:
                return i
            i += 1
        return -1

    def set_x(self, x, count):
        if self.probe_vector_input is None: self.probe_vector_input = np.zeros(count, dtype=complex)
        self.probe_vector_input[self.get_idx_of_direction(ProbeDirection.FORWARD)] = x
        self.on_probe_vector_changed()
        # print("new input: ", self.probe_vector_input)

    def set_y(self, y, count):
        if self.probe_vector_input is None: self.probe_vector_input = np.zeros(count, dtype=complex)
        self.probe_vector_input[self.get_idx_of_direction(ProbeDirection.RIGHT)] = y
        self.on_probe_vector_changed()
        # print("new input: ", self.probe_vector_input)

    def set_z(self, z, count):
        if self.probe_vector_input is None: self.probe_vector_input = np.zeros(count, dtype=complex)
        self.probe_vector_input[self.get_idx_of_direction(ProbeDirection.LEFT)] = z
        self.on_probe_vector_changed()
        # print("new input: ", self.probe_vector_input)

    def on_probe_vector_changed(self):
        for listener in self.on_probe_vector_changed_listeners:
            listener()

    def add_on_probe_vector_changed_listener(self, listener):
        self.on_probe_vector_changed_listeners.append(listener)

    def on_probe_vector_output_changed(self):
        for listener in self.on_probe_vector_output_changed_listeners:
            listener()

    def add_on_probe_vector_output_changed_listener(self, listener):
        self.on_probe_vector_output_changed_listeners.append(listener)

    def on_distance_changed(self):
        for listener in self.on_distance_changed_listeners:
            listener()

    def add_on_distance_changed_listener(self, listener):
        self.on_distance_changed_listeners.append(listener)

    def set_measured_distance(self, new):
        # print("distance: ", new)
        self.measured_distance = new
        self.on_distance_changed()

    def set_measured_probe(self, new):
        # print("probe: ", new)
        self.measured_probe = new
        # self.on_probe_changed()

    def clear_measurements(self):
        self.measured_distance = None
        if self.measured_probe is not None:
            self.set_probe_vector_output(None)
        self.measured_probe = None

    def set_probe_vector_output(self, new):
        self.probe_vector_output = new
        self.on_probe_vector_output_changed()


# class ProbeInputType(Enum):
#     NEW = 0
#     OLD = 1


class QueryWidget(QWidget):
    def __init__(self, game_state, probe_info):
        super().__init__()
        self.probe_info = probe_info
        self.probe_info.add_on_state_changed_listener(self.on_state_changed)

        self.count = len(self.probe_info.probe_idxs)

        base_layout = QVBoxLayout()
        base_layout.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)
        # base_layout.addStretch()
        self.setLayout(base_layout)

        self.top_half = QWidget()
        top_layout = QVBoxLayout()
        self.top_half.setLayout(top_layout)
        base_layout.addWidget(self.top_half)

        # TODO: disable radio if old unavailable
        radio_buttons = QWidget()
        top_layout.addWidget(radio_buttons)
        radio_layout = QGridLayout()
        radio_buttons.setLayout(radio_layout)

        self.rbn = QRadioButton("Enter new vector")
        self.rbn.setChecked(True)
        self.rbn.input_type = ProbeInputType.NEW
        self.rbn.toggled.connect(self.on_radio_clicked)
        radio_layout.addWidget(self.rbn, 0, 0)

        # TODO: disable when unavailable (first/last measured)
        self.rbo = QRadioButton("Use previous output")
        self.rbo.input_type = ProbeInputType.OLD
        self.rbo.toggled.connect(self.on_radio_clicked)
        radio_layout.addWidget(self.rbo, 0, 1)

        radio_buttons.setMaximumHeight(50)

        row1 = QWidget()
        top_layout.addWidget(row1)
        row1_layout = QHBoxLayout()
        row1.setLayout(row1_layout)

        self.v1 = QLineEdit("")
        # self.v1.setValidator(QDoubleValidator(0.99, 99.99, 2))
        self.v1.textChanged.connect(self.v1_changed)
        row1_layout.addWidget(QLabel("forward"))
        # self.v1.setDisabled(not self.probe_info.probe_directions.contains(ProbeDirection.FORWARD))
        row1_layout.addWidget(self.v1)

        row2 = QWidget()
        top_layout.addWidget(row2)
        row2_layout = QHBoxLayout()
        row2.setLayout(row2_layout)

        self.v2 = QLineEdit("")
        # self.v2.setValidator(QDoubleValidator(0.99, 99.99, 2))
        self.v2.textChanged.connect(self.v2_changed)
        row2_layout.addWidget(QLabel("right"))
        # self.v2.setDisabled(not self.probe_info.probe_directions.contains(ProbeDirection.RIGHT))
        row2_layout.addWidget(self.v2)

        row3 = QWidget()
        top_layout.addWidget(row3)
        row3_layout = QHBoxLayout()
        row3.setLayout(row3_layout)

        self.v3 = QLineEdit("")
        # self.v3.setValidator(QDoubleValidator(0.99, 99.99, 2))
        self.v3.textChanged.connect(self.v3_changed)
        # self.v3.setDisabled(not self.probe_info.probe_directions.contains(ProbeDirection.LEFT))
        row3_layout.addWidget(QLabel("left"))
        row3_layout.addWidget(self.v3)

        row4 = QWidget()
        base_layout.addWidget(row4)
        row4_layout = QHBoxLayout()
        row4.setLayout(row4_layout)

        query = QPixmap("./query.png")
        query = query.scaled(int(336 / 2), int(574 / 2))
        label = QLabel()
        label.setPixmap(query)
        # label.setFixedWidth(self.width())
        # label.setFixedHeight(self.width())
        row4_layout.addWidget(label)

        row4_layout.addWidget(QLabel("Measured Distance:"))

        self.distance = QLabel(str(self.probe_info.measured_distance))
        row4_layout.addWidget(self.distance)

        self.error_message = QLabel("Invalid vector!")
        self.error_message.setStyleSheet("color: red;")
        base_layout.addWidget(self.error_message)

        self.measure_button = QPushButton("Measure Distance")
        self.measure_button.clicked.connect(self.on_measure_distance)
        base_layout.addWidget(self.measure_button)

        divider = QFrame()
        divider.setFrameShape(QFrame.Shape.HLine)
        divider.sizePolicy()
        divider.setLineWidth(3)
        base_layout.addWidget(divider)

        self.set_disabled()

    def on_state_changed(self, state):
        if state == ProbeState.NONE:
            self.hide()
            self.error_message.hide()
            self.reset_input()
        if state == ProbeState.INPUT_PROBE_VECTOR:
            self.error_message.hide()

            self.rbn.setDisabled(False)
            self.show()
            self.top_half.show()
            self.measure_button.setDisabled(False)
            self.set_disabled()
            self.count = len(self.probe_info.probe_idxs)
            self.distance.setText(str(self.probe_info.measured_distance))
        if state == ProbeState.INVALID_VECTOR_INPUT:
            self.error_message.show()

            self.rbn.setDisabled(False)
            self.show()
            self.top_half.show()
            self.measure_button.setDisabled(False)
            self.set_disabled()
            self.count = len(self.probe_info.probe_idxs)
            self.distance.setText(str(self.probe_info.measured_distance))
        if state == ProbeState.UNITARY_OR_MEASURE:
            # self.reset_input()

            self.error_message.hide()
            # TODO: disable all
            # self.top_half.hide()
            self.rbn.setDisabled(True)
            self.rbo.setDisabled(True)
            self.v1.setDisabled(True)
            self.v2.setDisabled(True)
            self.v3.setDisabled(True)
            self.measure_button.setDisabled(True)
            self.distance.setText(str(self.probe_info.measured_distance))
        if state == ProbeState.MEASURED:
            # TODO: disable all
            # self.top_half.hide()
            self.rbn.setDisabled(True)
            self.rbo.setDisabled(True)
            self.v1.setDisabled(True)
            self.v2.setDisabled(True)
            self.v3.setDisabled(True)
            self.measure_button.setDisabled(True)
            self.distance.setText(str(self.probe_info.measured_distance))

    def reset_input(self):
        self.v1.setText("")
        self.v2.setText("")
        self.v3.setText("")

    def set_disabled(self):
        # print(self.probe_info.probe_directions)
        self.v1.setDisabled(ProbeDirection.FORWARD not in self.probe_info.probe_directions)
        self.v2.setDisabled(ProbeDirection.RIGHT not in self.probe_info.probe_directions)
        self.v3.setDisabled(ProbeDirection.LEFT not in self.probe_info.probe_directions)
        self.rbn.setDisabled(False)
        self.rbo.setDisabled(self.probe_info.probe_vector_output is None)
    # TODO:
    def v1_changed(self, text):
        # print(text)
        try:
            c = complex(text)
            self.probe_info.set_x(c, self.count)
        except ValueError:
            # TODO: display message
            pass

    def v2_changed(self, text):
        try:
            c = complex(text)
            self.probe_info.set_y(c, self.count)
        except ValueError:
            # TODO: display message
            pass

    def v3_changed(self, text):
        try:
            c = complex(text)
            self.probe_info.set_z(c, self.count)
        except ValueError:
            # TODO: display message
            pass

    def on_radio_clicked(self):
        radio_button = self.sender()
        if radio_button.isChecked():
            self.probe_info.input_type = radio_button.input_type
            if radio_button.input_type == ProbeInputType.OLD:
                self.v1.setDisabled(True)
                self.v2.setDisabled(True)
                self.v3.setDisabled(True)
            else:
                self.set_disabled()

    def on_measure_distance(self):
        self.probe_info.set_probe_state(ProbeState.MEASURE_DISTANCE)


class UnitaryWidget(QWidget):
    def __init__(self, game_state, probe_info):
        super().__init__()
        self.probe_info = probe_info
        self.probe_info.add_on_state_changed_listener(self.on_state_changed)

        base_layout = QVBoxLayout()
        self.setLayout(base_layout)

        base_layout.addWidget(QLabel("Apply Unitary Transformation Matrix"))
        # TODO: disable last row and column depending on available
        self.count = len(self.probe_info.probe_idxs)
        # print("number of probeable indices: ", self.count)

        row1 = QWidget()
        base_layout.addWidget(row1)
        row1_layout = QHBoxLayout()
        row1.setLayout(row1_layout)

        # row1_layout.addWidget(QLabel("r1"))

        self.m1 = QLineEdit("0")
        self.m1.setValidator(QDoubleValidator(0.99, 99.99, 2))
        self.m1.textChanged.connect(self.on_unitary_changed)
        row1_layout.addWidget(self.m1)

        # if self.count >= 2:
        self.m2 = QLineEdit("0")
        self.m2.setValidator(QDoubleValidator(0.99, 99.99, 2))
        self.m2.textChanged.connect(self.on_unitary_changed)
        row1_layout.addWidget(self.m2)

            # if self.count >= 3:
        self.m3 = QLineEdit("0")
        self.m3.setValidator(QDoubleValidator(0.99, 99.99, 2))
        self.m3.textChanged.connect(self.on_unitary_changed)
        row1_layout.addWidget(self.m3)

        # if self.count >= 2:
        row2 = QWidget()
        base_layout.addWidget(row2)
        row2_layout = QHBoxLayout()
        row2.setLayout(row2_layout)

        # row2_layout.addWidget(QLabel("r2"))

        self.m4 = QLineEdit("0")
        self.m4.setValidator(QDoubleValidator(0.99, 99.99, 2))
        self.m4.textChanged.connect(self.on_unitary_changed)
        row2_layout.addWidget(self.m4)

        self.m5 = QLineEdit("0")
        self.m5.setValidator(QDoubleValidator(0.99, 99.99, 2))
        self.m5.textChanged.connect(self.on_unitary_changed)
        row2_layout.addWidget(self.m5)

            # if self.count >= 3:
        self.m6 = QLineEdit("0")
        self.m6.setValidator(QDoubleValidator(0.99, 99.99, 2))
        self.m6.textChanged.connect(self.on_unitary_changed)
        row2_layout.addWidget(self.m6)

        row3 = QWidget()
        row3_layout = QHBoxLayout()
        row3.setLayout(row3_layout)

        # row3_layout.addWidget(QLabel("r3"))

        self.m7 = QLineEdit("0")
        self.m7.setValidator(QDoubleValidator(0.99, 99.99, 2))
        self.m7.textChanged.connect(self.on_unitary_changed)
        row3_layout.addWidget(self.m7)

        self.m8 = QLineEdit("0")
        self.m8.setValidator(QDoubleValidator(0.99, 99.99, 2))
        self.m8.textChanged.connect(self.on_unitary_changed)
        row3_layout.addWidget(self.m8)

        self.m9 = QLineEdit("0")
        self.m9.setValidator(QDoubleValidator(0.99, 99.99, 2))
        self.m9.textChanged.connect(self.on_unitary_changed)
        row3_layout.addWidget(self.m9)

        base_layout.addWidget(row3)

        self.error_message = QLabel("Invalid unitary matrix!")
        self.error_message.setStyleSheet("color: red;")
        base_layout.addWidget(self.error_message)

        apply_button = QPushButton("Perform")
        apply_button.clicked.connect(self.on_apply_unitary)
        base_layout.addWidget(apply_button)

        divider = QFrame()
        divider.setFrameShape(QFrame.Shape.HLine)
        divider.sizePolicy()
        divider.setLineWidth(3)
        base_layout.addWidget(divider)

    def on_state_changed(self, state):
        if state == ProbeState.NONE:
            self.hide()
            self.error_message.hide()
        if state == ProbeState.INPUT_PROBE_VECTOR:
            self.hide()
        if state == ProbeState.INVALID_VECTOR_INPUT:
            self.hide()
        if state == ProbeState.UNITARY_OR_MEASURE:
            self.reset_input()
            # self.probe_info.unitary = np.eye(len(self.probe_info.probe_idxs), dtype=complex)
            self.on_show()
            self.error_message.hide()
        if state == ProbeState.APPLY_UNITARY:
            # self.on_show()
            # TODO
            # self.reset_input()
            pass
        if state == ProbeState.INVALID_UNITARY_INPUT:
            self.error_message.show()
        if state == ProbeState.MEASURED:
            self.hide()

    def on_show(self):
        self.show()
        self.count = len(self.probe_info.probe_idxs)
        # print("number of probeable indices: ", self.count)
        self.m2.setDisabled(self.count < 2)
        self.m3.setDisabled(self.count < 3)
        self.m4.setDisabled(self.count < 2)
        self.m5.setDisabled(self.count < 2)
        self.m6.setDisabled(self.count < 3)
        self.m7.setDisabled(self.count < 3)
        self.m8.setDisabled(self.count < 3)
        self.m9.setDisabled(self.count < 3)

    def reset_input(self):
        self.probe_info.unitary = np.eye(len(self.probe_info.probe_idxs), dtype=complex)
        self.m1.setText("1")
        self.m2.setText("0")
        self.m3.setText("0")
        self.m4.setText("0")
        self.m5.setText("1")
        self.m6.setText("0")
        self.m7.setText("0")
        self.m8.setText("0")
        self.m9.setText("1")

    def on_apply_unitary(self):
        self.probe_info.set_probe_state(ProbeState.APPLY_UNITARY)

    def on_unitary_changed(self):
        # print("unitary changed")
        try:
            if self.count == 1:
                self.probe_info.unitary = np.array([[complex(self.m1.text())]])

            if self.count == 2:
                self.probe_info.unitary = np.array([[complex(self.m1.text()), complex(self.m2.text())],
                                                   [complex(self.m4.text()), complex(self.m5.text())]])
            if self.count == 3:
                self.probe_info.unitary = np.array([[complex(self.m1.text()), complex(self.m2.text()), complex(self.m3.text())],
                                                   [complex(self.m4.text()), complex(self.m5.text()), complex(self.m6.text())],
                                                   [complex(self.m7.text()), complex(self.m8.text()), complex(self.m9.text())]])
            # self.probe_info.set_probe_state(ProbeState.UNITARY_OR_MEASURE)
            self.error_message.hide()
        except ValueError:
            # print("INVALID MATRIX!!!")
            # self.error_message.hide()
            self.probe_info.set_probe_state(ProbeState.INVALID_UNITARY_INPUT)


class MeasureWidget(QWidget):
    def __init__(self, game_state, probe_info):
        super(MeasureWidget, self).__init__()
        self.probe_info = probe_info
        self.rng = np.random.default_rng()
        self.probe_info.add_on_state_changed_listener(self.on_state_changed)

        base_layout = QVBoxLayout()
        self.setLayout(base_layout)

        self.measure_button = QPushButton("Measure")
        self.measure_button.clicked.connect(self.on_measure_clicked)
        base_layout.addWidget(self.measure_button)

        base_layout.addWidget(QLabel("Measured Probe:"))
        self.vector = QLabel("NONE")  # TODO
        base_layout.addWidget(self.vector)

        divider = QFrame()
        divider.setFrameShape(QFrame.Shape.HLine)
        divider.sizePolicy()
        divider.setLineWidth(3)
        base_layout.addWidget(divider)

    def on_state_changed(self, state):
        if state == ProbeState.NONE:
            self.hide()
        if state == ProbeState.INPUT_PROBE_VECTOR:
            self.hide()
        if state == ProbeState.UNITARY_OR_MEASURE:
            self.measure_button.setDisabled(False)
            self.show()
            self.vector.setText(self.probe_direction_to_string(self.probe_info.measured_probe))
        if state == ProbeState.MEASURED:
            self.measure_button.setDisabled(True)
            self.show()
            self.vector.setText(self.probe_direction_to_string(self.probe_info.measured_probe))

    def probe_direction_to_string(self, direction):
        if direction == ProbeDirection.FORWARD:
            return "f"
        elif direction == ProbeDirection.RIGHT:
            return "r"
        elif direction == ProbeDirection.LEFT:
            return "l"

    def on_measure_clicked(self):
        # print("measure clicked")
        self.probe_info.set_probe_state(ProbeState.MEASURE_PROBE_VECTOR)


class ContinueWidget(QWidget):
    def __init__(self, game_state, probe_info):
        super(ContinueWidget, self).__init__()
        self.game_state = game_state
        self.probe_info = probe_info
        self.rng = np.random.default_rng()
        self.probe_info.add_on_state_changed_listener(self.on_state_changed)

        base_layout = QVBoxLayout()
        self.setLayout(base_layout)

        finish_button = QPushButton("Continue")
        finish_button.clicked.connect(self.on_finish_clicked)
        base_layout.addWidget(finish_button)

    def on_state_changed(self, state):
        if state == ProbeState.NONE:
            self.hide()
        if state == ProbeState.INPUT_PROBE_VECTOR:
            self.show()
        if state == ProbeState.UNITARY_OR_MEASURE:
            self.show()
        if state == ProbeState.MEASURED:
            self.show()

    def on_finish_clicked(self):
        # print("finish clicked")
        self.probe_info.set_probe_state(ProbeState.NONE)
        self.game_state.set_game_state(GameStateType.PROBE_END)


# class ProbeState(Enum):
#     NONE = 0
#     INPUT_PROBE_VECTOR = 1
#     UNITARY_MEASURE = 2
#     MEASURED = 3


class ProbeWidget(QWidget):
    def __init__(self, game_state, probe_info):
        super().__init__()
        # self.probe_vector = [1, 0, 0]
        # self.on_probe_vector_changed_listeners = []
        self.game_state = game_state
        self.probe_info = probe_info

        # self.probe_info.add_on_distance_changed_listener(self.on_distance_changed)

        base_base_layout = QVBoxLayout()
        # base_base_layout.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)
        self.setLayout(base_base_layout)

        scroll = QScrollArea()
        base_base_layout.addWidget(scroll)
        scroll.setWidgetResizable(True)
        scroll_content = QWidget(scroll)
        scroll.setWidget(scroll_content)

        base_layout = QVBoxLayout()
        scroll_content.setLayout(base_layout)
        base_layout.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)

        # QUERY
        self.query_widget = QueryWidget(self.game_state, self.probe_info)
        base_layout.addWidget(self.query_widget)

        # UNITARY
        self.unitary_widget = UnitaryWidget(self.game_state, self.probe_info)
        base_layout.addWidget(self.unitary_widget)

        # MEASURE
        measure = MeasureWidget(self.game_state, self.probe_info)
        base_layout.addWidget(measure)

        # CONTINUE
        finish_widget = ContinueWidget(self.game_state, self.probe_info)
        base_layout.addWidget(finish_widget)

        # self.setLayout(base_layout)

