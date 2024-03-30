import sys
from PyQt6.QtCore import QTimer
from PyQt6.QtWidgets import QApplication, QMainWindow
from ui.app_ui import Ui_MainWindow
import pandas as pd
from datetime import datetime

class APP(QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # Create a timer
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.scanID)
        self.timer.start(1000)  # Trigger the scanID function every 5 seconds
    
    def scanID(self):
        #Calling a function when the lineEdit field is changed
        self.ui.lineEdit.textChanged.connect(self.getdatetime)
        # Get the student ID from the lineEdit field and store it in a variable
        student_id = self.ui.lineEdit.text()

    def getdatetime(self):
        self.ui.lineEdit_3.setEnabled(True)
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        self.ui.lineEdit_3.setText(current_time)

    # Write a function to clear the lineEdit fields when scanning a new student ID
    def clearID(self):
        self.ui.lineEdit.clear()  

        # Read the data from the CSV file and check if the student ID is in the file
        #data = pd.read_csv('attendees.csv')
        #if student_id in data['Student ID'].values:
            # Get the student's name and checked-in date from the file
        #    student_name = data.loc[data['Student ID'] == student_id, 'Student Name'].values[0]
        #    checked_in_date = data.loc[data['Student ID'] == student_id, 'Checked-in Date'].values[0]
            # Display the student's name and checked-in date in the lineEdit fields
        #    self.ui.lineEdit_2.setText(student_name)
        #    self.ui.lineEdit_3.setText(checked_in_date)
        #else:
            # If the student ID is not in the file, display an error message
        #    self.ui.lineEdit_2.setText("Student not found")
        #    self.ui.lineEdit_3.setText("N/A")
        

    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = APP()
    main_window.show()
    sys.exit(app.exec())
