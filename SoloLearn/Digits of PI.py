# """
#This solution base on formular discovered by  David Bailey, Peter Borwein, and Simon Plouffe in 1995:
# Pi = SUM from  k=0 to infinity of ( 16^(-k))*[ 4/(8k+1) – 2/(8k+4) – 1/(8k+5) – 1/(8k+6) ]
# ref: https://math.hmc.edu/funfacts/finding-the-n-th-digit-of-pi/
# """
import math
from decimal import Decimal as dec , getcontext
getcontext().prec = 10000 # precision of display
def findN(n):
    #change to decimal since this formular return hex  numbers
    pi_sum = dec(0)
    for i in range(n):
        a=dec(math.pow(16, -i))
        b=dec(4/(8*i+1))
        c=dec(2/(8*i+4))
        d=dec(1/(8*i+5))
        e=dec(1/(8*i+6))
        pi_sum+=dec(a*(b-c-d-e))
    return str(pi_sum)[2:] # Take digits after decimal point
#------------------------------------------------------------------------------------------
try:
    nth= int(input(('N= ')))
    assert 0 < nth< 1001
    pi_Nth=findN(nth)
    print(pi_Nth)
    print(pi_Nth[nth-1])
except :
    print('Invalid!')
