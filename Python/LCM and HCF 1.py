import numpy as np
from functools import reduce
#-----------------------------------------------------------------------------
#Check number not 0
def check(data):
    chk=[n!=0 for n in data]
    return all(chk)
#-----------------------------------------------------------------------------
#Main Code
number_list=input('Numbers :').strip()
sep=',' if ',' in number_list else ' '
try:
    numbers=list(map(int,number_list.split(sep)))
    assert check(numbers)
    print('HCF  = {0}'.format(np.gcd.reduce(numbers)))
    print('LCM  = {0}'.format(np.lcm.reduce(numbers)))
except :
    print('Invalid Info')