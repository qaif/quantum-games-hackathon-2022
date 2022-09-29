from enum import Enum

import numpy as np
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QDoubleValidator, QPixmap
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QRadioButton, QGridLayout, QLineEdit, QLabel, QPushButton, \
    QHBoxLayout, QCheckBox


class ProbeInfo:
    def __init__(self):
        self.input_type = ProbeInputType.NEW
        self.measured_distance = -1
        self.measured_vector = [-1.0, -1.0, -1.0]

        self.probe_vector = [1.0, 0.0, 0.0]
        self.probe_vector_output = [0.0, 0.0, 0.0]

        self.unitary = np.matrix([[0.0, 0.0, 0.0],
                                 [0.0, 0.0, 0.0],
                                 [0.0, 0.0, 0.0]])
        self.using_unitary = True

        self.on_probe_vector_changed_listeners = []
        self.on_probe_vector_output_changed_listeners = []
        self.on_distance_changed_listeners = []

    def get_probe_vector(self):
        if self.input_type == ProbeInputType.NEW:
            return self.probe_vector
        else:
            return self.probe_vector_output

    def set_x(self, x):
        self.probe_vector[0] = x
        self.on_probe_vector_changed()

    def set_y(self, y):
        self.probe_vector[1] = y
        self.on_probe_vector_changed()

    def set_z(self, z):
        self.probe_vector[2] = z
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


class UnitaryWidget(QWidget):
    def __init__(self, probe_info):
        super().__init__()

        self.probe_info = probe_info

        base_layout = QVBoxLayout()
        self.setLayout(base_layout)

        row1 = QWidget()
        row1_layout = QHBoxLayout()
        row1.setLayout(row1_layout)

        # row1_layout.addWidget(QLabel("r1"))

        self.m1 = QLineEdit("0")
        self.m1.setValidator(QDoubleValidator(0.99, 99.99, 2))
        self.m1.textChanged.connect(self.on_unitary_changed)
        row1_layout.addWidget(self.m1)

        self.m2 = QLineEdit("0")
        self.m2.setValidator(QDoubleValidator(0.99, 99.99, 2))
        self.m2.textChanged.connect(self.on_unitary_changed)
        row1_layout.addWidget(self.m2)

        self.m3 = QLineEdit("0")
        self.m3.setValidator(QDoubleValidator(0.99, 99.99, 2))
        self.m3.textChanged.connect(self.on_unitary_changed)
        row1_layout.addWidget(self.m3)

        row2 = QWidget()
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

        base_layout.addWidget(row1)
        base_layout.addWidget(row2)
        base_layout.addWidget(row3)

    def on_unitary_changed(self):
        print("unitary changed")
        self.probe_info.unitary = np.matrix([[self.m1, self.m2, self.m3],
                                             [self.m4, self.m5, self.m6],
                                             [self.m7, self.m8, self.m9]])
        # self.probe_info.unitary = np.zeros((3, 3))


