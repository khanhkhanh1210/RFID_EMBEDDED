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
        # Create a timerm      
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.scanID)
        self.timer.start(3000)  # Trigger the scanID function every 3 seconds
        #self.ui.pushButton_2.clicked.connect(self.clear)
        self.ui.pushButton.clicked.connect(self.addID)
        self.ui.lineEdit.textChanged.connect(self.getdatetime)
        #self.ui.pushButton_2.clicked.connect(self.addattendee)
        self.ui.pushButton_2.clicked.connect(self.clear_and_addattendee)
        
    
    def scanID(self):
        #Calling a function when the ID input field (lineEdit) is changed
        #self.ui.lineEdit.text()
        self.ui.lineEdit.textChanged.connect(self.checkID)
        
    def getdatetime(self):
        now = datetime.now()
        current_time = now.strftime("%d-%m-%Y %H:%M:%S")
        self.ui.lineEdit_3.setText(current_time)
    
    #Function to check if the student ID is in the file
    def checkID(self):
        student_id = self.ui.lineEdit.text()
        #QTimer.singleShot(3000, self.ui.lineEdit.clear)
        data = pd.read_excel('/Users/yenthee1301/Documents/GitHub/RFID_EMBEDDED/check_in_gui/studentinfo.xlsx', dtype={'Student ID': str})
    
        # Find student_id in studentinfo.xlsx file 
        student_info = (data.loc[:, 'Student ID'] == student_id).any
        if student_info:
            matching_rows = data.loc[data['Student ID'] == student_id, 'Student Name']
            if matching_rows.size > 0:
                student_name = matching_rows.values[0]
                self.ui.lineEdit_2.setText(student_name)
                self.ui.label_5.setText("Student found")
            else:
                self.ui.label_5.setText("Student not found")
                

    #Read student ID from the lineEdit field and create a dataframe using pandas
    def addID(self):
        student_id = self.ui.lineEdit.text()
        student_name = self.ui.lineEdit_2.text()
        #timecheckin = self.ui.lineEdit_3.text()
        
    # create a dataframe for the new data
        new_info = pd.DataFrame({'Student ID': [student_id], 'Student Name': [student_name]})
        info = pd.read_excel('/Users/yenthee1301/Documents/GitHub/RFID_EMBEDDED/check_in_gui/studentinfo.xlsx', dtype={'Student ID': str})
        # append the new data
        info = pd.concat([info, new_info], ignore_index=True)
        info.to_excel('/Users/yenthee1301/Documents/GitHub/RFID_EMBEDDED/check_in_gui/studentinfo.xlsx', index=False)

    def clear_and_addattendee(self):
        student_id = self.ui.lineEdit.text()
        student_name = self.ui.lineEdit_2.text()
        self.clear()
        self.addattendee(student_id, student_name)

    def addattendee(self, student_id, student_name):
        #student_id = self.ui.lineEdit.text()
        #student_name = self.ui.lineEdit_2.text()
        #self.ui.lineEdit.setText(student_id)
        #self.ui.lineEdit_2.setText(student_name)
        timecheckin = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        new_attendance = pd.DataFrame({'Student ID': [student_id], 'Student Name': [student_name], 'Checked-in Date': [timecheckin]})
        attend = pd.read_excel('/Users/yenthee1301/Documents/GitHub/RFID_EMBEDDED/check_in_gui/attendees.xlsx', dtype={'Student ID': str})
        # append the new data
        attend = pd.concat([attend, new_attendance], ignore_index=True)
        # if the file does not exist, use the new data as the data
        attend.to_excel('/Users/yenthee1301/Documents/GitHub/RFID_EMBEDDED/check_in_gui/attendees.xlsx', index=False)
        
    
    def clear(self):
        self.ui.lineEdit.clear()
        self.ui.lineEdit_2.clear()
        self.ui.lineEdit_3.clear()  
        self.ui.lineEdit.setFocus()
        self.ui.label_5.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = APP()
    main_window.show()
    sys.exit(app.exec())