MAX_LIMIT=5
count=0
#--------------------------------------------------------
#Cut result in case of it's lenghth over LIMIT to avoid overflow if any
#Can increase limit if the number is too big
def cut(num):
    global count
    res=num
    while res % 10 == 0:
        count+=1
        res //= 10
    if len(str(res)) >MAX_LIMIT:
        res=int(str(res)[len(str(res))-MAX_LIMIT:])
    return res
#--------------------------------------------------------
def count_0(n,num):
    prod=cut(n)*cut(num)
    return cut(prod)
#--------------------------------------------------------
def Analyse(n):
    global count
    ans=1
    print('Calcucalting...')
    for i in range(2,n+1):
        ans=count_0(i,ans)
        #comment out to check
        print('Answer x {0} = {1} zero = {2}'.format(i,ans,count))
#--------------------------------------------------------
#Main Code
try:
    num=int(input('Number: '))
    assert num>=0
    Analyse(num)
    print('{0}! has {1} trailing zeros'.format(num,count))
except:
    print('Number is not positive integer!')