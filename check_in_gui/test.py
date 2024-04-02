# Importing PyQt 
from PyQt5.QtWidgets import QApplication, QWidget, QTextEdit, QVBoxLayout, QPushButton 
import sys 

    def scanID(self):
        #Calling a function when the lineEdit field is changed
        self.ui.lineEdit.textChanged.connect(self.getdatetime)
        self.ui.lineEdit.textChanged.connect(self.checkID)
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
        #self.ui.lineEdit.textChanged.connect(self.newID)
        #if self.ui.lineEdit.isModified():
        #    self.ui.lineEdit.setText(student_id)
        #else:
        #    self.ui.lineEdit.setText("")
        self.ui.lineEdit_2.text()
        self.ui.pushButton.clicked.connect(self.addID)
    
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

            # If the student ID is not in the file, display an error message
        #    self.ui.lineEdit_2.setText("Student not found")
        #    self.ui.lineEdit_3.setText("N/A")

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
        #create a dataframe using pandas to store the student ID and student name
        data = pd.DataFrame({'Student ID': [student_id], 'Student Name': [student_name]})
        #save the dataframe to a xlsx file
        data.to_excel('studentinfo.xlsx', index=False)
        