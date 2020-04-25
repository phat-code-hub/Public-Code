import numpy as np
from functools import reduce
from sympy import sieve
fact_list=[]
factors_All={}
#-----------------------------------------------------------------------------
def findfactors_All(datum):
    num=datum
    dic={1:1}
    global fact_list
    for i in fact_list:
        count=0
        while True:
            if num % i == 0:
                count+=1
                num=num//i
            else:
                if count>0:
                    dic[i]=count
                break
    return dic
#-----------------------------------------------------------------------------
def collect_Info(data):
    nums=sorted(data)
    #prepare prime lisr
    global fact_list,factors_All
    fact_list=[n for n in sieve.primerange(1,(max(nums))+1)]
    for n in nums:
        factors_All[n]=findfactors_All(n)
    #Collect factors to set
      
#-----------------------------------------------------------------------------
#Main Code4
input_list=input('Numbers :').strip()
sep=',' if ',' in input_list else ' '
try:
    numbers=list(map(int,input_list.split(sep)))
    collect_Info(numbers)
    print(factors_All)
except :
    print('Invalid Info')
