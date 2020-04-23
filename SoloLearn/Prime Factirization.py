from sympy import sieve
#----------------------------------------------
def Analyse(num):
    ans={}
    #prepare prime numbers up to given number 
    primes=list(sieve.primerange(2,num+1))
    #loop to find  prime and it's repeat 
    for i in primes:
        count=0
        while True:
            if num % i ==0 :
                count+=1
                num=num//i
            else:
                if count>0:
                    ans[str(i)]=str(count)
                break
    return ans
#----------------------------------------------
def showResult(num,result):
    res=''
    for k,v in  result.items():
        res+=k+' ^ '+v +' * '
    print('{0} = {1}'.format(num,res[:-3]))
#----------------------------------------------
number=int(input('Natural Number :'))
primes_info=Analyse(number)
showResult(number,primes_info)