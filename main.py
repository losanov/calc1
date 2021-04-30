from PyQt5 import QtWidgets
from calc import Ui_MainWindow
import sys


class Calculator(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.add_functions()
        self.is_equal = False

    def add_functions(self):
        self.btn_0.clicked.connect(lambda: self.write_number(self.btn_0.text()))
        self.btn_1.clicked.connect(lambda: self.write_number(self.btn_1.text()))
        self.btn_2.clicked.connect(lambda: self.write_number(self.btn_2.text()))
        self.btn_3.clicked.connect(lambda: self.write_number(self.btn_3.text()))
        self.btn_4.clicked.connect(lambda: self.write_number(self.btn_4.text()))
        self.btn_5.clicked.connect(lambda: self.write_number(self.btn_5.text()))
        self.btn_6.clicked.connect(lambda: self.write_number(self.btn_6.text()))
        self.btn_7.clicked.connect(lambda: self.write_number(self.btn_7.text()))
        self.btn_8.clicked.connect(lambda: self.write_number(self.btn_8.text()))
        self.btn_9.clicked.connect(lambda: self.write_number(self.btn_9.text()))
        self.btn_plus.clicked.connect(lambda: self.write_number(self.btn_plus.text()))
        self.btn_minus.clicked.connect(lambda: self.write_number(self.btn_minus.text()))
        self.btn_mult.clicked.connect(lambda: self.write_number(self.btn_mult.text()))
        self.btn_div.clicked.connect(lambda: self.write_number(self.btn_div.text()))

        self.btn_equal.clicked.connect(self.results)

    def write_number(self, number):
        if self.result.text() == '0' or self.is_equal:
            self.result.setText(number)
            self.is_equal = False
        else:
            self.result.setText(self.result.text() + number)

    def results(self):
        res = eval(self.result.text())
        self.result.setText(f'Result: {res}')
        self.is_equal = True


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    calculator = Calculator()
    calculator()
    sys.exit(app.exec_())
