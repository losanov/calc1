from PyQt5 import QtWidgets
import sys
from View.main_view import Calculator

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    calculator = Calculator()

    calculator.show()
    sys.exit(app.exec_())
