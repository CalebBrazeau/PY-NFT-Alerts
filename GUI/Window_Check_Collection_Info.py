from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt6.QtCore import Qt
import sys

class WindowCheckCollectionInfo(QWidget):
    def __init__(self):
        super().__init__()
        self.MainUI()

    def MainUI(self):
        self.resize(300, 300)
        self.setWindowTitle("Check Collection Information")

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.label = QLabel("Select an Action")
        self.label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.label.setStyleSheet("font-size: 24px")
        layout.addWidget(self.label)