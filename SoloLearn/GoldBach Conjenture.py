import math
from sympy import sieve
def OneNumber(n):
    results=dict()
    prime_list=[x for x in sieve.primerange(1,n)]
    for i in prime_list:
        if (n-i) in prime_list:
            results[i] = n-i
    return results
def RangeNumber(n1,n2):
    pass
info = input('Number(s): ').strip().split(',')
if len(info) ==1 :
    print(OneNumber(int(info[0])))
else:
    num1,num2=info
    RangeNumber(int(num1),int(num2))