def leapYear(year):
    if year % 400 == 0 or (year % 4 ==0  and year % 100 !=0 ):
        return True
    else:
        return False
#--------------------------------------------------------------
# Main Code:
if __name__ == '__main__':
    days=0
    for year in range(1,2020):
        if leapYear(year):
            days += 366
        else:
            days +=365
    print(days)
    print(days % 7)  