from PyQt5 import QtWidgets, QtCore
from UI.layout import Ui_MainWindow
from Widgets.result_line_widget import Result
from Widgets.button_widget import Button


class Calculator(QtWidgets.QMainWindow, Ui_MainWindow):
    widget_button_click_event = QtCore.pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.result_widget = Result()
        self.init_result_widget()
        self.widget_button_click_event.connect(self.button_click_processing)
        self.mult_buttons()

    @staticmethod
    def button_click_processing(value):
        print(value)

        # init widget result

    def init_result_widget(self):
        self.result_layout.addWidget(self.result_widget)

    def set_result(self, value):
        self.result.setText(value)

    def get_result(self):
        return self.result.text()

        # init widget button

    def mult_buttons(self):
        print(eval("1+1"))
        row = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '+', '-', '*', '/', '=']
        count_column = 0
        count_row = 0
        for item in row:
            button = Button(item, self.widget_button_click_event)
            self.button_layout.addWidget(button, count_row, count_column)
            count_column += 1
            if count_column > 3:
                count_column = 0
                count_row += 1

