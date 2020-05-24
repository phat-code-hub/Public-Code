weekday_title=['Sun','Mon','Tue','Wed','Thu','Fri','Sat']
weekday_names=['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
days_of_month =[0,31,28,31,30,31,30,31,31,30,31,30,31]
def IsleapYear(year):
    if year % 400 == 0 or (year % 4 ==0  and year % 100 !=0 ):
        return True
    else:
        return False
#--------------------------------------------------------------
def day_of_week(year,month):
    if IsleapYear(year):
        days_of_month[2]=29
    day=1
    days=31+28+365*(year-1) + year//4 -year//100+year//400+ (306*(month+1)//10)-122 +day
    return days % 7
#--------------------------------------------------------------
def show(year,month,dayOrd):
    rows=[]
    day=7-dayOrd
    dNum=days_of_month[month]
    row=(dNum-day) //7
    left=row*7-day 
    print (f'{month}/{year} calendar:')
    print(' '.join(weekday_title))
    firstRow=[]
    blank=' '*4*(dayOrd)
    if day>0:
        firstRow=[str(i).rjust(3) for i in range(1,day+1)]
        firstRow.insert(0,blank)
        firstRow[0].rjust(3)
    print(''.join(firstRow))
#--------------------------------------------------------------
# Main Code:
if __name__ == '__main__':
    year=int(input('Year: '))
    month=int(input('Month: '))
    show(year,month,day_of_week(year,month))