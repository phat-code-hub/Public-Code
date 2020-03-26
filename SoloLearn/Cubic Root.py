basecubics=[x**3 for x in range(0,11)]
print(basecubics)
LIMIT=0.0001
sign=0 #0: Positive, 1 Negative number
#----------------------------------------------------
def Analyse(nstr):
    #save sign state and extract int part of number
    num0=float(nstr)
    parts=nstr.split('.')
    positive=parts[0]
    if num0<0:
        signal =1
        positive=positive[1:]
    else:
        signal=0
    #cal tree digits multiple times
    times0=(len(positive)-1)//3
    cubic_base=positive[:len(positive)-times0*3]
    return abs(num0),positive,cubic_base,times0,signal
#-------------------------------------------------------
def SearchBound(realNum,basecubic,times10):
    isRealCubic=False
    for i in range(0,11):
        if basecubics[i] == int(basecubic):
            compareNum=int(basecubic)*10**(3*times10)
            if (float(realNum)-compareNum) == 0:
                isRealCubic=True
                upbound=i*10**times10
                downbound=upbound
            else:
                downbound=i*10**times10
                upbound=(i+1)*10**times10
            break
        elif basecubics[i]>int(basecubic):
            upbound=i*10**times10
            downbound=(i-1)*10**times10
            break
    return downbound,upbound,isRealCubic
def RootCal(minLimit,maxLimit,number,times_10):
    found=False
    ans=minLimit
    count=0
    while  not found:
        temp1=minLimit**3
        temp2=maxLimit**3
        delta1=abs(number-temp1)
        delta2=abs(temp2-number)
        print(temp1,temp2,delta1,delta2,count)
        if delta1 <= LIMIT:
            found=True
            ans=minLimit
        elif delta2 <=LIMIT:
            found=True
            ans=maxLimit
        else:
            count +=1
            mid=(minLimit+maxLimit)/2
            if delta1>delta2:
                minLimit=mid
            elif delta1<delta2:
                maxLimit=mid
            else:
                minLimit=mid/3
            continue
    return ans
#-------------------------------------------------------------
num_str= input('input number: ').strip()
num,int_num,base_num,times,sign=Analyse(num_str)
# print(num,int_num,base_num,times,sign)
min,max,isCompleteCubic=SearchBound(num,base_num,times)
print(min,max)
if isCompleteCubic:
    cubicRoot=min*((-1)**sign)
else:
    cubicRoot=RootCal(min,max,num,base_num)
print('Cubic Root of {0} is {1}'.format (num_str,cubicRoot))