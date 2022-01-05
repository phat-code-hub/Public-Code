# This programe converts US Date format (MM/DD/YYYY, MMM DD,YYYY or MMMM DD,YYYY) into  
# EU Date Format (DD/MM/YYYY)
import re
#-------------------------------------------------
# Initial necessary data
reg=re.compile(r'(\d{1,2}|[a-zA-Z]{3,9})(/| ){1}\d{1,2}(/|,){1}( )*\d{4}')
regM=re.compile(r'^\d')
month_name1=['January','February','March','April','May','June','July','August','September','October','November','December']
month_name2=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
days_in_month=[30,28,31,30,31,30,31,31,30,31,30,31]

#-------------------------------------------------
#Change days in February if it is leap year
def checkYear(yearC):
    if yearC >0:
        if yearC % 4 == 0 and yearC % 100 != 0 or yearC % 400 == 0:
            days_in_month[1]=29
        else:
            days_in_month[1]=28
        return yearC
    else:
        return 0
#-------------------------------------------------
#Check month format
def checkMonth(monthL):
    m=regM.match(monthL)
    if m: # Month is numbers
        if int(monthL)>0 and int(monthL)<13:
            return int(monthL)
        else:
            return 0
    else: #Month is word
        monthC=monthL.capitalize()
        if monthC in month_name1:
            return month_name1.index(monthC)+1
        elif monthC in month_name2:
            return month_name2.index(monthC)+1
        else:
            return 0
#-------------------------------------------------
#Validate day
def checkDay(dayL,monthL):
    if (dayL>=1) and (dayL<=days_in_month[monthL-1]):
        return dayL
    else:
        return 0
#-------------------------------------------------
#print result
def printResult(d,m,y):
    if (d>0) and (m>0) and (y>0):
        print('{day}/{month}/{year}'.format(day=d,month=m,year=y))
    else:
        print('Invalid Date')
#-------------------------------------------------
#Repeat until input ok
while True:
    inputDate=input('Input Date (Ok for exit) :').strip()
    if inputDate.upper() == 'OK':
        print('See you again')
        break
    elif len(inputDate) > 0 :
        #Check the format (Month can be DD, MMM or MMMM)
        m=re.match(reg,inputDate)
        if m!= None:
            # Format MMMM DD , YYYY
            if inputDate.find(',') >= 0:
                date0=inputDate.split(',')
                year=checkYear(int(date0[1]))
                daymonth=date0[0].split(' ')
                month=checkMonth(daymonth[0].strip())
                day=checkDay(int(daymonth[1]),month)
                printResult(day,month,year)
            #Format MM/DD/YYYY
            elif inputDate.find('/') >= 0:
                date0=inputDate.split('/')
                year=checkYear(int(date0[2]))
                month=checkMonth(date0[0].strip()) 
                day=checkDay(int(date0[1]),month)
                printResult(day,month,year)
            else:
                print('Invalid Date!!')
        else:
            print('Invalid Date!!!')
    else:
        print('No Thing')