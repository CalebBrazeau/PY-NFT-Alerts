from PyQt6.QtWidgets import QWidget, QLabel, QPushButton, QTextEdit, QGridLayout
from PyQt6.QtCore import Qt

class WindowCheckLaunchpad(QWidget):
    def __init__(self):
        super().__init__()
        self.MainUI()

    def MainUI(self):
        self.resize(300, 300)
        self.setWindowTitle('Check Launchpad')

        layout = QGridLayout()
        self.setLayout(layout)

        self.label = QLabel('Checking Launchpad...')
        self.label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.label.setStyleSheet('font-size: 24px')
        layout.addWidget(self.label, 0, 2)

        self.contentBox = QTextEdit()
        self.contentBox.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.contentBox.setStyleSheet('color: "#FFFFFF"')
        self.contentBox.setReadOnly(True)
        self.contentBox.append('Hello, Beautiful')
        layout.addWidget(self.contentBox, 2, 2)

        self.submitButton = QPushButton('Check Launchpad')
        layout.addWidget(self.submitButton, 3, 2)