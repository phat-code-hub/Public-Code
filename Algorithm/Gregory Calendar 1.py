def IsleapYear(year):
    if year % 400 == 0 or (year % 4 ==0  and year % 100 !=0 ):
        return True
    else:
        return False
#--------------------------------------------------------------
def day_of_week(year,month):
    days_of_month =[0,31,28,31,30,31,30,31,31,30,31,30,31]
    if IsleapYear(year):
        days_of_month[2]=29
    day=1
    days=0
    for year in range(1,year):
        if IsleapYear(year):
            days += 366
        else:
            days +=365
    for m in range(1,month):
        days += days_of_month[m]
    days +=day
    return days % 7
#--------------------------------------------------------------
# Main Code:
if __name__ == '__main__':
    weekday_title=['Sun','Mon','Tue','Wed','Thu','Fri','Sat']
    weekday_names=['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
    year=int(input('Year: '))
    month=int(input('Month: '))
    print(weekday_names[day_of_week(year,month)])