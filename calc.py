import os
from PyQt6.QtWidgets import QMainWindow, QLabel, QLineEdit, QPushButton
from PyQt6 import uic
from operator import add, sub, mul, truediv


operations = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': truediv
}


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        ui_path = os.path.join(os.path.dirname(__file__), "design/calculator_design.ui")
        print(f"Loading UI from: {ui_path}")
        uic.loadUi(ui_path, self)
        self.setMinimumSize(300, 400)

        self.expression = ""

        # Find buttons
        self.zeroButton = self.findChild(QPushButton, 'zeroButton')
        self.oneButton = self.findChild(QPushButton, 'oneButton')
        self.twoButton = self.findChild(QPushButton, 'twoButton')
        self.threeButton = self.findChild(QPushButton, 'threeButton')
        self.fourButton = self.findChild(QPushButton, 'fourButton')
        self.fiveButton = self.findChild(QPushButton, 'fiveButton')
        self.sixButton = self.findChild(QPushButton, 'sixButton')
        self.sevenButton = self.findChild(QPushButton, 'sevenButton')
        self.eightButton = self.findChild(QPushButton, 'eightButton')
        self.nineButton = self.findChild(QPushButton, 'nineButton')

        self.decimalButton = self.findChild(QPushButton, 'decimalButton')
        self.plusButton = self.findChild(QPushButton, 'plusButton')
        self.minusButton = self.findChild(QPushButton, 'minusButton')
        self.multiplyButton = self.findChild(QPushButton, 'multiplyButton')
        self.divideButton = self.findChild(QPushButton, 'divideButton')
        self.equalButton = self.findChild(QPushButton, 'equalButton')
        self.clearButton = self.findChild(QPushButton, 'clearButton')
        self.delButton = self.findChild(QPushButton, 'delButton')
        self.percentButton = self.findChild(QPushButton, 'percentButton')
        self.plusMinusButton = self.findChild(QPushButton, 'plusMinusButton')

        self.outputLineEdit = self.findChild(QLineEdit, "outputLineEdit")

        # Connect buttons

        self.plusminusButton.clicked.connect(self.make_plus_minus)
        self.zeroButton.clicked.connect(lambda: self.add_to_expression('0'))
        self.oneButton.clicked.connect(lambda: self.add_to_expression('1'))
        self.twoButton.clicked.connect(lambda: self.add_to_expression('2'))
        self.threeButton.clicked.connect(lambda: self.add_to_expression('3'))
        self.fourButton.clicked.connect(lambda: self.add_to_expression('4'))
        self.fiveButton.clicked.connect(lambda: self.add_to_expression('5'))
        self.sixButton.clicked.connect(lambda: self.add_to_expression('6'))
        self.sevenButton.clicked.connect(lambda: self.add_to_expression('7'))
        self.eightButton.clicked.connect(lambda: self.add_to_expression('8'))
        self.nineButton.clicked.connect(lambda: self.add_to_expression('9'))

        self.decimalButton.clicked.connect(self.add_decimal)
        self.plusButton.clicked.connect(lambda: self.add_to_expression('+'))
        self.minusButton.clicked.connect(lambda: self.add_to_expression('-'))
        self.multiplyButton.clicked.connect(lambda: self.add_to_expression('*'))
        self.divideButton.clicked.connect(lambda: self.add_to_expression('/'))
        self.equalButton.clicked.connect(self.calculate)
        self.clearButton.clicked.connect(self.clear_expression)
        self.delButton.clicked.connect(self.remove_last_char)
        self.percentButton.clicked.connect(self.percentage)

    def add_to_expression(self, button):
        if self.outputLineEdit.text() == "0" or self.outputLineEdit.text() == '':
            if button not in operations.keys():
                self.expression = button
                self.outputLineEdit.setText(self.expression)
        else:
            if button in operations.keys():
                if self.expression and self.expression[-1] in operations.keys():
                    self.expression = self.expression[:-1] + button
                else:
                    self.expression += button
            else:
                self.expression += button

            self.outputLineEdit.setText(self.expression)

    def remove_last_char(self):
        self.expression = self.expression[:-1]
        self.outputLineEdit.setText(self.expression)

    def clear_expression(self):
        self.expression = ""
        self.outputLineEdit.setText("0")

    def calculate(self):
        try:

            result = str(round(eval(self.expression), 3))
            self.outputLineEdit.setText(result)
            self.expression = result
        except:
            self.outputLineEdit.setText("Error")
            self.expression = ""

    def add_decimal(self):
        text = self.outputLineEdit.text()
        last_number = text.split('+')[-1].split('-')[-1].split('*')[-1].split('/')[-1]

        if '.' not in last_number:
            self.add_to_expression('.')

    def make_plus_minus(self):
        if self.expression:
            if self.expression[0] == '-':
                self.expression = self.expression[1:]
            else:
                self.expression = '-' + self.expression

            self.outputLineEdit.setText(self.expression)

    def percentage(self):
        try:
            if self.expression:
                last_num = self.expression.split('+')[-1].split('-')[-1].split('*')[-1].split('/')[-1]
                if last_num:
                    percent_value = str(eval(last_num) / 100)
                    self.expression = self.expression[:-len(last_num)] + percent_value
                    self.outputLineEdit.setText(self.expression)
        except:
            self.outputLineEdit.setText("Error")
            self.expression = ""





