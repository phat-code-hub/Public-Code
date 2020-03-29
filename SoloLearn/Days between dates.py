import traceback
import datetime as tg
from datetime import date
date_format='%B %d, %Y'
try:
    dt1=input('ngay1:').strip()
    dt2=input('Ngay 2: ').strip()
    date1=tg.datetime.strptime(dt1,date_format)
    date2=tg.datetime.strptime(dt2,date_format)
    delta=date1-date2
    print(abs(delta.days))
except:
    print(traceback.print_exc())