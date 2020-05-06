from sympy import sieve
def checkUgly(n):
    if n==1:
        return True
    else:
        factors=[f for f in sieve.primerange(1,n+1) if n % f ==0]
        return max(factors)<=5
#-----------------------------------------------
number= int(input('Number: '))
assert number>0
print(checkUgly(number))