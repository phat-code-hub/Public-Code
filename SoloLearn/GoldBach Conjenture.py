import math
from sympy import sieve
def OneNumber(n):
    n1=[]
    n2=[]
    prime_list=[x for x in sieve.primerange(1,n)]
    for i in prime_list:
        if (n-i) in prime_list:
            n1.append(i)
            n2.append(n-i)
    if len(n1) % 2 ==0:
        limit=len(n1)//2
    else:
        limit=len(n1)//2+1
    return n1[:limit],n2[:limit]
def RangeNumber(n1,n2):
    for i in range(n1,n2,2):
        pass
def Show(NumStr,n1,n2,isRange=False):
    if isRange:
        pass
    else:
        for i in range(len(n1)):
            print('{0} + {1}'.format(n1[i],n2[i]))
try:
    num_str = input('Number(s): ').strip().split(',')
    if len(num_str) ==1 :
        num=int(num_str[0])
        assert num % 2 == 0   ,'Number must be even!'
        num1,num2=OneNumber(num)
        Show(num_str,num1,num2,False)
    else:
        num1_str,num2_str=num_str
        number1=int(num1_str)
        number2=int(num2_str)
        assert number1 % 2 == 0   ,'Number must be even!'
        if number2<number1:
            number1,number2=number2,number1
        if number1 == number2:
            pass
        num1,num2,list =RangeNumber(number1,number2)
except:
    print('Invalid Even Number ')