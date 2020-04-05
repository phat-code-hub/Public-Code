import math
num=input('So: ').strip()
try:
    number=float(num)
    square=str(round(number**2,3))
    root=str(round(math.sqrt(number),3))
    chk_list=[n for n in square if n !='.' and n !='0']
    chk=[n in root for n in chk_list]
    if  any(chk):
        print('true')
    else:
        print('false')
except:
    print('Invalid Number')