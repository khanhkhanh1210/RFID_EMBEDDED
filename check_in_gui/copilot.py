import pandas as pd

# Create a DataFrame
df = pd.read_excel('/Users/yenthee1301/Documents/GitHub/RFID_EMBEDDED/studentinfo.xlsx')
# Access the student name of the student with index 0
# Access the 'Student ID' column
student_id = 2151034
student_check = df.loc[:, 'Student ID'] == student_id

print(student_check)