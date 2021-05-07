from PyQt5.QtWidgets import QWidget
from UI.button import Ui_Form


class Button(QWidget, Ui_Form):
    def __init__(self, name, callback):
        super().__init__()
        self.setupUi(self)
        self.name = name
        self.btn.setText(str(name))
        self.btn.clicked.connect(lambda: callback.emit(str(self.name)))

    # def set_button_number(self, value):
    #     self.btn.setText(value)
    #
    # def get_button_number(self):
    #     return self.btn.text()
