from enum import Enum

import numpy as np
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QDoubleValidator, QPixmap
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QRadioButton, QGridLayout, QLineEdit, QLabel, QPushButton, \
    QHBoxLayout, QCheckBox, QFrame


class ProbeDirection(Enum):
    FORWARD = 0
    RIGHT = 1
    LEFT = 2


class ProbeInfo:
    def __init__(self):
        self.probe_idxs = []
        self.probe_directions = []  # TODO: set this

        self.input_type = ProbeInputType.NEW
        self.measured_distance = -1
        # self.measured_vector = [-1.0, -1.0, -1.0]
        # self.measured_probe = ProbeDirection.FORWARD
        self.measured_probe = None

        # self.probe_vector = [1.0, 0.0, 0.0]
        self.probe_vector_input = [0,0,0]
        self.probe_vector_output = [0,0,0]

        self.unitary = np.matrix([[0.0, 0.0, 0.0],
                                 [0.0, 0.0, 0.0],
                                 [0.0, 0.0, 0.0]])
        self.using_unitary = True

        self.state = ProbeState.NONE

        self.on_state_changed_listeners = []

        self.on_probe_vector_changed_listeners = []
        self.on_probe_vector_output_changed_listeners = []
        self.on_distance_changed_listeners = []

    def set_probe_state(self, state):
        self.state = state
        for listener in self.on_state_changed_listeners:
            listener(state)

    def add_on_state_changed_listener(self, listener):
        self.on_state_changed_listeners.append(listener)

    def set_probe_idxs(self, probe_idxs):
        self.probe_idxs = probe_idxs

    def set_probe_directions(self, probe_directions):
        self.probe_directions = probe_directions

    def get_probe_vector(self):
        # TODO: normalize vector and update ui
        if self.input_type == ProbeInputType.NEW:
            return self.probe_vector
        else:
            return self.probe_vector_output

    def set_x(self, x):
        self.probe_vector_input[0] = x
        self.on_probe_vector_changed()

    def set_y(self, y):
        self.probe_vector_input[1] = y
        self.on_probe_vector_changed()

    def set_z(self, z):
        self.probe_vector_input[2] = z
        self.on_probe_vector_changed()

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
        print("distance: ", new)
        self.measured_distance = new
        self.on_distance_changed()

    def set_probe_vector_output(self, new):
        self.probe_vector_output = new
        self.on_probe_vector_output_changed()


class ProbeInputType(Enum):
    NEW = 0
    OLD = 1


