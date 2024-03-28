import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from ui.app_ui import Ui_MainWindow

class APP(QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
    
    def getdata(self):
        result = self.textEdit.toPlainText()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = APP()
    main_window.show()
    sys.exit(app.exec())
