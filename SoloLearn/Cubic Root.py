basecubics=[x**3 for x in range(0,11)]
print(basecubics)

# sign=0 #0: Positive, 1 Negative number
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
    return abs(num0),cubic_base,times0,signal
#-------------------------------------------------------
def isPerfectCubic(realNum,basecubic,times10):
    isCubic=False
    downbound=realNum
    for i in range(0,11):
        if basecubics[i] == int(basecubic):
            compareNum=int(basecubic)*10**(3*times10)
            if (float(realNum)-compareNum) == 0:
                isCubic=True
                downbound=i*10**times10
                break
    return isCubic,downbound
#-----------------------------------------------------
LIMIT =0.0001
def epsilon(n, mid) : 
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
        error = epsilon(n, mid) 
        if (error <= LIMIT) : 
            return mid 
        if ((mid * mid * mid) > n) : 
            end = mid 
        else : 
            start = mid 
#------------------------------------------------------
num_str= input('input number: ').strip()
num,base_num,times,sign=Analyse(num_str)
perfectCubic,cubic=isPerfectCubic(num,base_num,times)
if perfectCubic:
    print("Cubic root of", num_str, "is",  cubic*(-1)**sign)
else:
    if num<1:
        num=num*1000
        ans=cubicRoot(num)  
        print("Cubic root of", num_str, "is",  round(ans/10,5)*(-1)**sign)
    else:
        ans=cubicRoot(num)  
        print("Cubic root of", num_str, "is",  round(ans,5)*(-1)**sign)