import pandas as pd
data = pd.read_excel('test.xlsx')

new_info = pd.DataFrame({'Student ID': ['12345'], 'Student Name': ['John Doe']})
#print(data)
#data.loc[len(data)] = new_info
#data.to_excel('/Users/yenthee1301/Documents/GitHub/RFID_EMBEDDED/studentinfo.xlsx', index=False)
#print(new_info)
data = pd.concat([data, new_info], ignore_index=True)
print(data)