import pandas as pd

df = pd.read_excel("C:\\work\\Assignment_Timecard.xls")

def has_worked_7_consecutive_days(employee_name):
    employee_df = df[df['Employee Name'] == employee_name].copy()
    employee_df['Time'] = pd.to_datetime(employee_df['Time'])
    employee_df = employee_df.sort_values(by='Time')
    
    consecutive_days = 0
    prev_date = None
    
    for date in employee_df['Time']:
        if prev_date is None:
            prev_date = date
            consecutive_days = 1
        elif (date - prev_date).days == 1:
            consecutive_days += 1
            if consecutive_days == 7:
                return True
        else:
            consecutive_days = 1
        prev_date = date
    
    return False

for employee_name in df['Employee Name'].unique():
    if has_worked_7_consecutive_days(employee_name):
        position = df[df['Employee Name'] == employee_name].iloc[0]['Position ID']
        print(f"{employee_name} (Position: {position}): Worked 7 consecutive days")
    else:
        print(f"{employee_name}: Did not work 7 consecutive days")
