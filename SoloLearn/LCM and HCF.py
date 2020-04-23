import numpy as np
from functools import reduce
from sympy import sieve
#-----------------------------------------------------------------------------
#Collect all factors of all given numbers and their frequency
def factors_infos(num):
    ans={num:1}
    for j in sieve.primerange(2,num//2+1):
        count=0
        while True:
            if num % j ==0:
                count +=1
                num=num//j
            else:
                if count>0:
                    ans[j]=count
                break
    return ans
#-----------------------------------------------------------------------------
def findLCB(results,num_list):
    #extract factors and frequency list of each number
    factors_dict=[n for n in results.values()]
    #from extract data , collect factors and remove duplicated ones to set
    factors_list=[list(n.keys()) for n in factors_dict]
    print(factors_dict)
    print(factors_list)
    factor_set = set(np.array(factors_list).ravel())
    #if length of set > total of given numbers , remove these numbers themselve in set  
    if len(factor_set)>len(num_list):
        for datum in num_list:
            factor_set.remove(datum)
    print(factor_set)
    #from set , find max frequency for all factors
    final_factors_dict={}
    for factor in factor_set:
        final_factors_dict[factor]=0
        for item in factors_dict:
            if factor in item :
                final_factors_dict[factor]=max(final_factors_dict[factor],item[factor])
                continue
    print(final_factors_dict)
    #Calculate productsum of all factors
    total=1
    for key in final_factors_dict.keys():
        total*=key**final_factors_dict[key]
    return total
#-----------------------------------------------------------------------------
def AnalyseLCM(data):
    res={}
    for i in data:
        res[i]=factors_infos(i)
    return findLCB(res,data)
#-----------------------------------------------------------------------------
def showHCF(result,nums):
    if len(nums)==2:
        print('{0} is the HCF of {1} and {2}'.format(result,nums[0],nums[1]))
    else:
        num_str=','.join(list(map(str,nums)))
        print('{0} is the HCF of {1}'.format(result,num_str))
#-----------------------------------------------------------------------------
#Find LCF 
def AnalyseHCF(data):
    all_factors=[]
    for n in data:
        res=[1,n]
        for i in range(2,n//2+1):
            if n % i == 0:
                res.append(i)
        all_factors.append(res)
    #Find common numbers of all factors found and choose the greatest one
    hcf_result=sorted(reduce(np.intersect1d,all_factors))
    return hcf_result[-1]
#Main Code
input_list=input('Numbers :').strip()
sep=',' if ',' in input_list else ' '
try:
    numbers=list(map(int,input_list.split(sep)))
    # hcf=AnalyseHCF(numbers)
    lcm=AnalyseLCM(numbers)
    print('lcm=',lcm)
    # showHCF(hcf,numbers)
except :
    print('Invalid Info')
