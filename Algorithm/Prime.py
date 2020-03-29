def isPrime(n):
    """ Confirm n is prime number or not """
    if  n == 1:
        ans=True
    else:
        ans=True
        for i in range(2,n):
            if n % i == 0:
                ans=False
                break
    return ans
def PrimeInRange(min=1,max=100,isprint=True):
    """ List prime numbers in min and max range """
    list=[]
    if min==0:
        min=1
    for n in range(min,max+1):
        if isPrime(n):
            list.append(n)
    if isprint:
        for n in list:
            print(n)
