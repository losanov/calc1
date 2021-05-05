import button as button
from PyQt5 import QtWidgets
# from calc import Ui_MainWindow
from buttonView import Ui_Form
import sys

btn_name = [1, 2, 3, 4, 5, 6, 7, 8, 9, '+', '-', '*', '/', '=']


class Button(QtWidgets.QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.add_functions()

    def add_functions(self):
        for item in btn_name:
            self.btn.setText = item
            if item == '+':
                self.btn.setObjectNam = 'btn_sum'
            elif item == '-':
                self.btn.setObjectNam = 'btn_sub'
            elif item == '*':
                self.btn.setObjectNam = 'btn_mult'
            elif item == '/':
                self.btn.setObjectNam = 'btn_div'
            elif item == '=':
                self.btn.setObjectNam = 'btn_equal'
            else:
                self.btn.setObjectNam = f'btn_{item}'
            self.btn.clicked.connect(lambda: self.write_number(self.btn.text()))

        self.btn_equal.clicked.connect(self.results)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    btn = Button()
    btn.show()
    sys.exit(app.exec_())
