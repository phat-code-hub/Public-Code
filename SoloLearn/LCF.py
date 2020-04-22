import numpy as np
from sympy import sieve
def findFactors(data):
    print(len(data))
input_list=input('Numbers :').strip()
sep=',' if ',' in input_list else ' '
numbers=list(map(int,input_list.split(sep)))
findFactors(numbers)