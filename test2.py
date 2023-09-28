import pandas as pd

# Read the Excel file into a DataFrame
df = pd.read_excel("C:/work/Assignment_Timecard.xls")

# Function to check if an employee has short breaks between shifts
def has_short_breaks(employee_name):
    employee_df = df[df['Employee Name'] == employee_name].copy()
    employee_df['Time'] = pd.to_datetime(employee_df['Time'])
    employee_df = employee_df.sort_values(by='Time')
    
    for i in range(1, len(employee_df)):
        time_diff = (employee_df.iloc[i]['Time'] - employee_df.iloc[i - 1]['Time']).total_seconds() / 3600
        if 1 < time_diff < 10:
            return True
    
    return False



# Iterate through unique employee names and print those with short breaks between shifts
for employee_name in df['Employee Name'].unique():
    if has_short_breaks(employee_name):
        position = df[df['Employee Name'] == employee_name].iloc[0]['Position ID']
        print(f"{employee_name} (Position: {position}): Has short breaks between shifts")