class QueryWidget(QWidget):
    def __init__(self, probe_info):
        super().__init__()
        self.probe_info = probe_info
        self.probe_info.add_on_state_changed_listener(self.on_state_changed)

        base_layout = QVBoxLayout()
        base_layout.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)
        self.setLayout(base_layout)

        # TODO: disable radio if old unavailable
        radio_buttons = QWidget()
        base_layout.addWidget(radio_buttons)
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
        base_layout.addWidget(row1)
        row1_layout = QHBoxLayout()
        row1.setLayout(row1_layout)

        self.v1 = QLineEdit("")
        self.v1.setValidator(QDoubleValidator(0.99, 99.99, 2))
        self.v1.textChanged.connect(self.v1_changed)
        row1_layout.addWidget(QLabel("forward"))
        # self.v1.setDisabled(not self.probe_info.probe_directions.contains(ProbeDirection.FORWARD))
        row1_layout.addWidget(self.v1)

        row2 = QWidget()
        base_layout.addWidget(row2)
        row2_layout = QHBoxLayout()
        row2.setLayout(row2_layout)

        self.v2 = QLineEdit("")
        self.v2.setValidator(QDoubleValidator(0.99, 99.99, 2))
        self.v2.textChanged.connect(self.v2_changed)
        row2_layout.addWidget(QLabel("right"))
        # self.v2.setDisabled(not self.probe_info.probe_directions.contains(ProbeDirection.RIGHT))
        row2_layout.addWidget(self.v2)

        row3 = QWidget()
        base_layout.addWidget(row3)
        row3_layout = QHBoxLayout()
        row3.setLayout(row3_layout)

        self.v3 = QLineEdit("")
        self.v3.setValidator(QDoubleValidator(0.99, 99.99, 2))
        self.v3.textChanged.connect(self.v3_changed)
        # self.v3.setDisabled(not self.probe_info.probe_directions.contains(ProbeDirection.LEFT))
        row3_layout.addWidget(QLabel("left"))
        row3_layout.addWidget(self.v3)

        query = QPixmap("./query.png")
        query = query.scaled(300, 300)
        label = QLabel()
        label.setPixmap(query)
        # label.setFixedWidth(self.width())
        # label.setFixedHeight(self.width())
        base_layout.addWidget(label)

        base_layout.addWidget(QLabel("Measured Distance:"))

        self.distance = QLabel(str(self.probe_info.measured_distance))
        base_layout.addWidget(self.distance)

        query_button = QPushButton("Measure Distance")
        query_button.clicked.connect(self.on_measure_distance)
        base_layout.addWidget(query_button)

        divider = QFrame()
        divider.setFrameShape(QFrame.Shape.HLine)
        divider.sizePolicy()
        divider.setLineWidth(3)
        base_layout.addWidget(divider)

        self.set_disabled()

    def on_state_changed(self, state):
        if state == ProbeState.NONE:
            self.hide()
        if state == ProbeState.INPUT_PROBE_VECTOR:
            self.show()
            self.set_disabled()
        if state == ProbeState.UNITARY_MEASURE:
            # TODO: disable all
            self.hide()
        if state == ProbeState.MEASURED:
            # TODO: disable all
            self.hide()

    def set_disabled(self):
        self.v1.setDisabled(ProbeDirection.FORWARD not in self.probe_info.probe_directions)
        self.v2.setDisabled(ProbeDirection.RIGHT not in self.probe_info.probe_directions)
        self.v3.setDisabled(ProbeDirection.LEFT not in self.probe_info.probe_directions)
        # TODO: disable radio
        self.rbo.setDisabled(self.probe_info.probe_vector_output is None)


    def v1_changed(self, text):
        self.probe_info.set_x(float(text))

    def v2_changed(self, text):
        self.probe_info.set_y(float(text))

    def v3_changed(self, text):
        self.probe_info.set_z(float(text))

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
        # TODO
        self.probe_info.set_probe_state(ProbeState.UNITARY_MEASURE)
        pass


class UnitaryWidget(QWidget):
    def __init__(self, probe_info):
        super().__init__()
        self.probe_info = probe_info
        self.probe_info.add_on_state_changed_listener(self.on_state_changed)

        base_layout = QVBoxLayout()
        self.setLayout(base_layout)

        base_layout.addWidget(QLabel("Apply Unitary Transformation Matrix"))
        # TODO: disable last row and column depending on available
        self.count = len(self.probe_info.probe_idxs)

        row1 = QWidget()
        base_layout.addWidget(row1)
        row1_layout = QHBoxLayout()
        row1.setLayout(row1_layout)

        # row1_layout.addWidget(QLabel("r1"))

        self.m1 = QLineEdit("0")
        self.m1.setValidator(QDoubleValidator(0.99, 99.99, 2))
        self.m1.textChanged.connect(self.on_unitary_changed)
        row1_layout.addWidget(self.m1)

        if self.count >= 2:
            self.m2 = QLineEdit("0")
            self.m2.setValidator(QDoubleValidator(0.99, 99.99, 2))
            self.m2.textChanged.connect(self.on_unitary_changed)
            row1_layout.addWidget(self.m2)

            if self.count >= 3:
                self.m3 = QLineEdit("0")
                self.m3.setValidator(QDoubleValidator(0.99, 99.99, 2))
                self.m3.textChanged.connect(self.on_unitary_changed)
                row1_layout.addWidget(self.m3)

        if self.count >= 2:
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

            if self.count >= 3:
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
        if state == ProbeState.INPUT_PROBE_VECTOR:
            self.hide()
        if state == ProbeState.UNITARY_MEASURE:
            self.show()
        if state == ProbeState.MEASURED:
            self.hide()

    def on_apply_unitary(self):
        n = self.probe_info.unitary.shape[1]
        assert n == len(self.probe_info.probe_vector_output), 'Probe vector dimension doesn\'t match.'
        assert n == self.probe_info.unitary.shape[0], 'Given matrix not square'
        # TODO BROKEN!!!!!
        # assert self.probe_info.unitary.conj().T @ self.probe_info.unitary == np.eye(n), 'Given matrix not unitary'
        if self.probe_info.unitary.conj().T @ self.probe_info.unitary == np.eye(n):
            self.probe_info.probe_vector_output = self.probe_info.unitary @ self.probe_info.get_probe_vector()
            # TODO: clear text fields to signal transformation was applied
        else:
            print("GIVEN MATRIX NOT UNITARY!!!")
            # TODO: display warning, transform not applied

    def on_unitary_changed(self):
        print("unitary changed")
        if self.count == 1:
            self.probe_info.unitary = np.matrix([[float(self.m1.text())]])
        if self.count == 2:
            self.probe_info.unitary = np.matrix([[float(self.m1.text()), float(self.m2.text())],
                                             [float(self.m4.text()), float(self.m5.text())]])
        if self.count == 3:
            self.probe_info.unitary = np.matrix([[float(self.m1.text()), float(self.m2.text()), float(self.m3.text())],
                                             [float(self.m4.text()), float(self.m5.text()), float(self.m6.text())],
                                             [float(self.m7.text()), float(self.m8.text()), float(self.m9.text())]])


