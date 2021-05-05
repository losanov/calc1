# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'result_line.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from result_lineView import Ui_Form
import sys


class Result(QtWidgets.QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.is_equal = False

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
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
