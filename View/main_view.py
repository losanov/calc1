from PyQt5 import QtWidgets, QtCore
from UI.layout import Ui_MainWindow
from Widgets.result_line_widget import Result
from Widgets.button_widget import Button
import random
from View.button_row import Button_row


class Calculator(QtWidgets.QMainWindow, Ui_MainWindow, Button_row):
    widget_button_click_event = QtCore.pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.cng_clicked = Button_row().cng_clicked
        self.row = Button_row().row
        self.result_widget = Result()
        self.init_result_widget()
        self.widget_button_click_event.connect(self.button_click_processing)
        self.mult_buttons()

    def button_click_processing(self, value):
        if value == 'CHG':
            self.cng_clicked = True
        elif value == '=':
            self.result_widget.set_result(eval(self.get_result()))
        else:
            self.add_number(value)
        self.mult_buttons()
        self.cng_clicked = False

    # init widget result

    def init_result_widget(self):
        self.result_layout.addWidget(self.result_widget)

    def add_number(self, number):
        self.result_widget.set_result(self.result_widget.get_result() + number)

    def set_result(self, value):
        self.result.setText(value)

    def get_result(self):
        return self.result_widget.get_result()

    # init widget button

    def mult_buttons(self):
        if self.cng_clicked:
            random.shuffle(self.row)
        count_column = 0
        count_row = 0
        for item in self.row:
            button = Button(item, self.widget_button_click_event)
            self.button_layout.addWidget(button, count_row, count_column)
            count_column += 1
            if count_column > 3:
                count_column = 0
                count_row += 1
