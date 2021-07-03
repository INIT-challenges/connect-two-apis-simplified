import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QFormLayout, QPushButton, QLabel
import requests
import json



class Window(QWidget):
    def refreshName(self):
        response_API = requests.get('https://randomuser.me/api/')
        data = response_API.text
        parse_json = json.loads(data)
        name = parse_json["results"][0]["name"]["title"] + " " + parse_json["results"][0]["name"]["first"] + " " + \
               parse_json["results"][0]["name"]["last"]
        self.nameLabel2.setText(name)

    def refreshPrompt(self):
        response_API = requests.get('https://binaryjazz.us/wp-json/genrenator/v1/story/1/')
        data = response_API.text
        parse_json = json.loads(data)
        self.promptLabel2.setText(parse_json)

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Random prompt generator")
        self.setGeometry(100, 100, 400, 100)
        self.move(400, 200)
        # Create a QFormLayout instance
        layout = QFormLayout()
        # Add widgets to the layout

        self.nameLabel1 = QLabel("Name:")
        self.nameLabel2 = QLabel("?")
        layout.addRow(self.nameLabel1, self.nameLabel2)

        self.promptLabel1 = QLabel("Prompt:")
        self.promptLabel2 = QLabel("?")
        layout.addRow(self.promptLabel1, self.promptLabel2)

        button = QPushButton('Get random character')
        button.setToolTip('Click for a random character')
        button.move(100, 70)
        button.clicked.connect(self.refreshName)
        layout.addRow(button)


        btn2 = QPushButton('Get random prompt')
        btn2.setToolTip('Click for a random prompt')
        btn2.move(100, 70)
        btn2.clicked.connect(self.refreshPrompt)
        layout.addRow(btn2)

        # Set the layout on the application's window
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())