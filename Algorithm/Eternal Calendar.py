day_of_week_name = ('S M T W T F S',
                    '日 月 火 水 木 金 土',
                    'CN T2 T3 T4 T5 T6 T7')
year_name = ('Year', '年', 'Năm')
month_name = ('Month', '月', 'Tháng')
days_board = '''
                   1  2  3  4  5  6  7 

 2  3  4  5  6  7  8  9 10 11 12 13 14 

 9 10 11 12 13 14 15 16 17 18 19 20 21   

16 17 18 19 20 21 22 23 24 25 26 27 28   

23 24 25 26 27 28 29 30 31  

30 31 

             '''
try:
    lang = int(input('Select Language: 1-ENG ,2-JPN,3-VN -> '))
    curYear = year_name[lang - 1]
    curMonth = month_name[lang - 1]
    year = int(input(curYear + ' = '))
    month = int(input(curMonth + ' = '))
    # 1月と2月は前年の13月と14月にする
    if month == 1 or month == 2:
        year -= 1
        month += 12
    day = 1
    days = 31 + 28 + 365 * (year - 1) + year // 4 - year // 100 + year // 400 + (306 * (month + 1) // 10) - 122 + day
    day_of_week = days % 7
    print(' ' * 3 * (6 - day_of_week - 1) + day_of_week_name[lang - 1])
    print(days_board)
except:
    print('Illegal')
