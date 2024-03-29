import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from ui.app_ui import Ui_MainWindow
import pandas as pd
from datetime import datetime

class APP(QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
    
    def getdata(self):
        #Get RFID ID from keyboard
        ID = self.ui.textEdit.toPlainText()
        


        #Get checked-in time
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        self.ui.textEdit_3.setPlainText(str(current_time))
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = APP()
    main_window.show()
    sys.exit(app.exec())
