#This solution comes from these thinkings;
#1) 
#2)


from functools import reduce
from sympy import sieve
fact_list=[]
factors_Detail={}
factors_dict={}
#-----------------------------------------------------------------------------
#Check number not 0
def check(data):
    chk=[n!=0 for n in data]
    return all(chk)
#-----------------------------------------------------------------------------
def find_Detail(datum):
    num=datum
    fact_exp={1:1}
    global fact_list
    for i in fact_list:
        exp=0
        while True:
            if num % i == 0:
                exp+=1
                num=num//i
            else:
                if exp>0:
                    fact_exp[i]=exp
                break
    return fact_exp
#-----------------------------------------------------------------------------
#make dictionaries for LCM and HCF
def make_Dict(data,isLCM=True):
    dt={}
    for i in data:
        exp=[]
        for f in factors_dict:
            if i in f:
                exp.append(f[i])
        if isLCM: #LCM
            dt[i]=max(exp)
        else:#HCF
            dt[i]=min(exp)
    return dt          
#-----------------------------------------------------------------------------
def collect_Info(data):
    nums=sorted(data)
    #prepare prime list
    global fact_list,factors_Detail,factors_dict
    fact_list=[n for n in sieve.primerange(min(nums),(max(nums))+1)]
    for n in nums:
        factors_Detail[n]=find_Detail(n)
    #Collect factors to a set
    factors_dict=[v for v in factors_Detail.values() ]
    factors_by_number=[]
    for x in factors_dict:
        ans=[]
        for y in x.keys():
            ans.append(y)
        factors_by_number.append(set(ans))
    #find all factors appeared in all numbers
    factors_all_List=[n for m in factors_dict for n in m.keys()]
    factors_all=set(factors_all_List)
    #Find common factors of all numbers
    factors_common=reduce(set.intersection,factors_by_number)
    LCM_dict=make_Dict(factors_all)
    HCF_dict=make_Dict(factors_common,False)
    return LCM_dict,HCF_dict
#-----------------------------------------------------------------------------
def Calculate(data):
    total=1
    for k,v in data.items():
        total*=k**v
    return total
#-----------------------------------------------------------------------------
def Show(lcm_Data,hcf_Data):
    lcm=Calculate(lcm_Data)
    hcf=Calculate(hcf_Data)
    print()
    print('LCM = ',lcm)
    print('HCF = ',hcf)
#-----------------------------------------------------------------------------
#Main Code4
input_list=input('Numbers :').strip()
sep=',' if ',' in input_list else ' '
try:
    numbers=list(map(int,input_list.split(sep)))
    assert check((numbers))
    lcm_Info,hcf_Info=collect_Info(numbers)
    Show(lcm_Info,hcf_Info)
except :
    print('Invalid Info!')
