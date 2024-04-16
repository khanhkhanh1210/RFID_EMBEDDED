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
        self.timer.start(3000)  # Trigger the scanID function every 3 seconds
        self.ui.pushButton_2.clicked.connect(self.clear)
        self.ui.pushButton.clicked.connect(self.addID)
        self.ui.lineEdit_3.textChanged.connect(self.addattendee)
        
    
    def scanID(self):
        #Calling a function when the ID input field (lineEdit) is changed
        self.ui.lineEdit.text()
        self.ui.lineEdit.textChanged.connect(self.getdatetime)
        self.ui.lineEdit.textChanged.connect(self.checkID)
        
        # Get the student ID from the lineEdit field and store it in a variable
        #self.ui.lineEdit.textChanged.connect(self.newID)
        #if self.ui.lineEdit.isModified():
        #    self.ui.lineEdit.setText(student_id)
        #else:
        #    self.ui.lineEdit.setText("")
        #self.ui.lineEdit_2.text()

    def getdatetime(self):
        now = datetime.now()
        current_time = now.strftime("%d-%m-%Y %H:%M:%S")
        self.ui.lineEdit_3.setText(current_time)
    
    #Function to check if the student ID is in the file
    def checkID(self):
        student_id = self.ui.lineEdit.text()
        #QTimer.singleShot(3000, self.ui.lineEdit.clear)
        data = pd.read_excel('/Users/yenthee1301/Documents/GitHub/RFID_EMBEDDED/studentinfo.xlsx', dtype={'Student ID': str})
    
        # Find student_id in studentinfo.xlsx file 
        student_info = (data.loc[:, 'Student ID'] == student_id).any
        if student_info:
            matching_rows = data.loc[data['Student ID'] == student_id, 'Student Name']
            if matching_rows.size > 0:
                student_name = matching_rows.values[0]
                self.ui.lineEdit_2.setText(student_name)
                self.ui.label_5.setText("Student found")
                #self.ui.lineEdit_2.textChanged.connect(self.addattendee)
            else:
                self.ui.label_5.setText("Student not found")
                
            #student_name = data.loc[data['Student ID'] == student_id, 'Student Name'].values[0]
            #self.ui.lineEdit_2.setText(student_name)
            #self.ui.label_5.setText("Student found")
        #else:
            #self.ui.label_5.setText("Student not found")
            

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


    #Read student ID from the lineEdit field and create a dataframe using pandas
    def addID(self):
        student_id = self.ui.lineEdit.text()
        student_name = self.ui.lineEdit_2.text()
        #timecheckin = self.ui.lineEdit_3.text()
        
    # create a dataframe for the new data
        new_info = pd.DataFrame({'Student ID': [student_id], 'Student Name': [student_name]})
        info = pd.read_excel('/Users/yenthee1301/Documents/GitHub/RFID_EMBEDDED/studentinfo.xlsx', dtype={'Student ID': str})
        # append the new data
        info = pd.concat([info, new_info], ignore_index=True)
        info.to_excel('/Users/yenthee1301/Documents/GitHub/RFID_EMBEDDED/studentinfo.xlsx', index=False)
        #self.ui.lineEdit_2.textChanged.connect(self.addattendee)


    def addattendee(self):
        student_id = self.ui.lineEdit.text()
        student_name = self.ui.lineEdit_2.text()
        timecheckin = self.ui.lineEdit_3.text()
        new_attendance = pd.DataFrame({'Student ID': [student_id], 'Student Name': [student_name], 'Checked-in Date': [timecheckin]})
        attend = pd.read_excel('/Users/yenthee1301/Documents/GitHub/RFID_EMBEDDED/attendees.xlsx', dtype={'Student ID': str})
        # append the new data
        attend = pd.concat([attend, new_attendance], ignore_index=True)
        # if the file does not exist, use the new data as the data
        attend.to_excel('/Users/yenthee1301/Documents/GitHub/RFID_EMBEDDED/attendees.xlsx', index=False)
        
    
    def clear(self):
        self.ui.lineEdit.clear()
        self.ui.lineEdit_2.clear()
        self.ui.lineEdit_3.clear()  
        self.ui.lineEdit.setFocus()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = APP()
    main_window.show()
    sys.exit(app.exec())
