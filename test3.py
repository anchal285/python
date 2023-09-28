
import pandas as pd

# Read the Excel file into a DataFrame
df = pd.read_excel("C:/work/Assignment_Timecard.xls")

# Function to check if an employee has worked for more than 14 hours in a single shift
def has_long_shifts(employee_name):
    # Create a copy of the DataFrame to avoid SettingWithCopyWarning
    employee_df = df[df['Employee Name'] == employee_name].copy()
    employee_df['Time'] = pd.to_datetime(employee_df['Time'])
    
    # Convert 'Timecard Hours (as Time)' to numeric (assuming it contains hours as strings)
    employee_df.loc[:, 'Timecard Hours (as Time)'] = pd.to_numeric(employee_df['Timecard Hours (as Time)'], errors='coerce')
    
    if any(employee_df['Timecard Hours (as Time)'] > 14):
        return True
    else:
        return False

# Iterate over unique employee names and check for long shifts
for employee_name in df['Employee Name'].unique():
    position = df[df['Employee Name'] == employee_name].iloc[0]['Position ID']
    
    if has_long_shifts(employee_name):
        print(f"{employee_name} (Position: {position}): Worked more than 14 hours in a single shift")
    else:
        print(f"{employee_name} (Position: {position}): Did not work more than 14 hours in a single shift")
