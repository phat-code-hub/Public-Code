from sympy import sieve
def Show(num):
    prime_list=[p for p in sieve.primerange(2,(num//2)+1)]
    temp=num
    ans={}
    for i in prime_list:
        count=0
        while True:
            if temp % i ==0:
                count+=1
                temp=temp//i
            else:
                if count>0:
                    ans[str(i)]=str(count)
                break
    res=[n+' ^ '+ans[n] for n in ans.keys() ]
    print('{0} = {1}'.format(num,' * '.join(res)))
#-----------------------------------------------------------------
def play(nums,factors):
    if len(factors)>0:
        pass
#-----------------------------------------------------------------
#Main
try:
    number=int(input('Number: '))
    assert number>0
    Show(number)
except :
    print('Invalid number!')