class MeasureWidget(QWidget):
    def __init__(self, probe_info):
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
        if state == ProbeState.UNITARY_MEASURE:
            self.measure_button.setDisabled(False)
            self.show()
        if state == ProbeState.MEASURED:
            self.measure_button.setDisabled(True)
            self.show()

    def on_measure_clicked(self):
        print("measure clicked")
        self.probe_info.set_probe_state(ProbeState.MEASURED)

        self.probe_info.measured_probe = self.probe_measurement()

    def probe_measurement(self):
        probabilities = np.abs(self.probe_info.probe_vector_output) ** 2  # probabilities of different outcomes
        # Randomly choose a direction according to Born rule probabilities.
        return self.rng.choice(self.probe_info.probe_directions, p=probabilities)


class ContinueWidget(QWidget):
    def __init__(self, probe_info):
        super(ContinueWidget, self).__init__()
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
        if state == ProbeState.UNITARY_MEASURE:
            self.show()
        if state == ProbeState.MEASURED:
            self.show()

    def on_finish_clicked(self):
        print("finish clicked")
        self.probe_info.set_probe_state(ProbeState.NONE)


class ProbeState(Enum):
    NONE = 0
    INPUT_PROBE_VECTOR = 1
    UNITARY_MEASURE = 2
    MEASURED = 3


class ProbeWidget(QWidget):
    def __init__(self, probe_info):
        super().__init__()
        # self.probe_vector = [1, 0, 0]
        # self.on_probe_vector_changed_listeners = []
        self.probe_info = probe_info

        # self.probe_info.add_on_distance_changed_listener(self.on_distance_changed)

        base_layout = QVBoxLayout()
        base_layout.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)

        # QUERY
        self.query_widget = QueryWidget(self.probe_info)
        base_layout.addWidget(self.query_widget)

        # DIVIDER
        # divider = QFrame()
        # divider.setFrameShape(QFrame.Shape.HLine)
        # divider.sizePolicy()
        # divider.setLineWidth(3)
        # base_layout.addWidget(divider)

        # UNITARY
        self.unitary_widget = UnitaryWidget(self.probe_info)
        base_layout.addWidget(self.unitary_widget)

        # DIVIDER
        # divider = QFrame()
        # divider.setFrameShape(QFrame.Shape.HLine)
        # divider.sizePolicy()
        # divider.setLineWidth(3)
        # base_layout.addWidget(divider)

        # MEASURE
        measure = MeasureWidget(self.probe_info)
        base_layout.addWidget(measure)

        # DIVIDER
        # divider = QFrame()
        # divider.setFrameShape(QFrame.Shape.HLine)
        # divider.sizePolicy()
        # divider.setLineWidth(3)
        # base_layout.addWidget(divider)

        # CONTINUE
        finish_widget = ContinueWidget(self.probe_info)
        base_layout.addWidget(finish_widget)

        self.setLayout(base_layout)

    # def vector_to_text(self, vector):
    #     text = ""
    #     for e in vector:
    #         text += str(e) + ", "
    #     # return text.removesuffix(", ")
    #     return text

