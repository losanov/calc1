# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QWidget
from UI.result_line import Ui_Form


class Result(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def set_result(self, value):
        self.result.setText(str(value))

    def get_result(self):
        return self.result.text()

    def add_number(self, value):
        self.result.setText(self.result.text() + str(value))
