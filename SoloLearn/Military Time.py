import datetime
PM=tuple(t for t in range(0,25))
timeStr=input('Date :').strip()
time_origin=timeStr.split()
signal =time_origin[1].upper()
time0=time_origin[0].split(':')
hour=int(time0[0])
minute=int(time0[1])
if signal=='AM':
    hour=PM[hour]
elif signal=='PM':
    hour =PM[hour+12]
else:
    pass
military_time=datetime.time(hour,minute)
print('{0:02d}:{1:02d}'.format(military_time.hour,military_time.minute))