class ProbeWidget(QWidget):
    def __init__(self, probe_info):
        super().__init__()
        # self.probe_vector = [1, 0, 0]
        # self.on_probe_vector_changed_listeners = []
        self.probe_info = probe_info

        self.probe_info.add_on_distance_changed_listener(self.on_distance_changed)

        base_layout = QVBoxLayout()
        base_layout.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)

        base_layout.addWidget(self.init_radio_widget())

        self.v1 = QLineEdit("1")
        self.v1.setValidator(QDoubleValidator(0.99, 99.99, 2))
        self.v1.textChanged.connect(self.v1_changed)
        base_layout.addWidget(QLabel("forward"))
        base_layout.addWidget(self.v1)

        self.v2 = QLineEdit("0")
        self.v2.setValidator(QDoubleValidator(0.99, 99.99, 2))
        self.v2.textChanged.connect(self.v2_changed)
        base_layout.addWidget(QLabel("right"))
        base_layout.addWidget(self.v2)

        self.v3 = QLineEdit("0")
        self.v3.setValidator(QDoubleValidator(0.99, 99.99, 2))
        self.v3.textChanged.connect(self.v3_changed)
        base_layout.addWidget(QLabel("left"))
        base_layout.addWidget(self.v3)

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

        self.using_unitary_check = QCheckBox("Apply Unitary Transformation Matrix")
        self.using_unitary_check.setChecked(True)
        self.using_unitary_check.toggled.connect(self.on_unitary_checked)
        base_layout.addWidget(self.using_unitary_check)
        # if self.probe_info.using_unitary: base_layout.addWidget(UnitaryWidget(self.probe_info))
        # if self.using_unitary_check.isChecked(): base_layout.addWidget(UnitaryWidget(self.probe_info))
        self.unitary_widget = UnitaryWidget(self.probe_info)
        base_layout.addWidget(self.unitary_widget)

        measure_button = QPushButton("Measure")
        measure_button.clicked.connect(self.on_measure_clicked)
        base_layout.addWidget(measure_button)

        base_layout.addWidget(QLabel("Measured Vector:"))
        self.vector = QLabel(str(self.probe_info.measured_vector[0]) + ", " + str(self.probe_info.measured_vector[1]) + ", " + str(self.probe_info.measured_vector[2]))
        base_layout.addWidget(self.vector)

        self.setLayout(base_layout)

    def init_radio_widget(self):
        w = QWidget()
        layout = QGridLayout()
        w.setLayout(layout)

        radio_buttons = QRadioButton("Enter new vector")
        radio_buttons.setChecked(True)
        radio_buttons.input_type = ProbeInputType.NEW
        radio_buttons.toggled.connect(self.on_radio_clicked)
        layout.addWidget(radio_buttons, 0, 0)

        radio_buttons = QRadioButton("Use previous output")
        radio_buttons.input_type = ProbeInputType.OLD
        radio_buttons.toggled.connect(self.on_radio_clicked)
        layout.addWidget(radio_buttons, 0, 1)

        w.setMaximumHeight(50)

        return w

    # def init_image_layout(self):
    #     self.query = QPixmap("./query.png")
    #     self.label = QLabel()
    #     self.label.setPixmap(self.query)

    def on_radio_clicked(self):
        radio_button = self.sender()
        if radio_button.isChecked():
            self.probe_info.input_type = radio_button.input_type
            disabled = radio_button.input_type == ProbeInputType.OLD
            self.v1.setDisabled(disabled)
            self.v2.setDisabled(disabled)
            self.v3.setDisabled(disabled)
            # TODO: make input invisible

    def v1_changed(self, text):
        self.probe_info.set_x(float(text))

    def v2_changed(self, text):
        self.probe_info.set_y(float(text))

    def v3_changed(self, text):
        self.probe_info.set_z(float(text))

    def on_distance_changed(self):
        self.distance.setText(str(self.probe_info.measured_distance))

    def on_unitary_checked(self):
        check = self.sender()
        self.probe_info.using_unitary = check.isChecked()
        self.unitary_widget.setDisabled(not check.isChecked())

    def vector_to_text(self, vector):
        text = ""
        for e in vector:
            text += str(e) + ", "
        # return text.removesuffix(", ")
        return text

    def on_measure_clicked(self):
        print("measure clicked")

        if not self.probe_info.using_unitary:
            self.probe_info.measured_vector = self.probe_info.probe_vector_output
        else:
            n = self.probe_info.unitary.shape[1]
            assert n == len(self.probe_info.probe_vector_output), 'Probe vector dimension doesn\'t match.'
            assert n == self.probe_info.unitary.shape[0], 'Given matrix not square'
            # TODO BROKEN!!!!!
            # assert self.probe_info.unitary.conj().T @ self.probe_info.unitary == np.eye(n), 'Given matrix not unitary'
            if self.probe_info.unitary.conj().T @ self.probe_info.unitary == np.eye(n):
                # self.probe_info.probe_vector_output = self.probe_info.unitary @ self.probe_info.get_probe_vector()
                self.probe_info.probe_vector_output = None
                self.probe_info.measured_vector = self.probe_info.unitary @ self.probe_info.get_probe_vector()
            else:
                print("GIVEN MATRIX NOT UNITARY!!!")

        self.vector.setText(self.vector_to_text(self.probe_info.measured_vector))

