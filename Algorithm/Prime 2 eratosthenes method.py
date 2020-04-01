import math
def getPrime (n):
    if n<=1:
        return []
    prime =[2]
    limit = int(math.sqrt(n))
    #make odd number list
    data=[n+1 for n in range(2,n,2)]
    while limit> data[0]:
        prime.append(data[0])
        #return not divisible number only 
        data=[n for n in data if n % data[0] !=0]
    return prime+data
print(getPrime(100))