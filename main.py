import sys
from math import sin, cos, tan, sqrt, radians, log10, pi, e, log
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QGridLayout, QPushButton, QLineEdit, QLabel
from PyQt6.QtCore import Qt

class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.setFixedSize(400, 400)

        # Create display label
        self.display = QLineEdit()
        self.display.setFixedHeight(50)
        self.display.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.display.setReadOnly(True)

        # Create buttons
        buttons = [
            ["C", "(", ")", "sin", "7", "8", "9", "+"],
            ["1/x", "x^2", "sqrt", "cos", "4", "5", "6", "-"],
            ["log10", "e", "pi", "tan", "1", "2", "3", "*"],
            [ "0", ".", "=", "/"],
            ["ln","deg/rad"]
        ]

        # Create button grid layout
        layout = QGridLayout()

        for row, button_row in enumerate(buttons):
            for col, button_text in enumerate(button_row):
                button = QPushButton(button_text)
                button.setFixedSize(50, 50)
                layout.addWidget(button, row, col)
                button.clicked.connect(self.button_clicked)

        # Create main widget and layout
        widget = QWidget()
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.display)
        main_layout.addLayout(layout)
        widget.setLayout(main_layout)
        self.setCentralWidget(widget)

        # Set radians as the default mode
        self.is_radians = True

        # Create mode label
        self.mode_label = QLabel("Radians")
        self.statusBar().addWidget(self.mode_label)

    def button_clicked(self):
        button = self.sender()
        button_text = button.text()

        if button_text == "C":
            self.display.clear()
        elif button_text == "=":
            try:
                expression = self.display.text()
                result = eval(expression)
                self.display.setText(str(result))
            except:
                self.display.setText("Error")
        elif button_text == "deg/rad":
            self.is_radians = not self.is_radians
            mode = "Radians" if self.is_radians else "Degrees"
            self.mode_label.setText(mode)
        elif button_text == "sin" or button_text == "cos" or button_text == "tan":
            if self.display.text():
                angle = float(self.display.text())
                if not self.is_radians:
                    angle = radians(angle)
                if button_text == "sin":
                    result = sin(angle)
                elif button_text == "cos":
                    result = cos(angle)
                elif button_text == "tan":
                    result = tan(angle)
                self.display.setText(str(result))
            else:
                self.display.setText("Error: No number selected")
        elif button_text == "log10":
            if self.display.text():
                number = float(self.display.text())
                if number <= 0:
                    self.display.setText("Error: Invalid input")
                else:
                    result = log10(number)
                    self.display.setText(str(result))
            else:
                self.display.setText("Error: No number selected")
        elif button_text == "sqrt":
            if self.display.text():
                number = float(self.display.text())
                if number < 0:
                    self.display.setText("Error: Invalid input")
                else:
                    result = sqrt(number)
                    self.display.setText(str(result))
            else:
                self.display.setText("Error: No number selected")
        elif button_text == "pi":
            self.display.setText(str(pi))
        elif button_text == "e":
            self.display.setText(str(e))
        elif button_text == "1/x":
            if self.display.text():
                number = float(self.display.text())
                if number != 0:
                    result = 1 / number
                    self.display.setText(str(result))
                else:
                    self.display.setText("Error: Division by zero")
            else:
                self.display.setText("Error: No number selected")
        elif button_text == "x^2":
            if self.display.text():
                number = float(self.display.text())
                result = number ** 2
                self.display.setText(str(result))
            else:
                self.display.setText("Error: No number selected")
        elif button_text == "ln":
            if self.display.text():
                number = float(self.display.text())
                if number <= 0:
                    self.display.setText("Error: Invalid input")
                else:
                    result = log(number)
                    self.display.setText(str(result))
            else:
                self.display.setText("Error: No number selected")
        else:
            self.display.setText(self.display.text() + button_text)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    calculator = Calculator()
    calculator.show()
    sys.exit(app.exec())

