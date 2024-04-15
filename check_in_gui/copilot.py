import pandas as pd
from datetime import datetime

# Create a DataFrame
df = pd.read_excel('/Users/yenthee1301/Documents/GitHub/RFID_EMBEDDED/studentinfo.xlsx', dtype={'Student ID': str})
# Access the student name of the student with index 0
# Access the 'Student ID' column
student_id = '2151034'
student_check = (df.loc[:, 'Student ID'] == student_id).any
if student_check:
    student_name = df.loc[df['Student ID'] == student_id, 'Student Name'].values[0]
    print(student_name)
else:
    print("Student not found")

now = datetime.now()
timecheckin = now.strftime("%d/%m/%Y %H:%M:%S")
new_attendance = pd.DataFrame({'Student ID': [student_id], 'Student Name': [student_name], 'Checked-in Date': [timecheckin]})
print(new_attendance)
attend = pd.read_excel('/Users/yenthee1301/Documents/GitHub/RFID_EMBEDDED/attendees.xlsx', dtype={'Student ID': str})
attend = pd.concat([attend, new_attendance], ignore_index=True)
print(attend)
attend.to_excel('/Users/yenthee1301/Documents/GitHub/RFID_EMBEDDED/attendees.xlsx', index=False)
