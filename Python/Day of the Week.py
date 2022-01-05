import re
from datetime import datetime
reg=re.compile(r'^(\D)+')
format_dt1='%m/%d/%Y'
format_dt2='%B %d, %Y'
try:
    dt_str=input('Date: ').strip()
    m=reg.match(dt_str)
    if m:
        format_dt=format_dt2
    else:
        format_dt=format_dt1
    date=datetime.strptime(dt_str,format_dt)
    print(date.strftime('%A'))
except:
    print('Invalid Date')