from math import factorial as fact
def Analyse(n):
    
    pass
try:
    num=int(input('Number: '))
    assert num>=0
    result,zero_num=Analyse(num)
    print('{0}! has {1} trailing zeros at the end'.format(num,zero_num))
except:
    print('Number is not positive integer!')

