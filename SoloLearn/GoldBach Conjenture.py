import math
from sympy import sieve
def OneNumber(n,isRange=False):
    n1=[]
    n2=[]
    num_list=[]
    prime_list=[x for x in sieve.primerange(1,n)]
    for i in prime_list:
        if (n-i) in prime_list:
            n1.append(i)
            n2.append(n-i)
            num_list.append(n)
    if len(n1) % 2 ==0:
        limit=len(n1)//2
    else:
        limit=len(n1)//2+1
    n1=n1[:limit]
    n2=n2[:limit]
    num_list=num_list[:limit]
    if isRange:
         for i in range(len(n1)):
            print('{0}: {1} + {2}'.format(num_list[i],n1[i],n2[i]))
    else:    
        for i in range(len(n1)):
            print('{0} + {1}'.format(n1[i],n2[i]))
def RangeNumber(n1,n2):
    numbs=[]
    num1_ls=[]
    num2_ls=[]
    for i in range(n1,n2+1,2):
        OneNumber(i,True)
try:
    num_str = input('Number(s): ').strip().split(',')
    if len(num_str) ==1 :
        num=int(num_str[0])
        assert num % 2 == 0   ,'Number must be even!'
        OneNumber(num)
    else:
        num1_str,num2_str=num_str
        number1=int(num1_str)
        number2=int(num2_str)
        assert number1 % 2 == 0   ,'Number must be even!'
        if number2<number1:
            number1,number2=number2,number1
        if number1 == number2:
            OneNumber(number1)
        else:
            RangeNumber(number1,number2)
except:
    print('Invalid Even Number ')