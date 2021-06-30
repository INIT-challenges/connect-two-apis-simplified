import sys

import requests
import json
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QFormLayout, QPushButton



def on_click():
    print("helllo")

app = QApplication(sys.argv)

# make new QWidget window
window = QWidget()
window.setGeometry(100, 100, 400, 100)
window.move(400, 200)
window.setWindowTitle('two-factor login')

# create the form layout
layout = QFormLayout()

nameLine = QLineEdit()
layout.addRow('Name:', nameLine)

pwField = QLineEdit()
pwField.setEchoMode(QLineEdit.Password)
layout.addRow('Password:', pwField)

recipientEmailLine = QLineEdit()
layout.addRow('Email:', recipientEmailLine)

button = QPushButton('Generate OTP')
button.setToolTip('Click to generate otp')
button.move(100, 70)
button.clicked.connect(on_click)

layout.addRow(button)

# apply the created layout to thw QWidget
window.setLayout(layout)

# show the first window
window.show()

# close the program
sys.exit(app.exec_())