from PyQt5 import QtWidgets
from calc import Ui_MainWindow
from layout import Ui_MainWindow
import sys


class Calculator(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.is_equal = False


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    calculator = Calculator()
    calculator.show()
    sys.exit(app.exec_())
