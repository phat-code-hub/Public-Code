def InputOneNumber():
    num_str=input('Number of 3 digits or more  : ').strip()
    if num_str.isnumeric:
        if len(num_str)>=3:
            if (isGapful(num_str)):
                print('true')
            else:
                print('false')
        else:
            print('Number must be at least 3 digits')
    else:
        print('Invalid Number')
def inputRange():
    down= int (input('Lower bound: '))
    up=int(input('Higher bound: '))
    for i in range(down,up+1):
        i_str=str(i)
        if isGapful(i_str):
            print(i)
def isGapful(n):
    number=int(n)
    sub_num=int(n[0]+n[-1])
    if number % sub_num == 0:
        return True
    else:
        return False
q=input('Yes[Y] for One number or No[N]} for print Gapful Range ').strip()
if q.upper() =='Y':
    InputOneNumber()
else:
    inputRange()
