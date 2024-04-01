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
        self.ui.lineEdit.textChanged.connect(self.checkID)
        # Get the student ID from the lineEdit field and store it in a variable
        #student_id = self.ui.lineEdit.text()
        #self.ui.lineEdit.textChanged.connect(self.newID)
        #if self.ui.lineEdit.isModified():
        #    self.ui.lineEdit.setText(student_id)
        #else:
        #    self.ui.lineEdit.setText("")
        self.ui.lineEdit_2.text()
        self.ui.pushButton.clicked.connect(self.addID)
    
    #Function to check if the student ID is in the file
    def checkID(self):
        student_id = self.ui.lineEdit.text()
        data = pd.read_excel('studentinfo.xlsx')
        if student_id in data['Student ID'].values:
            student_name = data.loc[data['Student ID'] == student_id, 'Student Name'].values[0]
            self.ui.lineEdit_2.setText(student_name)
            self.ui.label_5.setText("Student found")
        else:
            self.ui.label_5.setText("Student not found")
            self.ui.pushButton.clicked.connect(self.addID)
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

    #Function to get the current time
    def getdatetime(self):
        self.ui.lineEdit_3.setEnabled(True)
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        self.ui.lineEdit_3.setText(current_time)

    #Read student ID from the lineEdit field and create a dataframe using pandas
    def addID(self):
        student_id = self.ui.lineEdit.text()
        student_name = self.ui.lineEdit_2.text()
        timecheckin = self.ui.lineEdit_3.text()

    # create a dataframe for the new data
        new_data = pd.DataFrame({'Student ID': [student_id], 'Student Name': [student_name]})
        attendance = pd.DataFrame({'Student ID': [student_id], 'Student Name': [student_name], 'Checked-in Date': [timecheckin]})
    # try to read the existing data
        try:
            data = pd.read_excel('studentinfo.xlsx')
        # append the new data
            data = data.append(new_data, ignore_index=True)
        except FileNotFoundError:
        # if the file does not exist, use the new data as the data
            data = new_data

    # save the dataframe to a xlsx file
            data.to_excel('studentinfo.xlsx', index=False)
        


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = APP()
    main_window.show()
    sys.exit(app.exec())
