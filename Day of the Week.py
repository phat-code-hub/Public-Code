from datetime import datetime
format_dt='%m/%d/%Y'
dt_str=input('Date: ').strip()
try:
    date=datetime.strptime(dt_str,format_dt)
    print(date.strftime('%A'))
except:
    print('Invalid Date')