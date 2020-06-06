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
    return (days % 7)
#--------------------------------------------------------------
def show(year,month,dayOrd):
    print(dayOrd)
    print (f'{month}/{year} Calendar:')
    Lich=[w.rjust(3) for w in weekday_title]
    print(' '.join(Lich))
    dNum=list(str(d) for d in range(1,days_of_month[month]+1))
    for n in range(dayOrd):
        dNum.insert(0,' ')
    line,left=divmod(len(dNum),7)
    if left>0:
        for l in range(7-left):
            dNum.insert(len(dNum),' ')
        line +=1
    lNum=[]
    for l in range(line):
        temp=[]
        for n in range(7):
            temp.append(dNum[l*7+n].rjust(3))
        lNum.append(temp)
    for i in range(line):
        print(' '.join(lNum[i]))
    print(weekday_names[dayOrd])
#--------------------------------------------------------------
# Main Code:
if __name__ == '__main__':
    year=int(input('Year: '))
    month=int(input('Month: '))
    show(year,month,day_of_week(year,month))