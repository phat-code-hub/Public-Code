#This solution comes from rules of finding LCM and HCF;
#1) for example two numbers 60,126
#2) find all factors : 60 = 2^2*3*5 , 126=2*3^2*7
#3) HCF is calculated from to product all common factors
#   with their minimum exponential indexes (2*3)
# 4) LCM is came from to product all available factors, each
#   factors take maximum  exponential indexes (2^2*3^2*5*7)
#Note : 1)It can find for any numbers available not 0
#       2)With negative numbers inside, because there is no
#         referential documents so that may be sometimes the results
#        are unexpected one.  
from functools import reduce
from sympy import sieve
numbers=[]
fact_list=[]
factors_Detail={}
factors_dict={}
#-----------------------------------------------------------------------------
#Check number not 0
def check(data):
    chk=[n!=0 for n in data]
    return all(chk)
#-----------------------------------------------------------------------------
#divide 2 groups if having negative numbers
def devideGroup(data):
    pos_part=[]
    nev_part=[]
    for item in data:
        if item<0:
            nev_part.append(item)
        else:
            pos_part.append(item)
    return [nev_part,pos_part]
#-----------------------------------------------------------------------------
def find_Detail(datum,isNevgative=False):
    num=datum
    if isNevgative:
        fact_exp={-1:1}
    else:
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
    for item in data:
        exp=[]
        for f in factors_dict:
            if (item in f) :
                exp.append(f[item])
            if (-1)*item in f :
                exp.append(f[(-1)*item])
        if isLCM: #LCM
            dt[item]=max(exp)
        else:#HCF
            dt[item]=min(exp)
    return dt          
#-----------------------------------------------------------------------------
def collect_Info(data):
    #prepare factors check list
    global fact_list,factors_Detail,factors_dict
    nums=sorted(data)
    groups=devideGroup(nums)
    if len(groups[0])>0:#negative group
        start=-2
        end=groups[0][0]-1
        fact_list=[n for n in range(start,end,-1)]
        for n in groups[0]:
            factors_Detail[n]=find_Detail(n,True)
    if len(groups[1])>0:#positive group
        start=2
        end=groups[1][-1]+1
        fact_list=[n for n in range(start,end)]
        for n in groups[1]:
            factors_Detail[n]=find_Detail(n)
    #Collect factors to a set
    factors_dict=[v for v in factors_Detail.values()]
    factors_by_number=[]
    for x in factors_dict:
        ans=[]
        for y in x.keys():
            ans.append(abs(y))
        factors_by_number.append(set(ans))
    #find all factors appeared in all numbers
    factors_all_List=[abs(n) for m in factors_dict for n in m.keys()]
    factors_all=set(factors_all_List)
    #Find common factors of all numbers
    factors_common=reduce(set.intersection,factors_by_number)
    LCM_dict=make_Dict(factors_all)
    HCF_dict=make_Dict(factors_common,False)
    return LCM_dict,HCF_dict
#-----------------------------------------------------------------------------
def Calculate(data,isHCF=False):
    global numbers
    total=1
    for k,v in data.items():
        total*=k**v
    if isHCF:
        if (-1)*total in numbers:
            total=(-1)*total
    return total
#-----------------------------------------------------------------------------
def Show(lcm_Data,hcf_Data):
    global numbers
    lcm=Calculate(lcm_Data)
    hcf=Calculate(hcf_Data,True)
    print()
    print('LCM = ',lcm)
    print('HCF = ',hcf)
#-----------------------------------------------------------------------------
#Main Code4
input_list=input('Numbers (seperate by space or ,) :').strip()
sep=',' if ',' in input_list else ' '
try:
    numbers=list(map(int,input_list.split(sep)))
    assert check((numbers))
    lcm_Info,hcf_Info=collect_Info(numbers)
    Show(lcm_Info,hcf_Info)
except :
    print('Invalid Info!')
