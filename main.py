from PyQt5 import QtWidgets
from layout import Ui_MainWindow
from button import Button
# from result_line import Ui_Form
import sys


class Calculator(QtWidgets.QMainWindow, Ui_MainWindow, Button):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.add_functions()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    calculator = Calculator()
    calculator.show()
    sys.exit(app.exec_())
