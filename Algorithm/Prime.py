import math
def isPrime(n):
    """ Confirm n is prime number or not """
    if  n <= 1:
        return False
    else:
        for i in range(2,int(math.sqrt(n))+1):
            if n % i == 0:
                return False
    return True
def PrimeInRange(min=2,max=100,isprint=True):
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
PrimeInRange(2,65,True)