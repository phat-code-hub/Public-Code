from string import hexdigits, digits
def Convert_fromDEC(tobased,n):
    """Convert form 10_based number to n_based number """
    ans=''
    num=int(n)
    base=int(tobased)
    while num>0:
        ans =str( num % base) + ans
        num=num // base
    return ans
#--------------------------------------------------------------
def Convert_toDEC(frombased,n):
    """Convert form n_based number to DEC_based number """
    num=str(n) 
    lenN=len(str(n))
    base=int(frombased)
    ans=0
    for i in range(0,lenN):
        ans += int(num[i])*base**(lenN-i-1)
    return ans
#--------------------------------------------------------------
def Convert(fromNum, toNum, n):
    fromN=int(fromNum)
    toN=int(toNum)
    return Convert_fromDEC(toN,Convert_toDEC(fromN,n))
##--------------------------------------------------------------  
# number_to_Convert=input('number: ')
# base_to_convert = input('to Base: ')
# print(Convert_fromDEC(base_to_convert,number_to_Convert))
# number_to_Convert=input('number: ')
# base_to_convert = input('to Base: ')
# print(Convert_toDEC(base_to_convert,number_to_Convert))
from_Number=input('convert from base: ')
to_Number=input('to base: ')
number=input('number: ')
print(Convert(from_Number,to_Number,number))