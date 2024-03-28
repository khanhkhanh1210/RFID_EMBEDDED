import sys
import PyQt6.QtCore
from PyQt6.QtCore import QTimer
from PyQt6.QtGui import *
from PyQt6.QtWidgets import QApplication, QMainWindow, QTextEdit, QPushButton, QLabel, QVBoxLayout

class APP(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupGUI()
    
    def setupGUI(self):
        self.resize(521, 297)
        self.setWindowTitle("PROMPT")
        layout = QVBoxLayout()
        self.label_2 = QLabel("Student's name")
        layout.addWidget(self.label_2)
        self.label_3 = QLabel("Checked-in date")
        layout.addWidget(self.label_3)
        self.label_4 = QLabel("Class Check-in Wizard")
        layout.addWidget(self.label_4)

        self.setLayout(layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainwindow = APP()
    mainwindow.show() 
    app.exec()
