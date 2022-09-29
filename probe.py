from enum import Enum

import numpy as np
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QDoubleValidator, QPixmap
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QRadioButton, QGridLayout, QLineEdit, QLabel, QPushButton, \
    QHBoxLayout, QCheckBox


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

        self.on_probe_vector_changed_listeners = []
        self.on_probe_vector_output_changed_listeners = []
        self.on_distance_changed_listeners = []

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

        base_layout = QVBoxLayout()
        base_layout.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)
        self.setLayout(base_layout)

        # TODO: disable radio if old unavailable
        radio_buttons = QWidget()
        base_layout.addWidget(radio_buttons)
        radio_layout = QGridLayout()
        radio_buttons.setLayout(radio_layout)

        rb = QRadioButton("Enter new vector")
        rb.setChecked(True)
        rb.input_type = ProbeInputType.NEW
        rb.toggled.connect(self.on_radio_clicked)
        radio_layout.addWidget(rb, 0, 0)

        # TODO: disable when unavailable (first/last measured)
        rb = QRadioButton("Use previous output")
        rb.input_type = ProbeInputType.OLD
        rb.toggled.connect(self.on_radio_clicked)
        radio_layout.addWidget(rb, 0, 1)

        radio_buttons.setMaximumHeight(50)

        row1 = QWidget()
        base_layout.addWidget(row1)
        row1_layout = QHBoxLayout()
        row1.setLayout(row1_layout)

        self.v1 = QLineEdit("")
        self.v1.setValidator(QDoubleValidator(0.99, 99.99, 2))
        self.v1.textChanged.connect(self.v1_changed)
        row1_layout.addWidget(QLabel("forward"))
        row1_layout.addWidget(self.v1)

        row2 = QWidget()
        base_layout.addWidget(row2)
        row2_layout = QHBoxLayout()
        row2.setLayout(row2_layout)

        self.v2 = QLineEdit("")
        self.v2.setValidator(QDoubleValidator(0.99, 99.99, 2))
        self.v2.textChanged.connect(self.v2_changed)
        row2_layout.addWidget(QLabel("right"))
        row2_layout.addWidget(self.v2)

        row3 = QWidget()
        base_layout.addWidget(row3)
        row3_layout = QHBoxLayout()
        row3.setLayout(row3_layout)

        self.v3 = QLineEdit("")
        self.v3.setValidator(QDoubleValidator(0.99, 99.99, 2))
        self.v3.textChanged.connect(self.v3_changed)
        row3_layout.addWidget(QLabel("left"))
        row3_layout.addWidget(self.v3)

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
            disabled = radio_button.input_type == ProbeInputType.OLD
            self.v1.setDisabled(disabled)
            self.v2.setDisabled(disabled)
            self.v3.setDisabled(disabled)


class UnitaryWidget(QWidget):
    def __init__(self, probe_info):
        super().__init__()

        self.probe_info = probe_info

        base_layout = QVBoxLayout()
        self.setLayout(base_layout)

        base_layout.addWidget(QLabel("Apply Unitary Transformation Matrix"))
        # TODO: disable last row and column depending on available
        count = len(self.probe_info.probe_idxs)

        row1 = QWidget()
        base_layout.addWidget(row1)
        row1_layout = QHBoxLayout()
        row1.setLayout(row1_layout)

        # row1_layout.addWidget(QLabel("r1"))

        self.m1 = QLineEdit("0")
        self.m1.setValidator(QDoubleValidator(0.99, 99.99, 2))
        self.m1.textChanged.connect(self.on_unitary_changed)
        row1_layout.addWidget(self.m1)

        if count >= 2:
            self.m2 = QLineEdit("0")
            self.m2.setValidator(QDoubleValidator(0.99, 99.99, 2))
            self.m2.textChanged.connect(self.on_unitary_changed)
            row1_layout.addWidget(self.m2)

            if count >= 3:
                self.m3 = QLineEdit("0")
                self.m3.setValidator(QDoubleValidator(0.99, 99.99, 2))
                self.m3.textChanged.connect(self.on_unitary_changed)
                row1_layout.addWidget(self.m3)

        if count >= 2:
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

            if count >= 3:
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

    def on_apply_unitary(self):
        n = self.probe_info.unitary.shape[1]
        assert n == len(self.probe_info.probe_vector_output), 'Probe vector dimension doesn\'t match.'
        assert n == self.probe_info.unitary.shape[0], 'Given matrix not square'
        # TODO BROKEN!!!!!
        # assert self.probe_info.unitary.conj().T @ self.probe_info.unitary == np.eye(n), 'Given matrix not unitary'
        if self.probe_info.unitary.conj().T @ self.probe_info.unitary == np.eye(n):
            self.probe_info.probe_vector_output = self.probe_info.unitary @ self.probe_info.get_probe_vector()
        else:
            print("GIVEN MATRIX NOT UNITARY!!!")
            # TODO: display warning, transform not applied

    def on_unitary_changed(self):
        print("unitary changed")
        self.probe_info.unitary = np.matrix([[float(self.m1.text()), float(self.m2.text()), float(self.m3.text())],
                                             [float(self.m4.text()), float(self.m5.text()), float(self.m6.text())],
                                             [float(self.m7.text()), float(self.m8.text()), float(self.m9.text())]])


class ProbeWidget(QWidget):
    def __init__(self, probe_info):
        super().__init__()
        # self.probe_vector = [1, 0, 0]
        # self.on_probe_vector_changed_listeners = []
        self.probe_info = probe_info

        self.probe_info.add_on_distance_changed_listener(self.on_distance_changed)

        base_layout = QVBoxLayout()
        base_layout.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)

        query_widget = QueryWidget(self.probe_info)
        base_layout.addWidget(query_widget)

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

        # TODO: divider, below invisible

        # base_layout.addWidget(QLabel("Apply Unitary Transformation Matrix"))
        # if self.probe_info.using_unitary: base_layout.addWidget(UnitaryWidget(self.probe_info))
        # if self.using_unitary_check.isChecked(): base_layout.addWidget(UnitaryWidget(self.probe_info))
        self.unitary_widget = UnitaryWidget(self.probe_info)
        base_layout.addWidget(self.unitary_widget)

        measure_button = QPushButton("Measure")
        measure_button.clicked.connect(self.on_measure_clicked)
        base_layout.addWidget(measure_button)

        base_layout.addWidget(QLabel("Measured Probe:"))
        self.vector = QLabel(
            # TODO
        )
        base_layout.addWidget(self.vector)

        self.setLayout(base_layout)

    # def init_image_layout(self):
    #     self.query = QPixmap("./query.png")
    #     self.label = QLabel()
    #     self.label.setPixmap(self.query)

    def on_distance_changed(self):
        self.distance.setText(str(self.probe_info.measured_distance))

    # def on_unitary_checked(self):
    #     check = self.sender()
    #     self.probe_info.using_unitary = check.isChecked()
    #     self.unitary_widget.setDisabled(not check.isChecked())

    def vector_to_text(self, vector):
        text = ""
        for e in vector:
            text += str(e) + ", "
        # return text.removesuffix(", ")
        return text

    def on_measure_distance(self):
        pass

    def on_measure_clicked(self):
        print("measure clicked")

        self.probe_info.measured_probe = ProbeDirection.FORWARD

