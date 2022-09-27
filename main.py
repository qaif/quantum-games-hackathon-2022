import sys

from PyQt6.QtGui import QColor, QPainter, QFont
from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QHBoxLayout
from PyQt6.QtCore import Qt, QRect

from grid import Grid, GridWidget
from quantum_circuit import QuantumCircuit


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        mw = QWidget()
        layout = QHBoxLayout()
        mw.setLayout(layout)
        self.setCentralWidget(mw)

        grid = Grid(10, 50)
        grid_widget = GridWidget(grid)

        block_widget = QuantumCircuit(100, 100)

        self.setGeometry(0, 0, grid.width + grid.width, grid.height)
        self.setWindowTitle('Quantum Snake')

        layout.addWidget(grid_widget)
        layout.addWidget(block_widget)


# app = QtWidgets.QApplication(sys.argv)
# # window = MainWindow()
# window = MainWidget()
# window.show()
# app.exec()

def main():

    app = QApplication(sys.argv)
    # grid = GridWidget(Grid(10, 50))
    window = Window()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()