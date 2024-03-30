# Importing PyQt 
from PyQt5.QtWidgets import QApplication, QWidget, QTextEdit, QVBoxLayout, QPushButton 
import sys 

class TextEditDemo(QWidget): 
	def __init__(self, parent=None): 
		super().__init__(parent) 
		
		# Setting the title of the GUI 
		self.setWindowTitle("QTextEdit") 
		
		# Setting the size of the window 
		self.resize(300, 270) 
		
		# Creating the first textedit 
		self.textEdit1 = QTextEdit() 
		
		# Creating the second textedit 
		self.textEdit2 = QTextEdit() 
		
		# Creating the button 
		self.btnPress1 = QPushButton("Button 1") 
		
		# Creating a vertical box layout 
		layout = QVBoxLayout() 
		
		# Adding the first textedit into the layout 
		layout.addWidget(self.textEdit1) 
		
		# Adding the second textedit into the layout 
		layout.addWidget(self.textEdit2) 
		
		# Adding the button into the layout 
		layout.addWidget(self.btnPress1) 

		self.setLayout(layout) 

		# Calling the function when the button is clicked 
		self.btnPress1.clicked.connect(self.btnPress1_Clicked) 

	def btnPress1_Clicked(self): 
		''' 
		This function reads the data from the first TextEdit and 
		add 10 to it. After adding the number, it displays the result 
		in the second TextEdid. 
		'''
		result = int(self.textEdit1.toPlainText()) + 10
		
		# Displaying the result in the second textEdit. 
		self.textEdit2.setPlainText(str(result)) 


if __name__ == '__main__': 
	''' 
	Main code that creates the GUI 
	'''
	app = QApplication(sys.argv) 
	win = TextEditDemo() 
	win.show() 
	sys.exit(app.exec_()) 