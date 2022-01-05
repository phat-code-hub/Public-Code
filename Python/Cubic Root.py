import re
LIMIT =0.0001
basecubics=[x**3 for x in range(0,11)]
# sign=0 #0: Positive, 1 Negative number
#----------------------------------------------------
def Analyse(nstr):
    #save sign state and extract int part of number
    num0=float(nstr)
    parts=nstr.split('.')
    positive=parts[0]
    if len(parts)>1:
        decimal=parts[1]
    else:
        decimal=''
    if num0<0:
        signal =1
        positive=positive[1:]
    else:
        signal=0
    #cal tree digits multiple times in integer part
    int_repeat_times=(len(positive)-1)//3
    cubic_base=positive[:len(positive)-int_repeat_times*3]
    return abs(num0),cubic_base,int_repeat_times,decimal,signal
#-------------------------------------------------------
def isPerfectCubic(realNum,basecubic,times10):
    isCubic=False
    downbound=realNum
    if realNum ==0 or realNum >=1:
        for i in range(0,11):
            if basecubics[i] == int(basecubic):
                compareNum=int(basecubic)*10**(3*times10)
                if (float(realNum)-compareNum) == 0:
                    isCubic=True
                    downbound=i*10**times10
                    break
    return isCubic,downbound
#-----------------------------------------------------
#Calculate first apperance of decimal part and convert to 3 digits places repeat times 
def decimalRepeatTimes(decimals):
    reg=re.compile(r'[1-9]')
    m=reg.search(decimals)
    return (m.start()//3+1)
#-----------------------------------------------------
def difference(n, mid) : 
    if (n > (mid * mid * mid)) : 
        return (n - (mid * mid * mid)) 
    else : 
        return ((mid * mid * mid) - n) 
#------------------------------------------------------
def cubicRoot(n) : 
    start = 0
    end = n 
    while True : 
        mid = (start + end) / 2
        epsilon = difference(n, mid) 
        if (epsilon <= LIMIT) : 
            return mid 
        if ((mid * mid * mid) > n) : 
            end = mid 
        else : 
            start = mid 
#------------------------------------------------------
num_str= input('input number: ').strip()
num,base_num,times,decimal_str,sign=Analyse(num_str)
perfectCubic,cubic=isPerfectCubic(num,base_num,times)
if perfectCubic:
    print("Cubic root of", num_str, "is",  cubic*(-1)**sign)
else:
    if num<1:
        decimal_times=decimalRepeatTimes(decimal_str)
        num=num*(1000**decimal_times)
        root=round(cubicRoot(num)/(10**decimal_times),len(str(LIMIT))-1) * (-1)**sign
    else:
        root=round(cubicRoot(num),len(str(LIMIT))-1)*(-1)**sign
    print('Cubic root of {0} is {1}'.format(num_str,root))